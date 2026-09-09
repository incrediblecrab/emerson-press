"""Source-aware model judgments, not human reviews or publication approval.

Builders keep record identities outside the judge-facing prompt. Run with an
externally started generate.LiveTransport (or a test transport with its receipt
contract). No SDK, model, credential, or subprocess calls occur on import.

Each job is exactly {"id": str, "request": sealed_request}. Resume is
verification-only unless continue_unstarted=True explicitly permits first
attempts for untouched jobs. Failed or incomplete attempts are never repeated.
Hashes establish local consistency, not provider authenticity or judge accuracy.
Literal self-identifying article text is retained; no identifying metadata is
added to the prompt. The caller owns eligibility, registration and statistics.
"""

from __future__ import annotations

import asyncio
from copy import deepcopy
from datetime import datetime
from pathlib import Path
import random
import re
from typing import Any

from scripts import evaluate, generate
from scripts.modules import DocumentError, digest


TEMPLATES = {
    "preference": "evals/newsroom/preference-prompt.md",
    "pointwise": "evals/newsroom/source-aware-pointwise-prompt.md",
}
WORD_COUNT_NOTE = (
    "Each supplied word_count is the objectively computed number of "
    "whitespace-separated words in the ENTIRE unchanged response, including "
    "headlines and commentary. Use this count instead of guessing. "
    "A soft word target alone is not a factual falsehood."
)
REQUEST_FIELDS = {
    "schema_version", "kind", "assessor", "model", "template", "bindings",
    "data", "data_sha256", "prompt", "prompt_sha256", "request_sha256",
}
CAPTURE_FIELDS = {
    "requested_prompt_sha256", "effective_user_message",
    "effective_user_message_sha256", "response", "response_sha256", "usage",
    "started_at", "completed_at",
}


def paragraphs(text: str) -> dict[int, str]:
    """Number all unchanged material; attach blank-line separators to the prior part."""
    evaluate.nonempty(text, "article response")
    pieces = re.split(r"((?:\r?\n)[ \t]*(?:\r?\n)+)", text)
    parts = [
        pieces[index] + (pieces[index + 1] if index + 1 < len(pieces) else "")
        for index in range(0, len(pieces), 2)
    ]
    content, prefix = [], ""
    for part in parts:
        if part.strip():
            content.append(prefix + part)
            prefix = ""
        elif content:
            content[-1] += part
        else:
            prefix += part
    result = {number: part for number, part in enumerate(content, 1)}
    evaluate.require("".join(result.values()) == text, "paragraphs lost response material")
    return result


def _model(value: Any) -> str:
    evaluate.nonempty(value, "judge model")
    evaluate.require(
        not any(character.isspace() for character in value)
        and value.lower() not in ("auto", "default"),
        "judge model must be an explicit model identifier",
    )
    return value


def _article(text: str) -> dict:
    return {
        "text": text,
        "evidence": [{"id": number, "text": part} for number, part in paragraphs(text).items()],
        "word_count": len(text.split()),
    }


def _prompt(template: str, data: dict) -> str:
    return template + "\n" + WORD_COUNT_NOTE + "\nINPUT DATA:\n" + evaluate.canonical(data)


def _request(root: Path, records: dict[str, dict], model: str, kind: str) -> dict:
    _model(model)
    for record in records.values():
        evaluate.validate_result(root, record)
        evaluate.require(
            record["request"]["operation"] == "draft"
            and record["request"]["variant"] in ("full", "bare-task"),
            "newsroom judgments require full or bare-task draft records",
        )
    first = next(iter(records.values()))
    case = first["request"]["case"]
    source = {"task": case["task"], "facts": deepcopy(case["facts"])}
    bindings = {
        "case_id": case["id"], "case_sha256": first["request"]["case_sha256"],
        "operation": "draft", "source_sha256": digest(evaluate.canonical(source)),
        "writer_model": first["model"], "writer_family": first["family"],
        "writer_settings_sha256": digest(evaluate.canonical(first["settings"])),
        "records": {side: record["result_sha256"] for side, record in records.items()},
        "requests": {side: record["request"]["request_sha256"] for side, record in records.items()},
        "responses": {side: record["response_sha256"] for side, record in records.items()},
        "variants": {side: record["request"]["variant"] for side, record in records.items()},
    }
    if kind == "preference":
        bindings["pair_id"] = evaluate.compatible(records["a"], records["b"])
        bindings["candidate_side"] = next(
            side for side, record in records.items() if record["request"]["variant"] == "full"
        )
        data = {**source, **{side: _article(record["response"]) for side, record in records.items()}}
    else:
        data = {**source, **_article(first["response"])}
    template_text = evaluate.read_text(root / TEMPLATES[kind])
    evaluate.nonempty(template_text, "judge template")
    prompt = _prompt(template_text, data)
    return evaluate.seal({
        "schema_version": 1, "kind": kind, "assessor": "model", "model": model,
        "template": {"path": TEMPLATES[kind], "text": template_text, "sha256": digest(template_text)},
        "bindings": bindings, "data": data, "data_sha256": digest(evaluate.canonical(data)),
        "prompt": prompt, "prompt_sha256": digest(prompt),
    }, "request_sha256")


