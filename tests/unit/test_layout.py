"""Layout regressions and immutable historical-evidence compatibility."""

import lzma
from pathlib import Path
import subprocess
import unittest

from tests.scripts import baseline, build, evaluate, newsroom_judge, simulate
from tests.scripts.modules import (
    CORE, ROOT, DocumentError, canonical_path, local_path, module_names, source_text,
)


def archive_rows(name):
    raw = (ROOT / f"tests/evals/newsroom/artifacts/{name}.jsonl.xz").read_bytes()
    return [evaluate.parse_json(line) for line in lzma.decompress(raw).decode("utf-8").split("\n") if line]


class RepositoryLayoutTests(unittest.TestCase):
    def test_tracked_root_is_consolidated_and_workflows_are_removed(self):
        result = subprocess.run(
            ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True,
        )
        roots = {
            Path(name).parts[0] for name in result.stdout.decode().split("\0")
            if name and not name.startswith(".") and (ROOT / name).is_file()
        }
        self.assertEqual(roots, {"stop-the-slop", "domains", "tests", "readme.md", "quick-guide.md"})
        self.assertFalse((ROOT / ".github/workflows").exists())

    def test_module_catalog_excludes_contract_profiles_and_evidence(self):
        names = module_names(ROOT)
        self.assertEqual(len(names), 32)
        self.assertTrue(set(CORE) <= set(names))
        self.assertNotIn("stop-the-slop/prompts/task.md", names)
        self.assertTrue(all(not name.startswith("tests/") for name in names))
        self.assertTrue(any(name.startswith("tests/sources/") for name in module_names(ROOT, include_sources=True)))

    def test_old_locations_resolve_but_duplicate_aliases_are_rejected(self):
        for old, current in (
            ("core/accuracy.md", "stop-the-slop/accuracy.md"),
            ("domain/press.md", "domains/press.md"),
            ("citation/apa7.md", "domains/citation/apa7.md"),
            ("user-interface/website.md", "domains/user-interface/website.md"),
            ("sources/ap-stylebook.md", "tests/sources/ap-stylebook.md"),
            ("evals/baseline.json", "tests/evals/baseline.json"),
            ("tests/test_generate.py", "tests/unit/test_generate.py"),
            ("README.md", "readme.md"),
        ):
            with self.subTest(old=old):
                self.assertEqual(canonical_path(old), current)
                self.assertEqual(local_path(ROOT, old), (ROOT / current).resolve())
        with self.assertRaisesRegex(DocumentError, "duplicate"):
            build.assemble(ROOT, ["domain/press.md", "domains/press.md"], operation="draft")

    def test_current_packs_normalize_legacy_example_selectors(self):
        current = "stop-the-slop/accuracy.md#causation-from-correlation"
        original = "core/accuracy.md#causation-from-correlation"
        self.assertEqual(
            build.assemble(ROOT, ["domain/press.md"], operation="draft", examples=[original]),
            build.assemble(ROOT, ["domains/press.md"], operation="draft", examples=[current]),
        )
        with self.assertRaisesRegex(DocumentError, "duplicate"):
            build.assemble(ROOT, [], operation="draft", examples=[original, current])

    def test_current_paths_can_read_exact_git_pinned_original_sources(self):
        revision = "d9b53a99517a50ac90b9c88f9f033c197671d942"
        for original in ("core/accuracy.md", "domain/medical.md", "citation/apa7.md", "prompts/task.md"):
            with self.subTest(original=original):
                self.assertEqual(
                    source_text(ROOT, canonical_path(original), revision),
                    source_text(ROOT, original, revision),
                )

    def test_git_pinned_original_baseline_is_unchanged(self):
        frozen = evaluate.load_json(ROOT / "tests/evals/baseline.json")
        self.assertEqual(baseline.capture(ROOT, frozen["revision"]), frozen)

    def test_original_requests_and_judgments_validate_without_resealing(self):
        rows = archive_rows("primary-writing")
        records = {row["record"]["result_sha256"]: row["record"] for row in rows}
        protocol = evaluate.load_json(ROOT / "tests/evals/newsroom/primary-protocol.json")
        revision = protocol["design"]["allocation"]["source_revision"]
        cache = {}
        for row in rows[:2]:
            record = row["record"]
            before = evaluate.canonical(record)
            evaluate.validate_result(ROOT, record)
            simulate.verify_revision(ROOT, record["request"], revision, cache)
            self.assertEqual(evaluate.canonical(record), before)
        pair = archive_rows("primary-preference")[0]
        request = evaluate.parse_json(pair["files"]["request.json"]["source_text"])
        before = evaluate.canonical(request)
        newsroom_judge.validate_request(ROOT, request, records)
        self.assertEqual(evaluate.canonical(request), before)
        capture = evaluate.parse_json(pair["files"]["capture.json"]["source_text"])
        value, evidence = newsroom_judge.parse_assessment(request, capture["response"])
        stored = evaluate.parse_json(pair["files"]["assessment.json"]["source_text"])
        self.assertEqual(value, stored["assessment"])
        self.assertEqual(evidence, stored["evidence"])


if __name__ == "__main__":
    unittest.main()
