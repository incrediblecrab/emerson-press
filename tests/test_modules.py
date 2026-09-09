import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.baseline import capture
from scripts.build import assemble, task_contract
from scripts.modules import (
    CORE, ROOT, DocumentError, Module, digest, local_path, read_yaml,
    section_ranges, token_count,
)


class ParsingTests(unittest.TestCase):
    def test_duplicate_yaml_is_an_error(self):
        with self.assertRaisesRegex(DocumentError, "duplicate key"):
            read_yaml("id: first\nid: second\n", "fixture")

    def test_nested_duplicate_yaml_is_an_error(self):
        with self.assertRaisesRegex(DocumentError, "duplicate key"):
            read_yaml("source:\n  url: one\n  url: two\n", "fixture")

    def test_non_mapping_yaml_is_an_error(self):
        with self.assertRaisesRegex(DocumentError, "mapping"):
            read_yaml("- value", "fixture")

    def test_literal_token_marker_can_be_counted(self):
        self.assertGreater(token_count("The text contains <|endoftext|> as an example."), 0)

    def test_unsafe_yaml_tag_is_an_error(self):
        with self.assertRaises(DocumentError):
            read_yaml("x: !!python/object:example {}", "fixture")

    def test_paths_stay_in_repository(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ("../outside.md", "/outside.md", "core\\voice.md", "core/./voice.md", "", "bad\x00path"):
                with self.subTest(name=name), self.assertRaises(DocumentError):
                    local_path(root, name)

    def test_symlink_cannot_escape(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "repo"
            root.mkdir()
            (root / "outside").symlink_to(Path(folder), target_is_directory=True)
            with self.assertRaisesRegex(DocumentError, "leaves the repository"):
                local_path(root, "outside/file.md")

    def test_symlink_cannot_export_ignored_source_material(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "raw-data").mkdir()
            (root / "raw-data/source.md").write_text("Private source.")
            (root / "core").mkdir()
            (root / "core/alias.md").symlink_to(root / "raw-data/source.md")
            with self.assertRaisesRegex(DocumentError, "private"):
                local_path(root, "core/alias.md")

    def test_private_paths_are_rejected_with_case_variants(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "core").mkdir()
            ordinary = root / "core/ordinary.md"
            ordinary.write_text("Ordinary synthetic module.")
            self.assertEqual(local_path(root, "core/ordinary.md"), ordinary.resolve())
            for name in ("Raw-Data", ".GIT", ".VENV", "NODE_MODULES"):
                with self.subTest(name=name):
                    directory = root / name
                    directory.mkdir()
                    source = directory / "source.md"
                    source.write_text("Synthetic excluded material.")
                    alias = root / "core/alias.md"
                    alias.symlink_to(source)
                    try:
                        with self.assertRaisesRegex(DocumentError, "private"):
                            local_path(root, "core/alias.md")
                    finally:
                        alias.unlink()

    def test_headings_inside_fences_are_not_sections(self):
        text = "# Title\n\n## Write\n\n```md\n## Examples\n```\n\nKeep this.\n\n## Examples\n\nReal examples."
        sections = section_ranges(text)
        self.assertEqual(text[slice(*sections["Write"])].count("Keep this."), 1)
        self.assertEqual(text[slice(*sections["Examples"])], "## Examples\n\nReal examples.")

    def test_unclosed_fence_is_an_error(self):
        with self.assertRaisesRegex(DocumentError, "unclosed"):
            section_ranges("## Write\n```python\nprint(1)\n")

    def test_duplicate_section_is_an_error(self):
        with self.assertRaisesRegex(DocumentError, "duplicate"):
            section_ranges("## Write\nOne.\n## Write\nTwo.\n")

    def test_examples_keep_context_and_ignore_fenced_headings(self):
        content = "# Title\n\n## Write\nKeep facts.\n\n## Examples\n\nSynthetic scenario.\n\n**First case**\n\n```md\n**Not an example**\n```\n\n**Second case**\n\nAnother."
        module = Module("core/example.md", {"layer": "core"}, content, content, section_ranges(content))
        preamble, examples = module.example_sections()
        self.assertIn("Synthetic scenario.", preamble)
        self.assertEqual(list(examples), ["first-case", "second-case"])
        self.assertIn("Not an example", examples["first-case"])
        self.assertIn("Synthetic scenario.", module.render_examples(["second-case"]))
        self.assertNotIn("First case", module.render_examples(["second-case"]))

    def test_empty_module_path_is_rejected(self):
        with self.assertRaises(DocumentError):
            Module.load(ROOT, "")

    def test_source_layer_cannot_be_spoofed(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "sources").mkdir()
            (root / "sources/private.md").write_text(
                "---\nid: fake\nversion: 1.0.0\nlayer: core\n---\n# Private\n## Write\nNo."
            )
            with self.assertRaisesRegex(DocumentError, "layer"):
                Module.load(root, "sources/private.md")

    def test_ui_scope_metadata_is_explicit(self):
        cases = [
            ("kind: medium", None),
            ("kind: overlay\nstandalone: true", None),
            ("kind: overlay\nstandalone: false", None),
            ("", "kind"),
            ("kind: extra", "kind"),
            ("kind: overlay\nstandalone: 'true'", "boolean"),
            ("kind: medium\nstandalone: true", "only overlays"),
        ]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "user-interface").mkdir()
            path = root / "user-interface/test.md"
            for fields, diagnostic in cases:
                with self.subTest(fields=fields):
                    path.write_text(
                        "---\nid: ui.test\nversion: 1.0.0\nlayer: user-interface\n"
                        f"{fields}\n---\n# Test\n\n## Write\n\nUse the right surface.\n"
                    )
                    if diagnostic:
                        with self.assertRaisesRegex(DocumentError, diagnostic):
                            Module.load(root, "user-interface/test.md")
                    else:
                        self.assertEqual(Module.load(root, "user-interface/test.md").title, "Test")


class AssemblyTests(unittest.TestCase):
    def test_assembly_is_deterministic_and_counted(self):
        first, manifest = assemble(ROOT, ["domain/general.md"], operation="edit")
        second, repeated = assemble(ROOT, ["domain/general.md"], operation="edit")
        self.assertEqual(first, second)
        self.assertEqual(manifest, repeated)
        self.assertEqual(manifest["sha256"], digest(first))
        self.assertEqual(manifest["tokens"], token_count(first))
        self.assertNotIn("\nbudget:", first)

    def test_operation_selects_only_its_contract(self):
        text = task_contract(ROOT, "review")
        self.assertIn("## Review", text)
        self.assertNotIn("## Draft", text)
        self.assertNotIn("## Edit", text)

    def test_invalid_operation_fails(self):
        with self.assertRaises(DocumentError):
            assemble(ROOT, [], operation="detect-authorship")

    def test_incompatible_domains_fail(self):
        with self.assertRaisesRegex(DocumentError, "primary genre"):
            assemble(ROOT, ["domain/press.md", "domain/medical.md"], operation="edit")

    def test_incompatible_media_fail(self):
        with self.assertRaisesRegex(DocumentError, "UI medium"):
            assemble(ROOT, ["user-interface/applications.md", "user-interface/website.md"], operation="edit")

    def test_report_chart_does_not_require_a_ui_medium(self):
        text, _ = assemble(ROOT, ["domain/general.md", "user-interface/charts.md"], operation="edit")
        self.assertIn('path="user-interface/charts.md"', text)
        self.assertNotIn('path="user-interface/applications.md"', text)
        self.assertNotIn('path="user-interface/website.md"', text)

    def test_nonstandalone_overlay_requires_a_medium(self):
        with self.assertRaisesRegex(DocumentError, "requires a UI medium"):
            assemble(ROOT, ["user-interface/apple-hig.md"], operation="edit")

    def test_citation_selection_is_exclusive(self):
        with self.assertRaisesRegex(DocumentError, "citation style"):
            assemble(ROOT, ["citation/ama11.md", "citation/apa7.md"], operation="edit")

    def test_source_dossiers_cannot_be_exported(self):
        with self.assertRaisesRegex(DocumentError, "source dossiers"):
            assemble(ROOT, ["sources/ap-stylebook.md"], operation="edit")

    def test_core_is_not_loaded_twice(self):
        with self.assertRaisesRegex(DocumentError, "core is automatic"):
            assemble(ROOT, ["core/voice.md"], operation="edit")

    def test_missing_safeguard_is_not_silently_ignored(self):
        with self.assertRaisesRegex(DocumentError, "unknown safeguard"):
            assemble(ROOT, [], operation="edit", safeguards=["financial"])

    def test_example_must_belong_to_loaded_module(self):
        with self.assertRaisesRegex(DocumentError, "loaded module"):
            assemble(ROOT, [], operation="edit", examples=["domain/medical.md#relative-risk"])

    def test_compact_core_selects_operating_sections(self):
        text, _ = assemble(ROOT, [], operation="edit", variant="compact")
        self.assertNotIn("\n## Detect\n", text)
        self.assertNotIn("\n## Examples\n", text)
        for name in CORE:
            self.assertIn(f'path="{name}"', text)

    def test_frozen_baseline_is_reproducible(self):
        baseline = json.loads((ROOT / "evals/baseline.json").read_text())
        self.assertEqual(capture(ROOT, baseline["revision"]), baseline)

    def test_cli_exports_matching_manifest_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "pack.md"
            manifest_path = Path(folder) / "pack.json"
            command = [
                sys.executable, "-m", "scripts.build", "--module", "domain/general.md",
                "--output", str(output), "--manifest", str(manifest_path),
            ]
            first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            text = output.read_text()
            recorded = manifest_path.read_text()
            manifest = json.loads(recorded)
            self.assertEqual(manifest["sha256"], digest(text))
            self.assertEqual(manifest["tokens"], token_count(text))
            self.assertEqual(manifest["variant"], "full")
            repeated = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(repeated.returncode, 0)
            self.assertIn("refusing to overwrite", repeated.stderr)
            self.assertEqual(output.read_text(), text)
            self.assertEqual(manifest_path.read_text(), recorded)

    def test_cli_cannot_replace_a_dangling_output_symlink(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "unexpected.md"
            output = Path(folder) / "pack.md"
            output.symlink_to(target)
            result = subprocess.run(
                [sys.executable, "-m", "scripts.build", "--module", "domain/general.md",
                 "--output", str(output)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("could not create artifact", result.stderr)
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