def preference_request(
    root: Path, first_record: dict, second_record: dict, judge_model: str,
) -> dict:
    """Prepare A=first_record, B=second_record; candidate is inferred from full."""
    return _request(root, {"a": first_record, "b": second_record}, judge_model, "preference")


def pointwise_request(root: Path, record: dict, judge_model: str) -> dict:
    """Prepare a single source-aware assessment without exposing its condition."""
    return _request(root, {"article": record}, judge_model, "pointwise")


def _local_request(request: Any) -> dict:
    evaluate.fields(request, REQUEST_FIELDS, "newsroom judgment request")
    evaluate.version(request)
    evaluate.verify_seal(request, "request_sha256")
    evaluate.require(request["kind"] in ("preference", "pointwise"), "unknown judgment kind")
    evaluate.require(request["assessor"] == "model", "only model assessments are supported")
    _model(request["model"])
    template = request["template"]
    evaluate.fields(template, {"path", "text", "sha256"}, "judge template")
    evaluate.nonempty(template["text"], "judge template text")
    evaluate.require(
        template["path"] == TEMPLATES[request["kind"]]
        and template["sha256"] == digest(template["text"]), "template binding mismatch",
    )
    data = request["data"]
    article_fields = {"text", "evidence", "word_count"}
    expected_fields = {"task", "facts", "a", "b"} if request["kind"] == "preference" \
        else {"task", "facts", *article_fields}
    evaluate.fields(data, expected_fields, "judge-facing data")
    evaluate.nonempty(data["task"], "visible task")
    evaluate.require(isinstance(data["facts"], list), "visible facts must be a list")
    for fact in data["facts"]:
        evaluate.fields(fact, {"id", "text"}, "visible fact")
        evaluate.nonempty(fact["id"], "visible fact id")
        evaluate.nonempty(fact["text"], "visible fact text")
    articles = [data["a"], data["b"]] if request["kind"] == "preference" else [
        {key: data[key] for key in article_fields}
    ]
    for article in articles:
        evaluate.fields(article, article_fields, "judge article")
        evaluate.require(
            evaluate.canonical(article) == evaluate.canonical(_article(article["text"])),
            "article evidence or whole-response word count mismatch",
        )
    evaluate.require(
        request["data_sha256"] == digest(evaluate.canonical(data))
        and request["prompt"] == _prompt(template["text"], data)
        and request["prompt_sha256"] == digest(request["prompt"]),
        "judge payload or prompt binding mismatch",
    )
    return request


def validate_request(
    root: Path, request: dict, records_by_result_sha256: dict[str, dict],
) -> dict:
    """Rebuild from trusted records and current templates, not supplied metadata."""
    _local_request(request)
    evaluate.require(isinstance(records_by_result_sha256, dict), "records must be a hash-keyed object")
    bindings = request["bindings"]
    evaluate.require(isinstance(bindings, dict), "request bindings must be an object")
    sides = {"a", "b"} if request["kind"] == "preference" else {"article"}
    evaluate.fields(bindings.get("records"), sides, "bound records")
    records = {}
    for side in sorted(sides):
        sha = bindings["records"][side]
        evaluate.require(
            isinstance(sha, str) and evaluate.HASH.fullmatch(sha) is not None
            and sha in records_by_result_sha256, "unknown or invalid bound result hash",
        )
        record = records_by_result_sha256[sha]
        evaluate.validate_result(root, record)
        evaluate.require(record["result_sha256"] == sha, "record-map key does not match result hash")
        records[side] = record
    expected = _request(root, records, request["model"], request["kind"])
    evaluate.require(
        evaluate.canonical(request) == evaluate.canonical(expected),
        "request differs from its records, source, orientation, or current template",
    )
    return request


