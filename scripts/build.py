"""Assemble portable instructions; full-reference packs remain the default."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.modules import (
    CORE, OPERATIONS, PACK_VARIANTS, ROOT, DocumentError, Module, digest, load_profile,
    section_ranges, source_text, string_list, token_count, validate_selection,
)


def task_contract(root: Path, operation: str | None) -> str:
    text = source_text(root, "prompts/task.md").strip()
    if operation is None:
        return text
    if operation not in OPERATIONS:
        raise DocumentError(f"unknown operation: {operation!r}")
    sections = section_ranges(text)
    names = ("Shared contract", operation.capitalize(), "Completion")
    if any(name not in sections for name in names):
        raise DocumentError("prompts/task.md: missing a required contract section")
    selected = [text[slice(*sections[name])].strip() for name in names]
    return f"# Editorial task: {operation}\n\n" + "\n\n".join(selected)


def assemble(
    root: Path,
    selections: list[str],
    *,
    operation: str,
    variant: str = "full",
    safeguards: list[str] | None = None,
    examples: list[str] | None = None,
) -> tuple[str, dict]:
    if variant not in PACK_VARIANTS:
        raise DocumentError(f"unknown variant: {variant!r}")
    if variant == "focused" and operation not in ("draft", "edit"):
        raise DocumentError("focused is an experimental draft/edit recipe; use full or compact for review")
    string_list(selections, "module selection")
    safeguards = string_list([] if safeguards is None else safeguards, "safeguards")
    examples = string_list([] if examples is None else examples, "examples")
    selected = [Module.load(root, path) for path in selections]
    validate_selection(selected, safeguards)
    rank = {"domain": 0, "citation": 1, "user-interface": 3}
    selected.sort(key=lambda module: (
        2 if module.metadata.get("sublayer") == "education-level" else rank[module.metadata["layer"]],
        module.path,
    ))
    loaded = [*(Module.load(root, path) for path in CORE), *selected]
    by_path = {module.path: module for module in loaded}
    example_map: dict[str, list[str]] = {}
    for selector in examples:
        path, marker, slug = selector.partition("#")
        if not marker or not slug or path not in by_path:
            raise DocumentError(f"{selector}: choose a named example from a loaded module")
        example_map.setdefault(path, []).append(slug)

    contract = task_contract(root, operation)
    blocks = [contract]
    manifest_modules = []
    for module in loaded:
        rendered = module.render(variant)
        if module.path in example_map:
            rendered += "\n\n" + module.render_examples(example_map[module.path])
        blocks.append(f'<module path="{module.path}">\n{rendered}\n</module>')
        manifest_modules.append({
            "path": module.path,
            "id": module.metadata["id"],
            "version": module.metadata["version"],
            "source_sha256": digest(module.text),
            "rendered_sha256": digest(rendered),
        })
    for name in sorted(safeguards):
        module = Module.load(root, f"domain/{name}.md")
        rendered = module.section("Safeguards")
        blocks.append(f'<safeguards kind="{name}">\n{rendered}\n</safeguards>')
        manifest_modules.append({
            "path": module.path,
            "id": module.metadata["id"],
            "version": module.metadata["version"],
            "section": "Safeguards",
            "source_sha256": digest(module.text),
            "rendered_sha256": digest(rendered),
        })
    text = "\n\n".join(blocks).strip() + "\n"
    manifest = {
        "schema_version": 1,
        "operation": operation,
        "variant": variant,
        "evaluation_status": "not_evaluated",
        "contract_sha256": digest(contract),
        "modules": manifest_modules,
        "safeguards": sorted(safeguards),
        "examples": examples,
        "tokenizer": "o200k_base",
        "tokens": token_count(text),
        "sha256": digest(text),
    }
    if variant == "focused":
        manifest["excluded_sections"] = ["Detect"]
    return text, manifest


def quick_guide(root: Path) -> str:
    blocks = [
        "# Quick guide",
        "Use the operation that matches your request. These are writing instructions, not a test of authorship.",
        task_contract(root, None).split("\n", 1)[1].strip(),
    ]
    for path in CORE:
        module = Module.load(root, path)
        write = module.section("Write").split("\n", 1)[1].strip()
        blocks.append(f"## {module.title}\n\n{write}")
    return "\n\n".join(blocks).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--profile")
    selection.add_argument("--module", action="append")
    parser.add_argument("--mode", choices=OPERATIONS, default="edit")
    parser.add_argument("--variant", choices=PACK_VARIANTS, default="full")
    parser.add_argument("--safeguard", action="append", default=[])
    parser.add_argument("--example", action="append", default=[])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--write-quick-guide", action="store_true")
    args = parser.parse_args()
    if args.write_quick_guide and any((
        args.profile, args.module, args.safeguard, args.example, args.output, args.manifest,
        args.variant == "focused",
    )):
        parser.error("--write-quick-guide cannot be combined with pack selections or output paths")
    try:
        if args.write_quick_guide:
            target = args.root / "quick-guide.md"
            target.write_text(quick_guide(args.root), encoding="utf-8")
            print(f"Generated {target}")
            return
        if args.module is None:
            profile = load_profile(args.root, args.profile or "general")
            selections = profile["modules"]
            safeguards = profile.get("safeguards", []) + args.safeguard
        else:
            selections = args.module
            safeguards = args.safeguard
        text, manifest = assemble(
            args.root, selections, operation=args.mode, variant=args.variant,
            safeguards=safeguards, examples=args.example,
        )
    except DocumentError as error:
        parser.error(str(error))
    if args.manifest and not args.output:
        parser.error("--manifest requires --output")
    if args.output and args.manifest and args.output.resolve() == args.manifest.resolve():
        parser.error("output and manifest must be different files")
    for path in (args.output, args.manifest):
        if path and path.exists():
            parser.error(f"{path}: refusing to overwrite an existing artifact")
    if args.output:
        outputs = [(args.output, text)]
        if args.manifest:
            outputs.append((args.manifest, json.dumps(manifest, indent=2) + "\n"))
        for path, content in outputs:
            try:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("x", encoding="utf-8") as output:
                    output.write(content)
            except OSError as error:
                parser.error(f"{path}: could not create artifact: {error}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
