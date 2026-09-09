"""Offline case validation, response capture and explicitly human paired evaluation."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
import os
from pathlib import Path
import random
import re
import statistics
import sys
from typing import Any

from scripts.modules import (
    CORE, OPERATIONS, ROOT, DocumentError, Module, digest, module_names,
    section_ranges, source_text, token_count, validate_selection,
)


VARIANTS = ("task-only", "legacy-modules", "legacy-quick", "full", "compact")
FAILURES = (
    "unsupported_claim", "changed_meaning", "source_identity",
    "invented_verification", "disclosure_or_privacy", "unsafe_action",
)
CASE_FIELDS = {
    "schema_version", "id", "split", "operation", "task", "input", "source_kind",
    "facts", "modules", "safeguards", "checks",
}
REQUEST_FIELDS = {
    "schema_version", "kind", "case", "case_sha256", "split", "operation",
    "variant", "instructions", "input", "prompt", "prompt_sha256", "prompt_tokens", "manifest",
    "request_sha256",
}
RESULT_FIELDS = {
    "schema_version", "kind", "status", "metadata_source", "request", "response",
    "response_sha256", "model", "family", "settings", "result_sha256",
}
KEY_FIELDS = {
    "schema_version", "kind", "comparison_kind", "pair_id", "seed", "a", "b", "key_sha256",
}
JUDGMENT_FIELDS = {
    "schema_version", "pair_key", "pair_id", "reviewer_id", "assessor",
    "human_attestation", "winner", "rationale", "hard_failures",
    "important_regressions",
}
HASH = re.compile(r"[0-9a-f]{64}")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DocumentError(message)


def fields(value: Any, expected: set[str], label: str) -> None:
    require(isinstance(value, dict), f"{label}: expected an object")
    missing, unknown = expected - value.keys(), value.keys() - expected
    require(not missing and not unknown,
            f"{label}: missing fields {sorted(missing)}; unknown fields {sorted(unknown)}")


def nonempty(value: Any, label: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected nonempty text")
    return value


def strings(value: Any, label: str) -> list[str]:
    require(isinstance(value, list), f"{label}: expected a list")
    for item in value:
        nonempty(item, label)
    require(len(set(value)) == len(value), f"{label}: duplicate entries")
    return value


def version(value: dict) -> None:
    require(type(value["schema_version"]) is int and value["schema_version"] == 1,
            "schema_version must be the integer 1")


def canonical(value: Any) -> str:
    try:
        text = json.dumps(value, ensure_ascii=False, allow_nan=False,
                          sort_keys=True, separators=(",", ":"))
        text.encode("utf-8")
        return text
    except (ValueError, TypeError, UnicodeError, RecursionError) as error:
        raise DocumentError(f"expected finite UTF-8 JSON: {error}") from error


def unique_object(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def parse_json(text: str) -> Any:
    try:
        value = json.loads(text, object_pairs_hook=unique_object)
    except (ValueError, RecursionError) as error:
        raise DocumentError(f"invalid JSON: {error}") from error
    canonical(value)  # Also rejects NaN, Infinity and overflowing exponents.
    return value


def read_text(path: Path) -> str:
    try:
        return path.read_bytes().decode("utf-8")
    except (OSError, UnicodeError) as error:
        raise DocumentError(f"{path}: cannot read UTF-8: {error}") from error


def load_json(path: Path) -> Any:
    return parse_json(read_text(path))


def write_new(path: Path, text: str) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as output:
            output.write(text.encode("utf-8"))
    except (OSError, UnicodeError) as error:
        raise DocumentError(f"{path}: cannot create artifact (no overwrites): {error}") from error


def write_json(path: Path, value: Any) -> None:
    canonical(value)
    write_new(path, json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n")


def seal(value: dict, name: str) -> dict:
    return {**value, name: digest(canonical(value))}


def verify_seal(value: dict, name: str) -> None:
    require(isinstance(value.get(name), str) and HASH.fullmatch(value[name]) is not None,
            f"{name}: expected a SHA-256 digest")
    require(value[name] == digest(canonical({k: v for k, v in value.items() if k != name})),
            f"{name}: hash mismatch")


def optional_modules(root: Path) -> set[str]:
    return set(module_names(root)) - set(CORE)


def validate_case(root: Path, case: Any, filename: str | None = None) -> dict:
    fields(case, CASE_FIELDS, "case")
    version(case)
    nonempty(case["id"], "case id")
    require(re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", case["id"]) is not None,
            "case id must be kebab-case")
    require(filename is None or case["id"] == Path(filename).stem,
            "case id must match the filename stem")
    require(case["split"] in ("tuning", "held_out"), "invalid case split")
    require(case["operation"] in OPERATIONS, "invalid operation")
    require(case["source_kind"] == "synthetic", "only original synthetic cases are supported")
    nonempty(case["task"], "task")
    require(isinstance(case["input"], str), "input must be a string")
    require(case["operation"] == "draft" or bool(case["input"].strip()),
            "edit/review input must not be empty")
    require(isinstance(case["facts"], list), "facts must be a list")
    fact_ids = set()
    for fact in case["facts"]:
        fields(fact, {"id", "text"}, "fact")
        nonempty(fact["id"], "fact id")
        require(re.fullmatch(r"f[1-9][0-9]*", fact["id"]) is not None, "invalid fact id")
        require(fact["id"] not in fact_ids, "duplicate fact id")
        fact_ids.add(fact["id"])
        nonempty(fact["text"], "atomic fact")
    selected = strings(case["modules"], "modules")
    require(set(selected) <= optional_modules(root),
            "modules must name known optional .md paths; core is automatic; sources/raw-data are forbidden")
    safeguards = strings(case["safeguards"], "safeguards")
    require(set(safeguards) <= {"medical", "legal"},
            "safeguards may contain only medical and legal")
    validate_selection([Module.load(root, path) for path in selected], safeguards)
    for name in safeguards:
        Module.load(root, f"domain/{name}.md").section("Safeguards")
    checks = case["checks"]
    fields(checks, {"required_facts", "forbidden_additions", "preserve", "expected_action"}, "checks")
    required = strings(checks["required_facts"], "required_facts")
    require(set(required) <= fact_ids, "required_facts references a missing fact")
    strings(checks["forbidden_additions"], "forbidden_additions")
    strings(checks["preserve"], "preserve")
    actions = {
        "draft": ("draft", "flag_missing_evidence"),
        "edit": ("edit", "no_change", "flag_missing_evidence"),
        "review": ("review", "no_change", "flag_missing_evidence"),
    }
    require(checks["expected_action"] in actions[case["operation"]],
            "expected_action is incompatible with operation")
    canonical(case)
    return case


def load_cases(root: Path, directory: Path | None = None) -> list[dict]:
    cases, seen = [], set()
    for path in sorted((directory or root / "evals/cases").rglob("*.json")):
        try:
            case = validate_case(root, load_json(path), path.name)
        except DocumentError as error:
            raise DocumentError(f"{path}: {error}") from error
        require(case["id"] not in seen, f"duplicate case id: {case['id']}")
        seen.add(case["id"])
        cases.append(case)
    return cases


def coverage(root: Path, cases: list[dict]) -> dict:
    splits = Counter(case["split"] for case in cases)
    no_change = sum(case["checks"]["expected_action"] == "no_change" for case in cases)
    covered = {path for case in cases for path in case["modules"]}
    missing = sorted(optional_modules(root) - covered)
    issues = []
    if len(cases) < 40 or splits["tuning"] < 16 or splits["held_out"] < 24:
        issues.append("The suite requires at least 40 cases: at least 16 tuning and 24 held_out.")
    if no_change < 8:
        issues.append("At least eight no_change cases are required.")
    if missing:
        issues.append("Some optional modules have no case coverage.")
    return {
        "cases": len(cases), "tuning": splits["tuning"], "held_out": splits["held_out"],
        "no_change": no_change, "covered_modules": sorted(covered),
        "missing_modules": missing, "issues": issues,
    }


def instructions_for(root: Path, case: dict, variant: str) -> tuple[str, dict]:
    require(variant in VARIANTS, "unknown instruction variant")
    operation = case["operation"]
    if variant in ("full", "compact"):
        from scripts.build import assemble

        return assemble(root, case["modules"], operation=operation, variant=variant,
                        safeguards=case["safeguards"])
    manifest: dict[str, Any] = {
        "schema_version": 1, "operation": operation, "variant": variant,
        "modules": [], "examples": [], "tokenizer": "o200k_base",
        "evaluation_status": "not_evaluated",
    }
    if variant == "task-only":
        contract_source = source_text(root, "prompts/task.md")
        contract = contract_source.strip()
        sections = section_ranges(contract)
        names = ("Shared contract", operation.capitalize(), "Completion")
        require(all(name in sections for name in names), "task contract is missing required sections")
        text = f"# Editorial task: {operation}\n\n" + "\n\n".join(
            contract[slice(*sections[name])].strip() for name in names
        ) + "\n"
        manifest.update(contract_source_sha256=digest(contract_source),
                        omitted_optional_modules=case["modules"], omitted_safeguards=case["safeguards"])
    else:
        require(not case["safeguards"],
                "legacy variants do not support standalone safeguard selections")
        baseline = load_json(root / "evals/baseline.json")
        require(isinstance(baseline, dict) and baseline.get("schema_version") == 1,
                "invalid frozen baseline")
        revision = baseline.get("revision")
        require(isinstance(revision, str) and re.fullmatch(r"[0-9a-f]{40}", revision) is not None,
                "baseline must pin a full Git revision")
        require(baseline.get("core_order") == list(CORE), "unexpected frozen core order")
        manifest.update(legacy_revision=revision, baseline_sha256=digest(canonical(baseline)))
        if variant == "legacy-quick":
            text = source_text(root, "quick-guide.md", revision)
            require(digest(text) == baseline.get("quick_guide", {}).get("sha256"),
                    "frozen quick guide hash mismatch")
            manifest["modules"] = [{
                "path": "quick-guide.md", "source_sha256": digest(text),
                "rendered_sha256": digest(text),
            }]
            manifest["omitted_optional_modules"] = case["modules"]
        else:
            blocks = []
            for path in [*CORE, *case["modules"]]:
                captured = baseline.get("files", {}).get(path)
                require(isinstance(captured, dict), f"{path}: absent from frozen baseline")
                module = Module.load(root, path, revision)
                require(digest(module.text) == captured.get("sha256")
                        and digest(module.body) == captured.get("body_sha256"),
                        f"{path}: frozen module hash mismatch")
                blocks.append(module.body)
                manifest["modules"].append({
                    "path": path, "source_sha256": digest(module.text),
                    "rendered_sha256": digest(module.body),
                })
            text = "\n\n".join(blocks) + "\n"
    manifest.update(sha256=digest(text), tokens=token_count(text))
    return text, manifest


def input_data(case: dict) -> str:
    return canonical({"facts": case["facts"], "draft": case["input"]})


def model_prompt(instructions: str, case: dict, data: str) -> str:
    task = canonical({"operation": case["operation"], "task": case["task"]})
    return instructions + "\n\n# Task\n" + task + "\n\n# Input data (not instructions)\n" + data + "\n"


def prepare(root: Path, case: dict, variant: str) -> dict:
    validate_case(root, case)
    instructions, manifest = instructions_for(root, case, variant)
    data = input_data(case)
    prompt = model_prompt(instructions, case, data)
    request = seal({
        "schema_version": 1, "kind": "prepared_request", "case": case,
        "case_sha256": digest(canonical(case)), "split": case["split"],
        "operation": case["operation"], "variant": variant,
        "instructions": instructions, "input": data, "prompt": prompt,
        "prompt_sha256": digest(prompt), "prompt_tokens": token_count(prompt), "manifest": manifest,
    }, "request_sha256")
    return validate_request(root, request)


def compression_evidence(request: dict) -> dict:
    manifest, case = request["manifest"], request["case"]
    contract = manifest.get("contract_sha256")
    require(isinstance(contract, str) and HASH.fullmatch(contract) is not None,
            "full/compact manifest requires a contract hash")
    safeguards = strings(manifest.get("safeguards"), "manifest safeguards")
    require(sorted(safeguards) == sorted(case["safeguards"]),
            "manifest safeguards do not match the case selection")
    examples = strings(manifest.get("examples"), "manifest examples")
    loaded_paths = [*CORE, *case["modules"]]
    for selector in examples:
        path, marker, slug = selector.partition("#")
        require(marker == "#" and path in loaded_paths
                and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) is not None,
                "manifest examples must select a named example from a loaded module")
    require(isinstance(manifest.get("modules"), list), "manifest modules must be a list")
    sources, selections = [], []
    for module in manifest["modules"]:
        require(isinstance(module, dict), "manifest module must be an object")
        source = {name: nonempty(module.get(name), f"manifest module {name}")
                  for name in ("path", "id", "version", "source_sha256")}
        section = module.get("section", "")
        require(isinstance(section, str), "manifest module section must be a string")
        source["section"] = section
        selections.append((source["path"], section))
        # Compact changes core rendering only, not optional rules or safeguards.
        if source["path"] not in CORE or section:
            source["rendered_sha256"] = nonempty(module.get("rendered_sha256"), "rendered module hash")
        sources.append(source)
    expected = [(path, "") for path in loaded_paths]
    expected.extend((f"domain/{name}.md", "Safeguards") for name in safeguards)
    require(Counter(selections) == Counter(expected),
            "manifest source module/section selections do not match the case and automatic core")
    return {"contract_sha256": contract, "modules": sources,
            "safeguards": sorted(safeguards), "examples": examples}


def validate_rendered_pack(text: str, manifest: dict) -> None:
    require(text.endswith("\n"), "rendered payload must end with a newline")
    remaining = text[:-1]
    for module in reversed(manifest["modules"]):
        path = module["path"]
        if module.get("section") == "Safeguards":
            opening = f'\n\n<safeguards kind="{Path(path).stem}">\n'
            closing = "\n</safeguards>"
        else:
            opening = f'\n\n<module path="{path}">\n'
            closing = "\n</module>"
        require(remaining.endswith(closing), f"{path}: rendered payload boundary mismatch")
        end = len(remaining) - len(closing)
        start = remaining.rfind(opening, 0, end)
        # A quoted example may itself contain a wrapper; its hash identifies the real boundary.
        while start >= 0:
            if digest(remaining[start + len(opening):end]) == module["rendered_sha256"]:
                break
            start = remaining.rfind(opening, 0, start)
        require(start >= 0, f"{path}: rendered payload does not match its module hash")
        remaining = remaining[:start]
    require(digest(remaining) == manifest["contract_sha256"],
            "rendered payload does not match its contract hash")


def validate_request(root: Path, request: Any) -> dict:
    fields(request, REQUEST_FIELDS, "request")
    version(request)
    require(request["kind"] == "prepared_request", "not a prepared request")
    verify_seal(request, "request_sha256")
    case = validate_case(root, request["case"])
    require(request["case_sha256"] == digest(canonical(case)), "case hash mismatch")
    require(request["split"] == case["split"] and request["operation"] == case["operation"],
            "request case metadata mismatch")
    require(request["variant"] in VARIANTS, "unknown request variant")
    nonempty(request["instructions"], "instructions")
    require(request["input"] == input_data(case), "input does not match the case")
    require(request["prompt"] == model_prompt(request["instructions"], case, request["input"]),
            "prompt does not match its exact instructions/task/input")
    require(request["prompt_sha256"] == digest(request["prompt"]), "prompt hash mismatch")
    require(type(request["prompt_tokens"]) is int
            and request["prompt_tokens"] == token_count(request["prompt"]),
            "prompt token count mismatch")
    manifest = request["manifest"]
    require(isinstance(manifest, dict), "manifest must be an object")
    require(manifest.get("sha256") == digest(request["instructions"]), "manifest instruction hash mismatch")
    require(manifest.get("variant") == request["variant"]
            and manifest.get("operation") == request["operation"], "manifest selection mismatch")
    require(manifest.get("tokenizer") == "o200k_base"
            and type(manifest.get("tokens")) is int
            and manifest["tokens"] == token_count(request["instructions"]), "manifest token count mismatch")
    require(isinstance(manifest.get("modules"), list), "manifest modules must be a list")
    allowed = set(module_names(root))
    if request["variant"] == "legacy-quick":
        allowed.add("quick-guide.md")
    for module in manifest["modules"]:
        require(isinstance(module, dict) and isinstance(module.get("path"), str)
                and module["path"] in allowed, "manifest contains a forbidden module path")
        for name in ("source_sha256", "rendered_sha256"):
            require(isinstance(module.get(name), str) and HASH.fullmatch(module[name]) is not None,
                    f"manifest {name}: invalid hash")
    if request["variant"] in ("full", "compact"):
        compression_evidence(request)
        validate_rendered_pack(request["instructions"], manifest)
    return request


def validate_settings(settings: Any) -> None:
    require(isinstance(settings, dict), "settings must be a JSON object")
    canonical(settings)

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            for key, nested in value.items():
                require(isinstance(key, str), "settings keys must be strings")
                normalized = re.sub(r"[^a-z0-9]", "", key.lower())
                forbidden = ("apikey", "password", "passwd", "secret", "authorization",
                             "credential", "privatekey", "accesstoken", "refreshtoken", "authtoken",
                             "apitoken", "sessiontoken", "signingkey", "bearer")
                require(normalized not in {"token", "auth", "cookie", "setcookie"}
                        and not any(word in normalized for word in forbidden),
                        "settings contain an obvious credential key; remove credentials before capture")
                visit(nested)
        elif isinstance(value, list):
            for nested in value:
                visit(nested)

    visit(settings)


def record(root: Path, request: dict, response: str, model: str, family: str, settings: dict) -> dict:
    validate_request(root, request)
    nonempty(response, "response")
    nonempty(model, "declared model snapshot")
    nonempty(family, "declared model family")
    require(model == model.strip(), "model snapshot must not have surrounding whitespace")
    require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", family) is not None,
            "family must be a lowercase nonempty slug")
    validate_settings(settings)
    return seal({
        "schema_version": 1, "kind": "response_record", "status": "captured-unreviewed",
        "metadata_source": "operator-supplied-unverified", "request": request,
        "response": response, "response_sha256": digest(response),
        "model": model, "family": family, "settings": settings,
    }, "result_sha256")


def validate_result(root: Path, result: Any) -> dict:
    fields(result, RESULT_FIELDS, "result")
    version(result)
    verify_seal(result, "result_sha256")
    expected = record(root, result["request"], result["response"], result["model"],
                      result["family"], result["settings"])
    require(result == expected, "result hash, status or declared metadata mismatch")
    return result


def comparison_kind(first_variant: str, second_variant: str) -> str:
    if {first_variant, second_variant} == {"full", "compact"}:
        return "matched-compression"
    if first_variant.startswith("legacy-") or second_variant.startswith("legacy-"):
        return "legacy-instruction-comparison"
    return "instruction-ablation"


def compatible(first: dict, second: dict) -> str:
    a, b = first["request"], second["request"]
    require(a["variant"] != b["variant"], "a pair must compare different variants")
    require(a["case_sha256"] == b["case_sha256"] and a["case"]["id"] == b["case"]["id"]
            and a["operation"] == b["operation"], "incompatible pair: case/hash/operation differs")
    require(all(first[key] == second[key] for key in ("model", "family"))
            and canonical(first["settings"]) == canonical(second["settings"]),
            "incompatible pair: model/family/settings differs")
    if comparison_kind(a["variant"], b["variant"]) == "matched-compression":
        require(compression_evidence(a) == compression_evidence(b),
                "incompatible matched compression: source modules/order, contract, safeguards, "
                "example selections or non-core rendered rules differ")
    return digest(canonical(sorted([first["result_sha256"], second["result_sha256"]])))


def blind(root: Path, first: Path, second: Path, output: Path, seed: int) -> dict:
    records = [(path, validate_result(root, load_json(path))) for path in (first, second)]
    pair_id = compatible(records[0][1], records[1][1])
    records.sort(key=lambda entry: entry[1]["result_sha256"])
    random.Random(seed).shuffle(records)
    key: dict[str, Any] = {
        "schema_version": 1, "kind": "blind_key", "pair_id": pair_id, "seed": seed,
        "comparison_kind": comparison_kind(
            records[0][1]["request"]["variant"], records[1][1]["request"]["variant"],
        ),
    }
    for side, (path, result) in zip(("a", "b"), records):
        key[side] = {
            "result": os.path.relpath(path.resolve(), output.resolve()),
            "result_sha256": result["result_sha256"],
        }
    key = seal(key, "key_sha256")
    try:
        output.mkdir(parents=True, exist_ok=False)
    except OSError as error:
        raise DocumentError(f"{output}: blind output directory must be new: {error}") from error
    for side, (_, result) in zip(("a", "b"), records):
        write_new(output / f"{side}.txt", result["response"])
    write_json(output / "key.json", key)
    return key


def read_pair(root: Path, path: Path) -> tuple[dict, dict[str, dict]]:
    key = load_json(path)
    fields(key, KEY_FIELDS, "blind key")
    version(key)
    verify_seal(key, "key_sha256")
    require(key["kind"] == "blind_key" and type(key["seed"]) is int, "invalid blind key")
    records = {}
    for side in ("a", "b"):
        fields(key[side], {"result", "result_sha256"}, f"blind {side}")
        nonempty(key[side]["result"], "result path")
        result = validate_result(root, load_json(path.parent / key[side]["result"]))
        require(result["result_sha256"] == key[side]["result_sha256"], "blind result hash mismatch")
        require(read_text(path.parent / f"{side}.txt") == result["response"], "blinded text was changed")
        records[side] = result
    require(key["pair_id"] == compatible(records["a"], records["b"]), "blind pair id mismatch")
    require(key["comparison_kind"] == comparison_kind(
        records["a"]["request"]["variant"], records["b"]["request"]["variant"],
    ), "blind comparison kind mismatch")
    return key, records


def passage(value: Any, response: str) -> None:
    nonempty(value, "quoted passage")
    require(value in response, "quoted passage is not present in the corresponding response")


def validate_judgment(judgment: Any, records: dict[str, dict]) -> None:
    fields(judgment, JUDGMENT_FIELDS, "human judgment")
    version(judgment)
    require(judgment["assessor"] == "human" and judgment["human_attestation"] is True,
            "explicit human assessor and true human_attestation are required")
    reviewer = nonempty(judgment["reviewer_id"], "reviewer_id")
    require(re.fullmatch(r"reviewer-[0-9a-f]{8,32}", reviewer) is not None,
            "use a non-identifying reviewer ID: reviewer- followed by 8–32 random hex digits")
    require(judgment["winner"] in ("a", "b", "tie"), "winner must be a, b or tie")
    fields(judgment["rationale"], {"a", "b", "reason"}, "rationale")
    nonempty(judgment["rationale"]["reason"], "rationale reason")
    fields(judgment["hard_failures"], {"a", "b"}, "hard_failures")
    fields(judgment["important_regressions"], {"a", "b"}, "important_regressions")
    for side in ("a", "b"):
        passage(judgment["rationale"][side], records[side]["response"])
        failures = judgment["hard_failures"][side]
        require(isinstance(failures, list), "hard_failures sides must be lists")
        for failure in failures:
            fields(failure, {"category", "passage", "requirement", "reason"}, "hard failure")
            require(failure["category"] in FAILURES, "unknown hard-failure category")
            passage(failure["passage"], records[side]["response"])
            nonempty(failure["requirement"], "violated fact or requirement")
            nonempty(failure["reason"], "hard-failure reason")
        require(type(judgment["important_regressions"][side]) is bool,
                "important_regressions sides must be boolean flags")


def interval(scores: list[float], seed: int) -> list[float] | None:
    # Very small samples do not get an apparently conclusive degenerate interval.
    if len(scores) < 8:
        return None
    rng = random.Random(seed)
    samples = sorted(statistics.mean(rng.choices(scores, k=len(scores))) for _ in range(5000))
    quantiles = statistics.quantiles(samples, n=40, method="inclusive")
    return [quantiles[0], quantiles[-1]]


def summarize(rows: list[dict], cases: list[dict], seed: int) -> dict:
    pairs: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        pairs[row["pair_id"]].append(row)
    by_model_case: dict[tuple[str, str], list[float]] = defaultdict(list)
    for assessments in pairs.values():
        first = assessments[0]
        by_model_case[(first["cohort"], first["case_id"])].append(
            statistics.mean(row["score"] for row in assessments)
        )
    by_case: dict[str, list[float]] = defaultdict(list)
    for (_, case_id), scores in by_model_case.items():
        by_case[case_id].append(statistics.mean(scores))
    assessed = set(by_case)
    held_out = {case["id"] for case in cases if case["split"] == "held_out"}
    scores = [statistics.mean(by_case[case_id]) for case_id in sorted(assessed & held_out)]
    held_out_rows = [row for row in rows if row["case_id"] in held_out]
    return {
        "human_judgments": len(rows), "unique_pairs": len(pairs),
        "wins": sum(row["score"] == 1 for row in rows),
        "ties": sum(row["score"] == 0.5 for row in rows),
        "losses": sum(row["score"] == 0 for row in rows),
        "assessed_cases": sorted(assessed),
        "missing_cases": sorted({case["id"] for case in cases} - assessed),
        "held_out": {
            "human_judgments": len(held_out_rows),
            "wins": sum(row["score"] == 1 for row in held_out_rows),
            "ties": sum(row["score"] == 0.5 for row in held_out_rows),
            "losses": sum(row["score"] == 0 for row in held_out_rows),
            "assessed_cases": sorted(assessed & held_out),
            "missing_cases": sorted(held_out - assessed),
            "case_weighted_score": statistics.mean(scores) if scores else None,
            "ci95": interval(scores, seed),
        },
        "disagreements": sorted(pair_id for pair_id, assessments in pairs.items()
                                if len({row["score"] for row in assessments}) > 1),
    }


def report(
    root: Path, judgments_path: Path, candidate: str, baseline: str, *,
    case_dir: Path | None = None, seed: int = 1729,
) -> dict:
    require(candidate in VARIANTS and baseline in VARIANTS and candidate != baseline,
            "choose two different known variants")
    cases = load_cases(root, case_dir)
    suite = coverage(root, cases)
    case_hashes = {case["id"]: digest(canonical(case)) for case in cases}
    rows, hard_failures, regressions = [], [], []
    seen, model_families, cohorts = set(), {}, {}
    pair_cache = {}
    snapshots: dict[tuple[str, str, str], Any] = {}

    def match_snapshot(key: tuple[str, str, str], value: Any) -> None:
        require(key not in snapshots or snapshots[key] == value,
                f"mixed instruction snapshots for {' / '.join(key)}; report revisions separately")
        snapshots[key] = value

    text = read_text(judgments_path) if judgments_path.exists() else ""
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        judgment = parse_json(line)
        fields(judgment, JUDGMENT_FIELDS, f"judgment line {line_number}")
        key_path = judgments_path.parent / nonempty(judgment["pair_key"], "pair_key")
        key_path = key_path.resolve()
        if key_path not in pair_cache:
            pair_cache[key_path] = read_pair(root, key_path)
        key, records = pair_cache[key_path]
        validate_judgment(judgment, records)
        require(judgment["pair_id"] == key["pair_id"], "judgment pair_id does not match its key")
        identity = (key["pair_id"], judgment["reviewer_id"])
        require(identity not in seen, "duplicate pair/reviewer judgment")
        seen.add(identity)
        require({result["request"]["variant"] for result in records.values()} == {candidate, baseline},
                "judgment does not compare the requested candidate and baseline")
        for captured in records.values():
            request = captured["request"]
            variant, manifest = request["variant"], request["manifest"]
            match_snapshot(("prompt", variant, request["case"]["id"]), request["prompt_sha256"])
            contract = manifest.get("contract_sha256", manifest.get("contract_source_sha256"))
            if contract is not None:
                match_snapshot(("contract", variant, request["operation"]), contract)
            for module in manifest["modules"]:
                match_snapshot(("source", variant, module["path"]),
                               (module.get("id"), module.get("version"), module["source_sha256"]))
            for field in ("legacy_revision", "baseline_sha256"):
                if field in manifest:
                    match_snapshot(("legacy", variant, field), manifest[field])
        candidate_side = next(side for side, result in records.items()
                              if result["request"]["variant"] == candidate)
        result = records[candidate_side]
        case_id = result["request"]["case"]["id"]
        require(case_hashes.get(case_id) == result["request"]["case_sha256"],
                "judged case hash is absent from or changed in the current case suite")
        model, family, settings = result["model"], result["family"], result["settings"]
        require(model not in model_families or model_families[model] == family,
                "one model snapshot has conflicting declared families")
        model_families[model] = family
        cohort = canonical([model, family, settings])
        cohorts[cohort] = {"model": model, "family": family, "settings": settings}
        score = 0.5 if judgment["winner"] == "tie" else int(judgment["winner"] == candidate_side)
        context = {"pair_id": key["pair_id"], "reviewer_id": judgment["reviewer_id"],
                   "case_id": case_id, "model": model, "family": family}
        rows.append({**context, "cohort": cohort, "score": score})
        for side in ("a", "b"):
            label = "candidate" if side == candidate_side else "baseline"
            for failure in judgment["hard_failures"][side]:
                hard_failures.append({**context, "side": label, **failure})
            if judgment["important_regressions"][side]:
                regressions.append({**context, "side": label,
                                    "passage": judgment["rationale"][side],
                                    "reason": judgment["rationale"]["reason"]})
    overall = summarize(rows, cases, seed)
    per_model = [
        {**metadata, **summarize([row for row in rows if row["cohort"] == cohort], cases, seed)}
        for cohort, metadata in sorted(cohorts.items())
    ]
    families = sorted(set(model_families.values()))
    incomplete = list(suite["issues"])
    if not rows:
        incomplete.append("No explicitly human assessments are available.")
    if overall["missing_cases"]:
        incomplete.append("Every case is a mandatory hard case; some have no human assessment.")
    if len(families) < 2:
        incomplete.append("At least two declared model families are required.")
    if any(model["missing_cases"] for model in per_model):
        incomplete.append("Every observed model/settings cohort must cover the entire suite.")
    if len(overall["held_out"]["assessed_cases"]) < 24:
        incomplete.append("At least 24 held-out cases must be assessed; a pilot is not release evidence.")
    candidate_failures = sum(item["side"] == "candidate" for item in hard_failures)
    candidate_regressions = sum(item["side"] == "candidate" for item in regressions)
    ci = overall["held_out"]["ci95"]
    superior = ci is not None and ci[0] > 0.5
    if incomplete:
        status = "incomplete"
    elif candidate_failures or candidate_regressions:
        status = "blocked"
    elif not superior:
        status = "inconclusive"
    else:
        status = "superiority_supported"
    return {
        "schema_version": 1, "kind": "human_evaluation_report",
        "candidate": candidate, "baseline": baseline, "release_status": status,
        "comparison_kind": comparison_kind(candidate, baseline),
        "inputs": {
            "judgments_path": str(judgments_path), "judgments_sha256": digest(text),
            "judgments_present": judgments_path.exists(),
            "case_suite_sha256": digest(canonical(cases)),
            "instruction_snapshots_sha256": digest(canonical(sorted(snapshots.items()))),
            "assessed_pair_ids": sorted({row["pair_id"] for row in rows}),
        },
        "superiority_gate": {
            "passed": status == "superiority_supported", "incomplete_reasons": incomplete,
            "candidate_fidelity_failures": candidate_failures,
            "candidate_important_regressions": candidate_regressions,
            "held_out_lower_bound_above_half": superior,
            "declared_families": families,
        },
        "suite": suite, **overall, "per_model": per_model,
        "hard_failures": hard_failures, "important_regressions": regressions,
        "method": {
            "assessment_source": "explicitly human; attestation and model metadata are not independently verified",
            "counts_unit": "human judgments, not independent samples",
            "independent_unit": "case; average reviewers per pair, pairs per model/settings, then models per case",
            "uncertainty": "held-out case-clustered percentile bootstrap; no interval below eight cases",
            "bootstrap_samples": 5000, "seed": seed,
            "limitations": "No semantic auto-grading, model authentication, or proof of blinding/held-out non-exposure.",
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="validate structure and initial-suite coverage, not quality")
    validate.add_argument("--cases", type=Path)
    prepare_parser = commands.add_parser("prepare", help="export an exact prompt; never invokes a model")
    prepare_parser.add_argument("case", type=Path)
    prepare_parser.add_argument("--variant", choices=VARIANTS, required=True)
    prepare_parser.add_argument("--output", type=Path, required=True)
    record_parser = commands.add_parser("record", help="capture an unmodified, operator-provided real response")
    record_parser.add_argument("request", type=Path)
    for name in ("response", "settings", "output"):
        record_parser.add_argument(f"--{name}", type=Path, required=True)
    for name in ("model", "family"):
        record_parser.add_argument(f"--{name}", required=True)
    blind_parser = commands.add_parser("blind", help="export text and a private mapping key")
    blind_parser.add_argument("first", type=Path)
    blind_parser.add_argument("second", type=Path)
    blind_parser.add_argument("--output", type=Path, required=True)
    blind_parser.add_argument("--seed", type=int, required=True)
    report_parser = commands.add_parser("report", help="summarize only attested human judgments")
    report_parser.add_argument("judgments", type=Path)
    report_parser.add_argument("--candidate", choices=VARIANTS, required=True)
    report_parser.add_argument("--baseline", choices=VARIANTS, required=True)
    report_parser.add_argument("--output", type=Path, required=True)
    report_parser.add_argument("--cases", type=Path)
    report_parser.add_argument("--seed", type=int, default=1729)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            result = coverage(args.root, load_cases(args.root, args.cases))
            print(json.dumps({"status": "incomplete" if result["issues"] else "valid_structure",
                              **result}, indent=2))
            return int(bool(result["issues"]))
        if args.command == "prepare":
            case = validate_case(args.root, load_json(args.case), args.case.name)
            write_json(args.output, prepare(args.root, case, args.variant))
        elif args.command == "record":
            value = record(args.root, load_json(args.request), read_text(args.response),
                           args.model, args.family, load_json(args.settings))
            write_json(args.output, value)
        elif args.command == "blind":
            blind(args.root, args.first, args.second, args.output, args.seed)
        else:
            value = report(args.root, args.judgments, args.candidate, args.baseline,
                           case_dir=args.cases, seed=args.seed)
            write_json(args.output, value)
            print(value["release_status"])
            return int(not value["superiority_gate"]["passed"])
    except (DocumentError, OSError) as error:
        print(f"evaluate: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