def _evidence(value: Any, known: dict[int, str], required: bool) -> list[dict]:
    evaluate.require(
        isinstance(value, list)
        and all(type(identifier) is int and identifier in known for identifier in value),
        "evidence must contain supplied integer paragraph IDs",
    )
    evaluate.require(len(value) == len(set(value)), "duplicate evidence paragraph IDs")
    evaluate.require(not required or bool(value), "this assessment requires nonempty evidence")
    return [{"id": identifier, "text": known[identifier]} for identifier in value]


def parse_assessment(request: dict, raw_response: str) -> tuple[dict, Any]:
    """Parse without repairs; provenance additionally requires validate_request."""
    _local_request(request)
    evaluate.nonempty(raw_response, "judge response")
    text = raw_response.strip()
    if text.startswith("```json\n") and text.endswith("\n```"):
        text = text[8:-4]
    value = evaluate.parse_json(text)
    if request["kind"] == "preference":
        evaluate.fields(value, {"winner", "reason", "evidence_a", "evidence_b"}, "preference")
        evaluate.require(value["winner"] in ("a", "b", "tie"), "unknown preference winner")
        evaluate.nonempty(value["reason"], "preference reason")
        evidence = {
            side: _evidence(value[f"evidence_{side}"], paragraphs(request["data"][side]["text"]), True)
            for side in ("a", "b")
        }
    else:
        evaluate.fields(value, {"level", "reason", "evidence", "fidelity", "fidelity_reason"}, "pointwise")
        evaluate.require(value["level"] in ("absent", "minor", "salient", "unassessable"),
                         "unknown generic-writing level")
        evaluate.require(value["fidelity"] in ("no_flag", "flag", "uncertain"), "unknown fidelity state")
        evaluate.nonempty(value["reason"], "pointwise reason")
        evaluate.nonempty(value["fidelity_reason"], "fidelity reason")
        evidence = _evidence(
            value["evidence"], paragraphs(request["data"]["text"]),
            value["level"] in ("minor", "salient") or value["fidelity"] == "flag",
        )
    return value, evidence


def _settings(transport: Any, models: set[str]) -> dict:
    settings = getattr(transport, "settings", None)
    evaluate.require(isinstance(settings, dict), "transport must supply model settings")
    result = {}
    for model in sorted(models):
        evaluate.require(model in settings, f"transport has no settings for {model}")
        value = settings[model]
        evaluate.validate_settings(value)
        evaluate.require(value.get("model_selection") == model, "transport model selection mismatch")
        if "system_message_config_sha256" in value:
            options = value.get("session_options")
            evaluate.require(isinstance(options, dict) and "system_message" in options,
                             "system configuration is missing")
            evaluate.require(
                value["system_message_config_sha256"] == digest(evaluate.canonical(options["system_message"])),
                "system configuration hash mismatch",
            )
        result[model] = deepcopy(value)
    return result


def _validate_capture(capture: Any, request: dict) -> dict:
    evaluate.fields(capture, CAPTURE_FIELDS, "transport capture")
    evaluate.canonical(capture)
    evaluate.require(isinstance(capture["response"], str), "captured response must be text")
    evaluate.nonempty(capture["effective_user_message"], "effective user message")
    evaluate.require(
        capture["requested_prompt_sha256"] == request["prompt_sha256"]
        and capture["response_sha256"] == digest(capture["response"])
        and capture["effective_user_message_sha256"] == digest(capture["effective_user_message"]),
        "capture prompt, effective-message, or response hash mismatch",
    )
    evaluate.require(isinstance(capture["usage"], list) and bool(capture["usage"]),
                     "capture requires observed model/usage evidence")
    allowed = {*generate.USAGE_FIELDS, "nano_ai_credits"}
    for usage in capture["usage"]:
        evaluate.require(isinstance(usage, dict) and set(usage) <= allowed, "unknown usage metadata")
        evaluate.require(usage.get("model") == request["model"], "observed judge model mismatch")
        for key in ("numToolCalls", "availableToolCount"):
            evaluate.require(type(usage.get(key)) is int and usage[key] == 0,
                             f"judge capture must explicitly report zero {key}")
        evaluate.require(not usage.get("contentFilterTriggered", False), "judge capture was filtered")
    try:
        started = datetime.fromisoformat(capture["started_at"])
        completed = datetime.fromisoformat(capture["completed_at"])
        evaluate.require(started.tzinfo is not None and completed.tzinfo is not None
                         and completed >= started, "invalid capture timestamps")
    except (TypeError, ValueError) as error:
        raise DocumentError("invalid capture timestamps") from error
    return capture


