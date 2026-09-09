"""Synthetic transport fixtures; no real model calls or assessment results."""

import asyncio
from contextlib import redirect_stdout
from copy import deepcopy
import io
from pathlib import Path
import tempfile
import unittest

from scripts import evaluate, generate
from scripts.modules import CORE, DocumentError


class FakeTransport:
    def __init__(self, fail=False):
        self.settings = {"fixture-model": {"temperature": "uncontrolled"}}
        self.calls = 0
        self.fail = fail

    async def capture(self, model, prompt):
        self.calls += 1
        if self.fail:
            raise RuntimeError("Synthetic transport failure, not a real request.")
        return {"response": "Synthetic unit-test response: three blue blocks."}


class GenerationTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        for name in CORE:
            path = self.root / name
            path.parent.mkdir(exist_ok=True)
            path.write_text(
                f"---\nid: fixture.{path.stem}\nversion: '1.0.0'\nlayer: core\n---\n"
                f"# {path.stem}\n\n## Write\n\nPreserve synthetic facts.\n",
            )
        (self.root / "prompts").mkdir()
        (self.root / "prompts/task.md").write_text(
            "# Fixture contract\n\n## Shared contract\n\nKeep facts.\n\n"
            "## Edit\n\nEdit the fixture.\n\n## Completion\n\nReturn the text.\n",
        )
        self.case = {
            "schema_version": 1, "id": "fixture-blocks", "split": "tuning",
            "operation": "edit", "task": "Keep the synthetic count and color.",
            "input": "There are three blue blocks.", "source_kind": "synthetic",
            "facts": [{"id": "f1", "text": "The count is three."},
                      {"id": "f2", "text": "The blocks are blue."}],
            "modules": [], "safeguards": [],
            "checks": {"required_facts": ["f1", "f2"], "forbidden_additions": [],
                       "preserve": ["Count and color."], "expected_action": "no_change"},
        }
        self.request = evaluate.prepare(self.root, self.case, "full")
        evaluate.write_json(self.root / "request.json", self.request)
        self.plan = {"schema_version": 1, "jobs": [
            {"id": "fixture-job", "request": "request.json",
             "model": "fixture-model", "family": "fixture-family"},
        ]}
        evaluate.write_json(self.root / "jobs.json", self.plan)

    def events(self):
        return [
            {"type": "user.message", "data": {"content": "Fixture prompt", "transformedContent": "Dated fixture prompt"}},
            {"type": "assistant.message", "data": {"content": "  Fixture output.\r\n"}},
            {"type": "assistant.usage", "data": {
                "model": "fixture-model", "numToolCalls": 0, "availableToolCount": 0,
                "inputTokens": 100, "outputTokens": 5,
                "quotaSnapshots": {"account-private": "must not be published"},
                "copilotUsage": {"totalNanoAiu": 10},
            }},
        ]

    def test_receipt_preserves_text_and_excludes_account_metadata(self):
        receipt = generate.evidence_from_events(self.events(), "Fixture prompt", "fixture-model")
        self.assertEqual(receipt["response"], "  Fixture output.\r\n")
        self.assertEqual(receipt["effective_user_message"], "Dated fixture prompt")
        self.assertNotIn("quotaSnapshots", evaluate.canonical(receipt))
        self.assertNotIn("account-private", evaluate.canonical(receipt))
        self.assertEqual(receipt["usage"][0]["nano_ai_credits"], 10)

    def test_missing_usage_wrong_model_and_tools_are_explicit_errors(self):
        mutations = [
            lambda events: events.pop(),
            lambda events: events[2]["data"].update(model="other-model"),
            lambda events: events[2]["data"].update(numToolCalls=1),
            lambda events: events[2]["data"].update(availableToolCount=1),
            lambda events: events[2]["data"].update(contentFilterTriggered=True),
            lambda events: events[1]["data"].update(toolRequests=[{"name": "fixture-tool"}]),
            lambda events: events.append({"type": "tool.execution_start", "data": {}}),
            lambda events: events[0]["data"].update(content="Different fixture prompt"),
            lambda events: events.append(deepcopy(events[1])),
        ]
        for mutation in mutations:
            events = self.events()
            mutation(events)
            with self.subTest(mutation=mutation), self.assertRaises(DocumentError):
                generate.evidence_from_events(events, "Fixture prompt", "fixture-model")

    def test_job_schema_and_duplicate_or_automatic_model_selection(self):
        _, jobs = generate.load_jobs(self.root, self.root / "jobs.json")
        self.assertEqual(jobs[0]["request_value"], self.request)
        for mutate in (
            lambda plan: plan["jobs"].append(deepcopy(plan["jobs"][0])),
            lambda plan: plan["jobs"][0].update(id="../outside"),
            lambda plan: plan["jobs"][0].update(model="auto"),
            lambda plan: plan["jobs"][0].update(extra=True),
        ):
            plan = deepcopy(self.plan)
            mutate(plan)
            (self.root / "jobs.json").write_text(evaluate.canonical(plan))
            with self.subTest(mutate=mutate), self.assertRaises(DocumentError):
                generate.load_jobs(self.root, self.root / "jobs.json")

    def test_capture_and_verified_resume_do_not_regenerate(self):
        plan, jobs = generate.load_jobs(self.root, self.root / "jobs.json")
        transport = FakeTransport()
        output = self.root / "run"
        with redirect_stdout(io.StringIO()):
            result = asyncio.run(generate.run_jobs(self.root, plan, jobs, output, transport))
            resumed = asyncio.run(generate.run_jobs(
                self.root, plan, jobs, output, transport, resume=True,
            ))
        self.assertEqual(result["status"], "captured")
        self.assertEqual(resumed["captured_jobs"], 1)
        self.assertEqual(transport.calls, 1)
        record = evaluate.load_json(output / "fixture-job/record.json")
        evaluate.validate_result(self.root, record)
        self.assertEqual(record["status"], "captured-unreviewed")
        transport.settings["fixture-model"]["temperature"] = 1
        with self.assertRaisesRegex(DocumentError, "settings changed"):
            asyncio.run(generate.run_jobs(self.root, plan, jobs, output, transport, resume=True))

    def test_failures_are_retained_and_not_silently_retried(self):
        plan, jobs = generate.load_jobs(self.root, self.root / "jobs.json")
        transport = FakeTransport(fail=True)
        output = self.root / "run"
        with redirect_stdout(io.StringIO()):
            result = asyncio.run(generate.run_jobs(self.root, plan, jobs, output, transport))
            resumed = asyncio.run(generate.run_jobs(
                self.root, plan, jobs, output, transport, resume=True,
            ))
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["captured_jobs"], 0)
        self.assertEqual(resumed["jobs"]["fixture-job"]["status"], "blocked")
        self.assertEqual(transport.calls, 1)
        self.assertTrue((output / "fixture-job/failure.json").exists())
        self.assertFalse((output / "fixture-job/record.json").exists())


if __name__ == "__main__":
    unittest.main()
