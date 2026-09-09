"""Freeze the original instruction artifacts without copying the source library."""

import argparse
import json
from pathlib import Path
import re
import subprocess

from scripts.modules import CORE, MODULE_DIRS, ROOT, DocumentError, Module, digest, source_text, token_count


def capture(root: Path, revision: str) -> dict:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise DocumentError("revision must be a full, lowercase Git commit ID")
    result = subprocess.run(
        ["git", "-C", str(root), "ls-tree", "-r", "--name-only", revision],
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode:
        raise DocumentError(result.stderr.strip())
    names = [
        name for name in result.stdout.splitlines()
        if name.endswith(".md") and Path(name).parts[0] in MODULE_DIRS
    ]
    if not names:
        raise DocumentError(f"{revision}: no instruction modules found")
    files = {}
    for name in names:
        module = Module.load(root, name, revision)
        files[name] = {
            "sha256": digest(module.text),
            "body_sha256": digest(module.body),
            "full_file_tokens": token_count(module.text),
            "body_tokens": token_count(module.body),
        }
    quick = source_text(root, "quick-guide.md", revision)
    return {
        "schema_version": 1,
        "revision": revision,
        "tokenizer": "o200k_base",
        "core_order": list(CORE),
        "scope": "Original modules and quick guide; no behavioral results",
        "files": files,
        "quick_guide": {"sha256": digest(quick), "tokens": token_count(quick)},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"{args.output}: refusing to replace an existing baseline")
    try:
        report = capture(args.root, args.revision)
    except DocumentError as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Captured {len(report['files'])} modules at {args.revision}")


if __name__ == "__main__":
    main()
