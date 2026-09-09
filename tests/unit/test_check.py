from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests.scripts.check import check_catalog, recount
from tests.scripts.build import quick_guide
from tests.scripts.modules import CORE, ROOT, token_count


class AuthoringGateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        body = "# Rule\n\n## Detect\n\nMissing facts.\n\n## Write\n\nKeep supported facts."
        count = token_count(body)
        for name in CORE:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"---\nid: {name}\nlayer: core\nversion: 1.0.0\nstatus: draft\n"
                f"tokens: {count}\nbudget: {count}\nevidence:\n  - tests/sources/test.md\n---\n{body}\n"
            )
        (self.root / "tests/sources").mkdir(parents=True)
        consumers = "".join(f"  - {name}\n" for name in CORE)
        self.source = self.root / "tests/sources/test.md"
        self.source.write_text(
            "---\nid: sources.test\nlayer: sources\nversion: 1.0.0\nstatus: active\nbudget: none\n"
            "evidence_kind: house-inference\nverification_status: partial\nchecked_on: 2026-09-08\n"
            "source_version: fixture\nverification_note: Synthetic test, not a verified authority.\n"
            f"source_urls:\n  - https://example.org/fixture\nconsumers:\n{consumers}---\n# Test source\n"
        )

    def check(self):
        return check_catalog(self.root, generated=False, profiles=False, git=False)

    def test_valid_fixture(self):
        self.assertEqual(self.check(), [])

    def test_stale_count_fails_and_recount_repairs(self):
        path = self.root / CORE[0]
        path.write_text(path.read_text().replace("Keep supported facts.", "Keep all supported facts and dates."))
        self.assertTrue(any("measured" in error for error in self.check()))
        self.assertEqual(recount(self.root), [CORE[0]])
        self.assertEqual(self.check(), [])

    def test_missing_reciprocal_edge_fails(self):
        self.source.write_text(self.source.read_text().replace(f"  - {CORE[0]}\n", ""))
        self.assertTrue(any("reciprocal" in error for error in self.check()))

    def test_missing_source_fails(self):
        self.source.unlink()
        self.assertTrue(any("missing evidence target" in error for error in self.check()))

    def test_missing_provenance_field_fails(self):
        self.source.write_text(self.source.read_text().replace("checked_on: 2026-09-08\n", ""))
        self.assertTrue(any("checked_on" in error for error in self.check()))

    def test_invalid_public_url_fails(self):
        self.source.write_text(self.source.read_text().replace("https://example.org/fixture", "file:///private/source"))
        self.assertTrue(any("public source URL" in error for error in self.check()))

    def test_missing_operating_section_fails(self):
        path = self.root / CORE[0]
        path.write_text(path.read_text().replace("## Write", "## Notes"))
        self.assertTrue(any("missing ## Write" in error for error in self.check()))

    def test_duplicate_ids_fail(self):
        path = self.root / CORE[1]
        path.write_text(path.read_text().replace(f"id: {CORE[1]}", f"id: {CORE[0]}"))
        self.assertTrue(any("duplicate id" in error for error in self.check()))

    def test_ordinary_style_choices_are_not_linted(self):
        path = self.root / CORE[0]
        path.write_text(path.read_text().replace("Keep supported facts.", "Use robust statistics; keep three real options."))
        recount(self.root)
        self.assertEqual(self.check(), [])

    def test_examples_need_real_inline_packets(self):
        path = self.root / CORE[0]
        original = path.read_text()
        example = "\n## Examples\n\n**A case**\n\n> Keep the supported claim.\n"
        path.write_text(original + example)
        self.assertTrue(any("Supplied facts" in error for error in self.check()))
        valid = example.replace("**A case**", "**A case**\n\n**Supplied facts:** The claim is supported.")
        path.write_text(original + valid)
        self.assertEqual(self.check(), [])
        fenced = example.replace(
            "**A case**", "**A case**\n\n```md\n**Supplied facts:** Only a quoted marker.\n```"
        )
        path.write_text(original + fenced)
        self.assertTrue(any("Supplied facts" in error for error in self.check()))

    def test_operating_material_cannot_follow_examples(self):
        path = self.root / CORE[0]
        path.write_text(
            path.read_text()
            + "\n## Examples\n\n**A case**\n\n**Supplied facts:** A supported claim.\n"
            + "\n> Keep it.\n\n## Extra rules\n\nThis rule would be lost from the body.\n"
        )
        self.assertTrue(any("last level-two section" in error for error in self.check()))

    def make_cli_fixture(self):
        (self.root / "domains/user-interface").mkdir(parents=True)
        template = (self.root / CORE[0]).read_text()
        (self.root / "domains/user-interface/test.md").write_text(
            template.replace(f"id: {CORE[0]}", "id: ui.test")
            .replace("layer: core", "layer: user-interface\nkind: medium")
            .replace("evidence:\n  - tests/sources/test.md", "evidence: []")
        )
        (self.root / "stop-the-slop/prompts").mkdir(parents=True)
        (self.root / "stop-the-slop/prompts/task.md").write_text((ROOT / "stop-the-slop/prompts/task.md").read_text())
        (self.root / "domains/profiles").mkdir(parents=True)
        (self.root / "domains/profiles/general.yaml").write_text(
            "name: general\ndescription: Synthetic test profile.\nmodules: []\nsafeguards: []\n"
        )
        (self.root / "quick-guide.md").write_text(quick_guide(self.root))
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)

    def test_cli_returns_nonzero_for_a_planted_defect(self):
        self.make_cli_fixture()
        command = [sys.executable, "-m", "tests.scripts.check", "--root", str(self.root)]
        healthy = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(healthy.returncode, 0, healthy.stderr)
        path = self.root / CORE[0]
        path.write_text(path.read_text().replace("tokens:", "missing_tokens:"))
        result = subprocess.run(
            command,
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(CORE[0], result.stderr)
        self.assertIn("measured", result.stderr)

    def test_invalid_reciprocal_list_is_reported(self):
        text = self.source.read_text()
        beginning = text.split("consumers:\n", 1)[0]
        self.source.write_text(beginning + "consumers: 4\n---\n# Test source\n")
        self.assertTrue(any("list of strings" in error for error in self.check()))

    def test_each_gate_changes_a_healthy_cli_exit(self):
        self.make_cli_fixture()

        def replace(root, name, old, new):
            path = root / name
            path.write_text(path.read_text().replace(old, new))

        def track_working_source(root):
            (root / "raw-data").mkdir()
            (root / "raw-data/fixture.md").write_text("Synthetic test material, not a source book.")
            subprocess.run(
                ["git", "-C", str(root), "add", "raw-data/fixture.md"], check=True
            )

        def add_unregistered_core(root):
            name = "stop-the-slop/new-rule.md"
            template = (root / CORE[0]).read_text()
            (root / name).write_text(template.replace(f"id: {CORE[0]}", f"id: {name}"))
            replace(root, "tests/sources/test.md", "consumers:\n", f"consumers:\n  - {name}\n")

        def add_ungrounded_example(root):
            path = root / CORE[0]
            path.write_text(path.read_text() + "\n## Examples\n\n**Ungrounded example**\n\n> An invented claim.\n")

        def add_rule_after_examples(root):
            path = root / CORE[0]
            path.write_text(
                path.read_text()
                + "\n## Examples\n\n**A case**\n\n**Supplied facts:** A supported claim.\n"
                + "\n> Keep it.\n\n## Hidden rule\n\nThis must not disappear.\n"
            )

        defects = [
            ("metadata", lambda root: replace(root, CORE[0], "version: 1.0.0\n", ""), "version"),
            ("count", lambda root: replace(root, CORE[0], "tokens:", "missing_tokens:"), "measured"),
            ("edge", lambda root: replace(root, "tests/sources/test.md", f"  - {CORE[0]}\n", ""), "reciprocal"),
            ("section", lambda root: replace(root, CORE[0], "## Write", "## Notes"), "missing ## Write"),
            ("id", lambda root: replace(root, CORE[1], f"id: {CORE[1]}", f"id: {CORE[0]}"), "duplicate id"),
            ("date", lambda root: replace(root, "tests/sources/test.md", "2026-09-08", "not-a-date"), "ISO date"),
            ("profile", lambda root: replace(root, "domains/profiles/general.yaml", "modules: []", "modules: [stop-the-slop/accuracy.md]"), "core is automatic"),
            ("path", lambda root: replace(root, "domains/profiles/general.yaml", "modules: []", "modules: [../private.md]"), "not a module"),
            ("generated", lambda root: replace(root, "quick-guide.md", "# Quick guide", "# Unmaintained copy"), "generated content differs"),
            ("core-registry", add_unregistered_core, "unregistered core"),
            ("ui-kind", lambda root: replace(root, "domains/user-interface/test.md", "kind: medium", "kind: extra"), "kind must be"),
            ("ui-standalone", lambda root: replace(root, "domains/user-interface/test.md", "kind: medium", "kind: overlay\nstandalone: 'true'"), "standalone must be a boolean"),
            ("example-packet", add_ungrounded_example, "Supplied facts"),
            ("example-boundary", add_rule_after_examples, "last level-two section"),
            ("working-source", track_working_source, "must not be tracked"),
        ]
        for label, plant, diagnostic in defects:
            with self.subTest(gate=label), tempfile.TemporaryDirectory() as folder:
                root = Path(folder) / "repo"
                shutil.copytree(self.root, root)
                command = [sys.executable, "-m", "tests.scripts.check", "--root", str(root)]
                healthy = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(healthy.returncode, 0, healthy.stderr)
                plant(root)
                broken = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
                self.assertNotEqual(broken.returncode, 0)
                self.assertIn(diagnostic, broken.stderr)


if __name__ == "__main__":
    unittest.main()
