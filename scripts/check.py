"""Check authoring invariants, not prose quality or AI authorship."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit

from scripts.build import assemble, quick_guide
from scripts.modules import (
    CORE, PACK_VARIANTS, ROOT, DocumentError, Module, iso_date, load_profile, module_names,
    required_string, source_text, string_list, token_count, unfenced_lines,
)


EVIDENCE_KINDS = {
    "publisher-guidance", "peer-reviewed-research", "preprint-research",
    "mixed-research", "dataset-analysis", "practitioner", "community",
    "house-inference",
}


def check_catalog(
    root: Path,
    *,
    generated: bool = True,
    profiles: bool = True,
    git: bool = True,
) -> list[str]:
    issues = []
    loaded = {}
    identifiers = {}
    names = module_names(root, include_sources=True)
    if not names:
        return ["No modules found."]
    for name in names:
        try:
            module = Module.load(root, name)
            metadata = module.metadata
            identifier = metadata["id"]
            if identifier in identifiers:
                raise DocumentError(f"{name}: duplicate id also used by {identifiers[identifier]}")
            identifiers[identifier] = name
            loaded[name] = module
            if not re.fullmatch(r"\d+\.\d+\.\d+", metadata["version"]):
                raise DocumentError(f"{name}: version must have major.minor.patch form")
            if metadata.get("status") not in ("draft", "active"):
                raise DocumentError(f"{name}: invalid status")
            module.title
            if metadata["layer"] == "sources":
                string_list(metadata.get("consumers"), f"{name}: consumers")
                if metadata.get("evidence_kind") not in EVIDENCE_KINDS:
                    raise DocumentError(f"{name}: missing or invalid evidence_kind")
                status = metadata.get("verification_status")
                if status not in ("verified", "partial", "historical", "unverified"):
                    raise DocumentError(f"{name}: missing or invalid verification_status")
                iso_date(metadata.get("checked_on"), f"{name}: checked_on")
                required_string(metadata.get("source_version"), f"{name}: source_version")
                required_string(metadata.get("verification_note"), f"{name}: verification_note")
                urls = string_list(metadata.get("source_urls"), f"{name}: source_urls")
                if not urls and status != "unverified":
                    raise DocumentError(f"{name}: a located source URL is required")
                for url in urls:
                    try:
                        parsed = urlsplit(url)
                    except ValueError as error:
                        raise DocumentError(f"{name}: invalid public source URL {url!r}") from error
                    if parsed.scheme not in ("https", "http") or not parsed.netloc or parsed.username or parsed.password or any(char.isspace() for char in url):
                        raise DocumentError(f"{name}: invalid public source URL {url!r}")
            else:
                measured = token_count(module.body)
                for field in ("tokens", "budget"):
                    if type(metadata.get(field)) is not int or metadata[field] != measured:
                        issues.append(f"{name}: {field}={metadata.get(field)!r}, measured {measured}")
                for section in ("Detect", "Write"):
                    module.section(section)
                    if "Examples" in module.sections and module.sections[section][0] > module.sections["Examples"][0]:
                        raise DocumentError(f"{name}: ## {section} must precede ## Examples")
                if "Examples" in module.sections:
                    start = module.sections["Examples"][0]
                    if any(offset > start for offset, _ in module.sections.values()):
                        raise DocumentError(f"{name}: ## Examples must be the last level-two section")
                    _, examples = module.example_sections()
                    for slug, example in examples.items():
                        if not any(
                            re.match(r"^\*\*Supplied facts:\*\*\s+\S", line)
                            for _, line in unfenced_lines(example)
                        ):
                            raise DocumentError(f"{name}#{slug}: missing nonempty inline **Supplied facts:** packet")
                string_list(metadata.get("evidence", []), f"{name}: evidence")
                if metadata["layer"] == "citation":
                    required_string(metadata.get("edition"), f"{name}: edition")
        except DocumentError as error:
            issues.append(str(error))
    for name in CORE:
        if name not in loaded:
            issues.append(f"{name}: missing core module")
    for name in names:
        if name.startswith("core/") and name not in CORE:
            issues.append(f"{name}: unregistered core module; update the CORE registry deliberately")
    for name, module in loaded.items():
        is_source = module.metadata["layer"] == "sources"
        field = "consumers" if is_source else "evidence"
        reciprocal = "evidence" if is_source else "consumers"
        try:
            links = string_list(module.metadata.get(field, []), f"{name}: {field}")
        except DocumentError as error:
            issues.append(str(error))
            continue
        for target in links:
            other = loaded.get(target)
            if other is None:
                issues.append(f"{name}: missing {field} target {target}")
            elif (other.metadata["layer"] == "sources") == is_source:
                issues.append(f"{name}: {field} points to the wrong layer: {target}")
            else:
                try:
                    reverse_links = string_list(other.metadata.get(reciprocal, []), f"{target}: {reciprocal}")
                    if name not in reverse_links:
                        issues.append(f"{name}: {target} is missing reciprocal {reciprocal}")
                except DocumentError as error:
                    issues.append(str(error))
    if profiles:
        paths = sorted((root / "profiles").glob("*.yaml"))
        if not paths:
            issues.append("profiles/: no profiles found")
        for path in paths:
            try:
                profile = load_profile(root, path.stem)
                for variant in PACK_VARIANTS:
                    assemble(root, profile["modules"], operation="edit", variant=variant, safeguards=profile.get("safeguards", []))
            except DocumentError as error:
                issues.append(f"{path.name}: {error}")
    if generated:
        try:
            if source_text(root, "quick-guide.md") != quick_guide(root):
                issues.append("quick-guide.md: generated content differs; run python -m scripts.build --write-quick-guide")
        except DocumentError as error:
            issues.append(str(error))
    if git:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            capture_output=True, text=True,
        )
        if result.returncode:
            issues.append(f"Git inventory unavailable: {result.stderr.strip()}")
        else:
            for name in result.stdout.split("\0"):
                if "raw-data" in Path(name).parts:
                    issues.append(f"{name}: copyrighted/private working material must not be tracked")
    return sorted(set(issues))


def recount(root: Path) -> list[str]:
    changed = []
    for name in module_names(root):
        module = Module.load(root, name)
        measured = token_count(module.body)
        text = module.text
        for field in ("tokens", "budget"):
            pattern = rf"(?m)^{field}: [^\r\n]+$"
            frontmatter_end = text.index("\n---", 4)
            frontmatter = text[:frontmatter_end]
            if len(re.findall(pattern, frontmatter)) != 1:
                raise DocumentError(f"{name}: expected exactly one {field} field")
            text = re.sub(pattern, f"{field}: {measured}", frontmatter) + text[frontmatter_end:]
        if text != module.text:
            (root / name).write_text(text, encoding="utf-8")
            changed.append(name)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--recount", action="store_true", help="update recorded token fields, then run all checks")
    args = parser.parse_args()
    try:
        if args.recount:
            for name in recount(args.root):
                print(f"Recounted {name}")
        issues = check_catalog(args.root)
    except DocumentError as error:
        parser.error(str(error))
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        raise SystemExit(1)
    print("Authoring invariants passed. This is not a writing-quality evaluation.")


if __name__ == "__main__":
    main()