def _assessment(job: dict, plan: dict, capture: dict) -> dict:
    request = job["request"]
    value, evidence = parse_assessment(request, capture["response"])
    return evaluate.seal({
        "schema_version": 1, "kind": "newsroom-model-assessment", "assessor": "model",
        "status": "model-assessed-unverified", "job_id": job["id"],
        "plan_sha256": plan["plan_sha256"], "request_sha256": request["request_sha256"],
        "model": request["model"], "settings_sha256": digest(evaluate.canonical(
            plan["model_settings"][request["model"]],
        )),
        "capture_sha256": digest(evaluate.canonical(capture)),
        "response_sha256": capture["response_sha256"], "assessment": value, "evidence": evidence,
    }, "assessment_sha256")


def _saved(path: Path) -> Any:
    evaluate.require(not path.is_symlink(), "saved artifacts must not be symlinks")
    return evaluate.load_json(path)


def _completed(job: dict, plan: dict, target: Path) -> dict:
    evaluate.require(
        evaluate.canonical(_saved(target / "request.json"))
        == evaluate.canonical(job["request"]), "saved request differs from the planned request",
    )
    capture = _validate_capture(_saved(target / "capture.json"), job["request"])
    stored = _saved(target / "assessment.json")
    expected = _assessment(job, plan, capture)
    evaluate.require(evaluate.canonical(stored) == evaluate.canonical(expected),
                     "saved assessment or capture was changed")
    return {"status": "captured", "assessment_sha256": stored["assessment_sha256"],
            "capture_sha256": stored["capture_sha256"]}


def _latest_summary(output: Path, plan: dict, names: set[str]) -> dict | None:
    continuations = sorted(output.glob("continuation-*.json"))
    if not (output / "summary.json").exists():
        evaluate.require(not continuations, "continuation history is missing its initial summary")
        return None
    previous = None
    for index, path in enumerate([output / "summary.json", *continuations]):
        summary = _saved(path)
        evaluate.fields(summary, {
            "schema_version", "kind", "assessor", "plan_sha256", "status", "planned_jobs",
            "captured_jobs", "jobs", "continuation_index", "previous_summary_sha256",
            "limitation", "summary_sha256",
        }, "judgment summary")
        evaluate.version(summary)
        evaluate.verify_seal(summary, "summary_sha256")
        evaluate.require(
            summary["kind"] == "newsroom-model-judgment-summary" and summary["assessor"] == "model"
            and summary.get("plan_sha256") == plan["plan_sha256"]
            and type(summary.get("continuation_index")) is int and summary["continuation_index"] == index
            and summary.get("previous_summary_sha256") == (
                previous["summary_sha256"] if previous is not None else None
            )
            and isinstance(summary.get("jobs"), dict) and set(summary["jobs"]) == names,
            "saved summary history does not match the frozen plan",
        )
        for row in summary["jobs"].values():
            evaluate.require(isinstance(row, dict)
                             and row.get("status") in ("captured", "failed", "blocked", "not_started"),
                             "invalid saved job status")
        captured = sum(row["status"] == "captured" for row in summary["jobs"].values())
        evaluate.require(
            type(summary["planned_jobs"]) is int and summary["planned_jobs"] == len(names)
            and type(summary["captured_jobs"]) is int and summary["captured_jobs"] == captured
            and summary["status"] == ("captured" if captured == len(names) else "incomplete"),
            "saved summary counts or status disagree with its jobs",
        )
        if index:
            evaluate.require(path.name == f"continuation-{index:04d}-{summary['summary_sha256'][:16]}.json",
                             "unexpected continuation filename")
        if previous is not None:
            for name, old in previous["jobs"].items():
                new = summary["jobs"][name]
                if old["status"] == "captured":
                    evaluate.require(new == old, "completed capture changed across continuation summaries")
                elif "failure_sha256" in old:
                    evaluate.require(new.get("failure_sha256") == old["failure_sha256"]
                                     and new["status"] in ("failed", "blocked"),
                                     "failed attempt changed across continuation summaries")
                elif old["status"] == "blocked":
                    evaluate.require(new["status"] == "blocked", "incomplete attempt was replaced")
        previous = summary
    return previous


