"""Synthetic transport fixtures; no real model calls or assessment results."""

import asyncio
from contextlib import redirect_stdout
from copy import deepcopy
import io
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest

from scripts import evaluate, generate
from scripts.modules import CORE, DocumentError


class FakeTransport:
    def __init__(self, fail=False, response="Synthetic unit-test response: three blue blocks."):
        self.settings = {"fixture-model": {"temperature": "uncontrolled"}}
        self.calls = 0
        self.fail = fail
        self.response = response

    async def capture(self, model, prompt):
        self.calls += 1
        if self.fail:
            raise RuntimeError("Synthetic transport failure, not a real request.")
        return {"response": self.response}


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

    def test_neutral_role_does_not_remove_runtime_safety_or_policy_sections(self):
        removed = generate.WRITING_SYSTEM["sections"]
        self.assertNotIn("safety", removed)
        self.assertNotIn("runtime_instructions", removed)
        self.assertNotIn("custom_instructions", removed)
        self.assertEqual(generate.WRITING_SYSTEM["mode"], "customize")
        settings = generate.settings_for("fixture-model", "1.0.0", False)
        evaluate.validate_settings(settings)
        self.assertEqual(settings["system_message_config_sha256"],
                         evaluate.digest(evaluate.canonical(generate.WRITING_SYSTEM)))
        self.assertTrue(settings["session_options"]["enable_managed_settings"])

    def test_missing_usage_wrong_model_and_tools_are_explicit_errors(self):
        mutations = [
            lambda events: events.pop(),
            lambda events: events[2]["data"].update(model="other-model"),
            lambda events: events[2]["data"].update(numToolCalls=1),
            lambda events: events[2]["data"].update(availableToolCount=1),
            lambda events: events[2]["data"].pop("numToolCalls"),
            lambda events: events[2]["data"].pop("availableToolCount"),
            lambda events: events[2]["data"].update(numToolCalls=False),
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

    def test_completed_capture_survives_record_validation_failure(self):
        plan, jobs = generate.load_jobs(self.root, self.root / "jobs.json")
        transport = FakeTransport(response=" \n")
        output = self.root / "run"
        with redirect_stdout(io.StringIO()):
            result = asyncio.run(generate.run_jobs(self.root, plan, jobs, output, transport))
            resumed = asyncio.run(generate.run_jobs(self.root, plan, jobs, output, transport, resume=True))
        self.assertEqual(result["jobs"]["fixture-job"]["error_type"], "DocumentError")
        self.assertEqual(resumed["jobs"]["fixture-job"]["status"], "blocked")
        self.assertEqual(transport.calls, 1)
        self.assertTrue((output / "fixture-job/capture.json").exists())
        self.assertEqual(evaluate.load_json(output / "fixture-job/capture.json"), {"response": " \n"})
        self.assertFalse((output / "fixture-job/record.json").exists())

    def test_specific_transport_errors_are_retained_and_broad_registration_rejected(self):
        class SyntheticRpcError(Exception):
            pass

        class RpcTransport(FakeTransport):
            capture_errors = (SyntheticRpcError,)

            async def capture(self, model, prompt):
                self.calls += 1
                raise SyntheticRpcError("Synthetic RPC fixture; no actual model request.")

        plan, jobs = generate.load_jobs(self.root, self.root / "jobs.json")
        transport = RpcTransport()
        with redirect_stdout(io.StringIO()):
            result = asyncio.run(generate.run_jobs(self.root, plan, jobs, self.root / "rpc-run", transport))
        self.assertEqual(result["jobs"]["fixture-job"]["error_type"], "SyntheticRpcError")
        self.assertEqual(transport.calls, 1)
        transport.capture_errors = (Exception,)
        with self.assertRaisesRegex(DocumentError, "specific exception classes"):
            asyncio.run(generate.run_jobs(self.root, plan, jobs, self.root / "broad-run", transport))
        self.assertFalse((self.root / "broad-run").exists())

    def test_observed_sdk_session_error_is_normalized_but_unrelated_errors_propagate(self):
        class Session:
            def __init__(self, error, observed):
                self.error, self.observed = error, observed

            async def __aenter__(self):
                return self

            async def __aexit__(self, kind, value, traceback):
                return None

            def on(self, handler):
                self.handler = handler

            async def send_and_wait(self, prompt, timeout):
                if self.observed:
                    value = {"type": "session.error", "data": {"errorType": "synthetic-runtime-error"}}
                    self.handler(SimpleNamespace(type=SimpleNamespace(value="session.error"), to_dict=lambda: value))
                raise self.error

        class Client:
            def __init__(self, session):
                self.session = session

            async def create_session(self, **kwargs):
                return self.session

        for error, observed, expected in (
            (Exception("Synthetic SDK error"), True, DocumentError),
            (ValueError("Synthetic unrelated error"), False, ValueError),
            (asyncio.CancelledError(), False, asyncio.CancelledError),
        ):
            transport = generate.LiveTransport(self.root, {"fixture-model"})
            transport.settings = {"fixture-model": {"reasoning_effort": "service-default"}}
            transport.client = Client(Session(error, observed))
            with self.subTest(observed=observed, expected=expected), self.assertRaises(expected):
                asyncio.run(transport.capture("fixture-model", "Synthetic prompt; no model call."))


if __name__ == "__main__":
    unittest.main()