def _existing_attempt(job: dict, plan: dict, output: Path, prior: dict | None) -> dict | None:
    name, request = job["id"], job["request"]
    target = output / name
    evaluate.require(not target.is_symlink(), "job directory must not be a symlink")
    old = prior["jobs"][name] if prior is not None else None
    if (target / "failure.json").exists():
        evaluate.require(old is None or old["status"] != "captured",
                         "a completed attempt was replaced with a failure")
        failure = _saved(target / "failure.json")
        evaluate.verify_seal(failure, "failure_sha256")
        evaluate.require(failure.get("plan_sha256") == plan["plan_sha256"]
                         and failure.get("request_sha256") == request["request_sha256"]
                         and failure.get("job_id") == name
                         and failure.get("stage") in ("transport", "capture_validation", "assessment", "artifact"),
                         "saved failure binding mismatch")
        evaluate.require(evaluate.canonical(_saved(target / "request.json"))
                         == evaluate.canonical(request), "failed request changed")
        if failure["capture_sha256"] is not None:
            evaluate.require(
                digest(evaluate.canonical(_saved(target / "capture.json"))) == failure["capture_sha256"],
                "failed capture changed",
            )
        if old is not None and old["status"] != "not_started":
            evaluate.require(old.get("failure_sha256") == failure["failure_sha256"],
                             "saved failure differs from the saved summary")
        return {"status": "blocked", "reason": "prior failed attempt retained; no retry",
                "failure_sha256": failure["failure_sha256"], "stage": failure["stage"]}
    if all((target / filename).is_file() for filename in ("request.json", "capture.json", "assessment.json")):
        result = _completed(job, plan, target)
        if old is not None and old["status"] != "not_started":
            evaluate.require(old == result, "completed capture differs from the saved summary")
        return result
    if target.exists():
        evaluate.require(
            old is None or old["status"] not in ("captured", "failed") and "failure_sha256" not in old,
            "a previously completed/failed attempt lost its artifacts",
        )
        return {"status": "blocked", "reason": "prior incomplete attempt retained; no retry"}
    evaluate.require(old is None or old["status"] == "not_started",
                     "an attempted job directory disappeared; refusing a new capture")
    return None


async def run_jobs(
    root: Path, jobs: list[dict], records_by_result_sha256: dict[str, dict],
    output: Path, transport: Any, *, concurrency: int = 4, order_seed: int = 731,
    resume: bool = False, continue_unstarted: bool = False,
) -> dict:
    """Capture once; verify existing runs or explicitly continue untouched jobs."""
    evaluate.require(type(concurrency) is int and concurrency > 0, "concurrency must be a positive integer")
    evaluate.require(type(order_seed) is int, "order_seed must be an integer")
    evaluate.require(type(resume) is bool, "resume must be a boolean")
    evaluate.require(type(continue_unstarted) is bool and (not continue_unstarted or resume),
                     "continue_unstarted requires explicit resume=True")
    evaluate.require(isinstance(jobs, list) and bool(jobs), "jobs must be a nonempty list")
    errors = generate.transport_errors(transport)
    frozen = deepcopy(jobs)
    names, observations = set(), set()
    for job in frozen:
        evaluate.fields(job, {"id", "request"}, "judge job")
        name = evaluate.nonempty(job["id"], "job id")
        evaluate.require(re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name) is not None,
                         "job id must be a safe lowercase filename")
        evaluate.require(name not in ("plan.json", "summary.json"), "job id collides with a run artifact")
        evaluate.require(name not in names, "duplicate job id")
        names.add(name)
        request = validate_request(root, job["request"], records_by_result_sha256)
        identity = (request["kind"], request["model"], tuple(sorted(request["bindings"]["records"].values())))
        evaluate.require(identity not in observations, "duplicate record/pair and judge observation")
        observations.add(identity)
    frozen.sort(key=lambda job: job["id"])
    settings = _settings(transport, {job["request"]["model"] for job in frozen})
    shuffled = list(frozen)
    random.Random(order_seed).shuffle(shuffled)
    plan = evaluate.seal({
        "schema_version": 1, "kind": "newsroom-model-judgment-plan", "assessor": "model",
        "requests": {job["id"]: job["request"]["request_sha256"] for job in frozen},
        "model_settings": settings, "order_seed": order_seed, "concurrency": concurrency,
        "launch_order": [job["id"] for job in shuffled],
        "judge_module_sha256": digest(evaluate.read_text(Path(__file__))),
        "transport_module_sha256": digest(evaluate.read_text(Path(generate.__file__))),
    }, "plan_sha256")
    output = Path(output)
    evaluate.require(not output.is_symlink(), "judge output must not be a symlink")
    prior = None
    if resume:
        evaluate.require(evaluate.canonical(_saved(output / "plan.json"))
                         == evaluate.canonical(plan), "resume plan, source, request, or model settings changed")
        prior = _latest_summary(output, plan, names)
    else:
        try:
            output.mkdir(mode=0o700, parents=True, exist_ok=False)
        except OSError as error:
            raise DocumentError(f"judge output must be new: {error}") from error
        evaluate.write_json(output / "plan.json", plan)
    results: dict[str, dict] = {}
    if resume:
        for job in frozen:
            result = _existing_attempt(job, plan, output, prior)
            if result is not None:
                results[job["id"]] = result
            elif not continue_unstarted:
                results[job["id"]] = {"status": "not_started", "reason": "verification-only resume; no new capture"}
    failures = 0
    semaphore = asyncio.Semaphore(concurrency)

    async def execute(job: dict) -> None:
        nonlocal failures
        async with semaphore:
            name, request = job["id"], job["request"]
            if name in results:
                return
            target = output / name
            evaluate.require(not target.is_symlink(), "job directory must not be a symlink")
            if failures >= 3:
                results[name] = {"status": "not_started", "reason": "three transport failures; circuit breaker"}
                return
            target.mkdir(mode=0o700, exist_ok=False)
            evaluate.write_json(target / "request.json", request)
            stage, capture_sha = "transport", None
            try:
                evaluate.require(evaluate.canonical(_settings(transport, set(settings))) == evaluate.canonical(settings),
                                 "transport settings changed")
                capture = await transport.capture(request["model"], request["prompt"])
                stage = "capture_validation"
                evaluate.write_json(target / "capture.json", capture)
                capture_sha = digest(evaluate.canonical(capture))
                evaluate.require(evaluate.canonical(_settings(transport, set(settings))) == evaluate.canonical(settings),
                                 "transport settings changed")
                _validate_capture(capture, request)
                stage = "assessment"
                assessment = _assessment(job, plan, capture)
                stage = "artifact"
                evaluate.write_json(target / "assessment.json", assessment)
                results[name] = {"status": "captured", "assessment_sha256": assessment["assessment_sha256"],
                                 "capture_sha256": capture_sha}
            except errors as error:
                transport_failure = stage in ("transport", "capture_validation")
                failures += int(transport_failure)
                failure = evaluate.seal({
                    "schema_version": 1, "kind": "newsroom-model-judgment-failure", "assessor": "model",
                    "job_id": name, "plan_sha256": plan["plan_sha256"],
                    "request_sha256": request["request_sha256"], "capture_sha256": capture_sha,
                    "stage": stage, "transport_failure": transport_failure,
                    "error_type": type(error).__name__, "error": str(error),
                }, "failure_sha256")
                evaluate.write_json(target / "failure.json", failure)
                results[name] = {"status": "failed", "failure_sha256": failure["failure_sha256"],
                                 "stage": stage, "error_type": type(error).__name__}
            print(evaluate.canonical({"job": name, **results[name]}), flush=True)

    await asyncio.gather(*(execute(job) for job in shuffled))
    index = prior["continuation_index"] if prior is not None else 0
    predecessor = prior["previous_summary_sha256"] if prior is not None else None
    if continue_unstarted and prior is not None:
        index += 1
        predecessor = prior["summary_sha256"]
    summary = evaluate.seal({
        "schema_version": 1, "kind": "newsroom-model-judgment-summary", "assessor": "model",
        "plan_sha256": plan["plan_sha256"],
        "status": "captured" if all(row["status"] == "captured" for row in results.values()) else "incomplete",
        "planned_jobs": len(frozen),
        "captured_jobs": sum(row["status"] == "captured" for row in results.values()),
        "jobs": dict(sorted(results.items())),
        "continuation_index": index, "previous_summary_sha256": predecessor,
        "limitation": "Model opinions can be wrong; exact evidence is not human verification or release evidence.",
    }, "summary_sha256")
    if not resume:
        evaluate.write_json(output / "summary.json", summary)
    elif continue_unstarted:
        name = "summary.json" if index == 0 else f"continuation-{index:04d}-{summary['summary_sha256'][:16]}.json"
        evaluate.write_json(output / name, summary)
    return summary
