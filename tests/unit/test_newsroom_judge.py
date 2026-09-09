"""Synthetic unit-test packets and fake transports, never benchmark observations."""

import asyncio
from contextlib import redirect_stdout
from copy import deepcopy
import io
from pathlib import Path
import random
import shutil
import unittest
import uuid

from tests.scripts import evaluate, newsroom_judge as judge
from tests.scripts.modules import CORE, DocumentError


def reseal(value, field):
    return evaluate.seal({key: item for key, item in value.items() if key != field}, field)


def rewrite_request(request):
    request["template"]["sha256"] = evaluate.digest(request["template"]["text"])
    request["data_sha256"] = evaluate.digest(evaluate.canonical(request["data"]))
    request["prompt"] = (
        request["template"]["text"] + "\n" + judge.WORD_COUNT_NOTE
        + "\nINPUT DATA:\n" + evaluate.canonical(request["data"])
    )
    request["prompt_sha256"] = evaluate.digest(request["prompt"])
    return reseal(request, "request_sha256")


class FakeTransport:
    """Generate only deterministic, explicitly synthetic assessment fixtures."""

    def __init__(self, raw=None, error=None, mutate=None):
        self.settings = {
            model: {"model_selection": model, "temperature": "synthetic-uncontrolled"}
            for model in ("fixture-judge-one", "fixture-judge-two")
        }
        self.raw, self.error, self.mutate = raw, error, mutate
        self.calls = []
        self.active = self.peak = 0

    async def capture(self, model, prompt):
        self.calls.append((model, prompt))
        self.active += 1
        self.peak = max(self.peak, self.active)
        try:
            await asyncio.sleep(0)
            if self.error is not None:
                raise self.error
            if self.raw is not None:
                response = self.raw
            elif prompt.startswith("SYNTHETIC PREFERENCE TEMPLATE"):
                response = evaluate.canonical({
                    "winner": "tie", "reason": "Synthetic parser fixture, not a real opinion.",
                    "evidence_a": [1], "evidence_b": [1],
                })
            else:
                response = evaluate.canonical({
                    "level": "absent", "reason": "Synthetic parser fixture only.", "evidence": [],
                    "fidelity": "no_flag", "fidelity_reason": "Synthetic test; no real assessment.",
                })
            effective = "SYNTHETIC WRAPPER\n" + prompt
            capture = {
                "requested_prompt_sha256": evaluate.digest(prompt),
                "effective_user_message": effective,
                "effective_user_message_sha256": evaluate.digest(effective),
                "response": response, "response_sha256": evaluate.digest(response),
                "usage": [{"model": model, "availableToolCount": 0, "numToolCalls": 0}],
                "started_at": "2000-01-01T00:00:00+00:00",
                "completed_at": "2000-01-01T00:00:01+00:00",
            }
            if self.mutate is not None:
                self.mutate(capture)
            return capture
        finally:
            self.active -= 1


class NewsroomJudgeTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(f".newsroom-judge-tests-{uuid.uuid4().hex}")
        self.root.mkdir(mode=0o700)
        self.addCleanup(shutil.rmtree, self.root)
        for name in CORE:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"---\nid: fixture.{path.stem}\nversion: '1.0.0'\nlayer: core\n---\n"
                f"# Synthetic {path.stem}\n\n## Write\n\nKeep synthetic facts.\n",
                encoding="utf-8",
            )
        (self.root / "stop-the-slop/prompts").mkdir(parents=True)
        (self.root / "stop-the-slop/prompts/task.md").write_text(
            "# Synthetic fixture contract\n\n## Shared contract\n\nUse the supplied facts.\n\n"
            "## Draft\n\nReturn the draft.\n\n## Edit\n\nReturn the edit.\n\n"
            "## Review\n\nReturn the review.\n\n## Completion\n\nKeep the facts.\n",
            encoding="utf-8",
        )
        for kind, name in judge.TEMPLATES.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(f"SYNTHETIC {kind.upper()} TEMPLATE\r\nNot a real assessment.\r\n".encode())
        self.case = {
            "schema_version": 1, "id": "fixture-case-private-identity", "split": "held_out",
            "operation": "draft",
            "task": "Synthetic unit-test brief only. Soft target: 200 words.",
            "input": "", "source_kind": "synthetic",
            "facts": [{"id": "f1", "text": "Three blue blocks were supplied."}],
            "modules": [], "safeguards": [],
            "checks": {"required_facts": ["f1"], "forbidden_additions": ["HIDDEN-FORBIDDEN"],
                       "preserve": ["HIDDEN-PRESERVE"], "expected_action": "draft"},
        }
        self.text = "SYNTHETIC TEST HEADLINE\r\n\r\nThree blue blocks.\u2028No red blocks.\n \nCommentary stays.\n"
        self.full = self.record("full", self.text)
        self.bare = self.record("bare-task", "Synthetic bare fixture\n\nThree blue blocks remain.\n")
        self.records = {record["result_sha256"]: record for record in (self.full, self.bare)}
        self.preference = judge.preference_request(
            self.root, self.full, self.bare, "fixture-judge-one",
        )
        self.pointwise = judge.pointwise_request(self.root, self.full, "fixture-judge-one")

    def record(self, variant, response, **changes):
        case = deepcopy(changes.pop("case", self.case))
        request = evaluate.prepare(self.root, case, variant)
        return evaluate.record(
            self.root, request, response, changes.get("model", "fixture-writer-model"),
            changes.get("family", "fixture-writer-family"),
            changes.get("settings", {"temperature": "synthetic-writer-default"}),
        )

    def preference_value(self, **changes):
        return {"winner": "a", "reason": " Synthetic fixture reason.\u2028Another clause. ",
                "evidence_a": [3, 1], "evidence_b": [2], **changes}

    def pointwise_value(self, **changes):
        return {"level": "absent", "reason": "Synthetic fixture reason.", "evidence": [],
                "fidelity": "no_flag", "fidelity_reason": "Synthetic fixture only.", **changes}

    def jobs(self):
        result = []
        for model in ("fixture-judge-one", "fixture-judge-two"):
            result.extend([
                {"id": f"preference-{model}",
                 "request": judge.preference_request(self.root, self.full, self.bare, model)},
                {"id": f"pointwise-full-{model}",
                 "request": judge.pointwise_request(self.root, self.full, model)},
                {"id": f"pointwise-bare-{model}",
                 "request": judge.pointwise_request(self.root, self.bare, model)},
            ])
        return result

    def run_jobs(self, jobs=None, transport=None, output=None, **kwargs):
        with redirect_stdout(io.StringIO()):
            return asyncio.run(judge.run_jobs(
                self.root, self.jobs() if jobs is None else jobs, self.records,
                self.root / "run" if output is None else output,
                FakeTransport() if transport is None else transport, **kwargs,
            ))

    def test_paragraph_convention_preserves_every_character(self):
        for text in (self.text, "\n\nA\n\n\nB\n", " A\r\n \r\nB\r\n", "A\u2028B\u2029C", "A\rB"):
            with self.subTest(text=text):
                parts = judge.paragraphs(text)
                self.assertEqual("".join(parts.values()), text)
                self.assertEqual(list(parts), list(range(1, len(parts) + 1)))
        self.assertEqual(judge.paragraphs("A\n\nB"), {1: "A\n\n", 2: "B"})
        self.assertEqual(judge.paragraphs("A\u2028B"), {1: "A\u2028B"})
        for invalid in ("", " \n", None, 1):
            with self.subTest(invalid=invalid), self.assertRaises(DocumentError):
                judge.paragraphs(invalid)

    def test_whitespace_only_edges_are_not_evidence_paragraphs(self):
        text = "\n\nSynthetic headline.\n\nSynthetic body.\n\n \n"
        parts = judge.paragraphs(text)
        self.assertTrue(all(part.strip() for part in parts.values()))
        self.assertEqual("".join(parts.values()), text)
        self.assertEqual(parts, {1: "\n\nSynthetic headline.\n\n", 2: "Synthetic body.\n\n \n"})

    def test_both_orientations_are_bound_to_actual_variants(self):
        reverse = judge.preference_request(self.root, self.bare, self.full, "fixture-judge-one")
        self.assertEqual(self.preference["bindings"]["candidate_side"], "a")
        self.assertEqual(reverse["bindings"]["candidate_side"], "b")
        self.assertEqual(reverse["bindings"]["pair_id"], self.preference["bindings"]["pair_id"])
        for request in (self.preference, reverse):
            self.assertEqual(judge.validate_request(self.root, request, self.records), request)
        self.assertEqual(reverse["data"]["b"]["text"], self.text)

    def test_source_counts_and_no_metadata_or_hidden_check_leakage(self):
        for record in (self.full, self.bare):
            request = judge.pointwise_request(self.root, record, "fixture-judge-one")
            self.assertEqual(set(request["data"]), {"task", "facts", "text", "evidence", "word_count"})
            self.assertEqual(request["data"]["word_count"], len(record["response"].split()))
            self.assertEqual(request["data"]["text"], record["response"])
            judge.validate_request(self.root, request, self.records)
        data = self.preference["data"]
        self.assertEqual(set(data), {"task", "facts", "a", "b"})
        self.assertEqual(data["a"]["word_count"], len(self.text.split()))
        self.assertEqual(data["a"]["evidence"][-1]["text"], "Commentary stays.\n")
        expected_source = {"task": self.case["task"], "facts": self.case["facts"]}
        self.assertEqual(self.preference["bindings"]["source_sha256"],
                         evaluate.digest(evaluate.canonical(expected_source)))
        self.assertIn(judge.WORD_COUNT_NOTE, self.preference["prompt"])
        self.assertIn("soft word target alone is not a factual falsehood", self.preference["prompt"])
        for hidden in ("HIDDEN-PRESERVE", "HIDDEN-FORBIDDEN", "required_facts", "expected_action",
                       "fixture-writer", "fixture-judge", self.case["id"], "result_sha256",
                       '"variant"', '"family"', '"input"', '"checks"'):
            self.assertNotIn(hidden, self.preference["prompt"])
        self.assertEqual(self.preference["template"]["text"],
                         evaluate.read_text(self.root / judge.TEMPLATES["preference"]))
        self.assertIn("\r\n", self.preference["template"]["text"])

    def test_builders_do_not_alias_case_fact_objects(self):
        self.full["request"]["case"]["facts"][0]["text"] = "Changed synthetic fixture."
        self.assertEqual(self.preference["data"]["facts"][0]["text"], "Three blue blocks were supplied.")

    def test_wrong_pairs_operations_variants_and_writer_settings_are_rejected(self):
        other_case = {**deepcopy(self.case), "id": "different-synthetic-case"}
        edit_case = {**deepcopy(self.case), "operation": "edit", "input": "Synthetic edit.",
                     "checks": {**self.case["checks"], "expected_action": "edit"}}
        invalid_seconds = [
            self.full,
            self.record("bare-task", "Synthetic text.", settings={"temperature": "different-setting"}),
            self.record("bare-task", "Synthetic text.", model="different-writer"),
            self.record("bare-task", "Synthetic text.", family="different-family"),
            self.record("bare-task", "Synthetic text.", case=other_case),
            self.record("bare-task", "Synthetic text.", case=edit_case),
            self.record("task-only", "Synthetic text."),
        ]
        for record in invalid_seconds:
            with self.subTest(record=record["result_sha256"]), self.assertRaises(DocumentError):
                judge.preference_request(self.root, self.full, record, "fixture-judge-one")
        for record in invalid_seconds[-2:]:
            with self.assertRaises(DocumentError):
                judge.pointwise_request(self.root, record, "fixture-judge-one")
        for model in ("auto", "default", " ", "fixture judge", None):
            with self.subTest(model=model), self.assertRaises(DocumentError):
                judge.pointwise_request(self.root, self.full, model)

    def test_corrupted_writer_response_hash_and_record_seal_are_rejected(self):
        for mutation in (
            lambda record: record.update(response=record["response"] + "Changed."),
            lambda record: record.update(response_sha256="0" * 64),
        ):
            bad = deepcopy(self.full)
            mutation(bad)
            bad = reseal(bad, "result_sha256")
            with self.assertRaises(DocumentError):
                judge.pointwise_request(self.root, bad, "fixture-judge-one")
        bad = deepcopy(self.full)
        bad["result_sha256"] = "0" * 64
        with self.assertRaises(DocumentError):
            judge.preference_request(self.root, bad, self.bare, "fixture-judge-one")

    def test_resealed_request_tampering_cannot_change_sources_or_orientation(self):
        mutations = (
            lambda r: r["data"].update(writer_model="injected-model-label"),
            lambda r: r["data"]["facts"][0].update(text="Wrong supplied source."),
            lambda r: r["bindings"].update(source_sha256="0" * 64),
            lambda r: r["bindings"].update(candidate_side="b"),
            lambda r: r["bindings"].update(writer_settings_sha256="0" * 64),
            lambda r: r["bindings"]["records"].update(
                a=self.bare["result_sha256"], b=self.full["result_sha256"]),
            lambda r: r["data"]["a"].update(word_count=200),
            lambda r: r["template"].update(text="Altered judge instructions."),
        )
        for mutation in mutations:
            bad = deepcopy(self.preference)
            mutation(bad)
            bad = rewrite_request(bad)
            with self.subTest(mutation=mutation), self.assertRaises(DocumentError):
                judge.validate_request(self.root, bad, self.records)
        bad = deepcopy(self.preference)
        bad["data"]["a"] = {
            "text": "Entirely different synthetic article.", "word_count": 4,
            "evidence": [{"id": 1, "text": "Entirely different synthetic article."}],
        }
        with self.assertRaises(DocumentError):
            judge.validate_request(self.root, rewrite_request(bad), self.records)

    def test_record_map_keys_and_current_template_must_match(self):
        swapped = {self.full["result_sha256"]: self.bare, self.bare["result_sha256"]: self.full}
        with self.assertRaisesRegex(DocumentError, "record-map key"):
            judge.validate_request(self.root, self.preference, swapped)
        with self.assertRaises(DocumentError):
            judge.validate_request(self.root, self.preference, {})
        template = self.root / judge.TEMPLATES["preference"]
        template.write_bytes(template.read_bytes() + b"New synthetic template rule.\n")
        with self.assertRaisesRegex(DocumentError, "current template"):
            judge.validate_request(self.root, self.preference, self.records)

    def test_preference_parser_keeps_original_values_unicode_and_evidence_order(self):
        value = self.preference_value()
        raw = evaluate.canonical(value)
        self.assertIn("\u2028", raw)
        for wrapped in (raw, " \n" + raw + "\r\n", "```json\n" + raw + "\n```"):
            parsed, evidence = judge.parse_assessment(self.preference, wrapped)
            self.assertEqual(parsed, value)
            self.assertEqual([item["id"] for item in evidence["a"]], [3, 1])
            self.assertEqual(evidence["a"][0]["text"], judge.paragraphs(self.text)[3])
            self.assertEqual(evidence["b"][0]["text"], judge.paragraphs(self.bare["response"])[2])

    def test_parser_rejects_duplicate_keys_nonfinite_json_and_fence_repairs(self):
        raw = evaluate.canonical(self.preference_value())
        invalid = (
            "", " \n", "null", "[]", raw.replace('"winner":"a"', '"winner":"a","winner":"b"'),
            raw.replace('"winner":"a"', '"winner":NaN'),
            raw.replace('"winner":"a"', '"winner":1e999'),
            "Preamble\n" + raw, raw + "\nTrailing material", "```\n" + raw + "\n```",
            "```JSON\n" + raw + "\n```", "```json\n```json\n" + raw + "\n```\n```",
        )
        for text in invalid:
            with self.subTest(text=text), self.assertRaises(DocumentError):
                judge.parse_assessment(self.preference, text)

    def test_preference_schema_and_integer_id_failures(self):
        for changes in (
            {"winner": "full"}, {"winner": True}, {"reason": ""}, {"reason": 1},
            {"extra": "not allowed"}, {"evidence_a": []}, {"evidence_b": []},
        ):
            with self.subTest(changes=changes), self.assertRaises(DocumentError):
                judge.parse_assessment(self.preference, evaluate.canonical(self.preference_value(**changes)))
        value = self.preference_value()
        del value["reason"]
        with self.assertRaises(DocumentError):
            judge.parse_assessment(self.preference, evaluate.canonical(value))
        for ids in ([True], ["1"], [1.0], [1, 1], [0], [-1], [999], [{}], None, "1", {}):
            for side in ("a", "b"):
                value = self.preference_value(**{f"evidence_{side}": ids})
                with self.subTest(ids=ids, side=side), self.assertRaises(DocumentError):
                    judge.parse_assessment(self.preference, evaluate.canonical(value))

    def test_pointwise_schema_and_conditional_evidence_rules(self):
        for level in ("absent", "minor", "salient", "unassessable"):
            for fidelity in ("no_flag", "flag", "uncertain"):
                required = level in ("minor", "salient") or fidelity == "flag"
                value = self.pointwise_value(level=level, fidelity=fidelity, evidence=[2, 1] if required else [])
                parsed, evidence = judge.parse_assessment(self.pointwise, evaluate.canonical(value))
                self.assertEqual(parsed, value)
                self.assertEqual([item["id"] for item in evidence], value["evidence"])
                if required:
                    value["evidence"] = []
                    with self.assertRaises(DocumentError):
                        judge.parse_assessment(self.pointwise, evaluate.canonical(value))
        for changes in (
            {"level": "clean"}, {"fidelity": "verified"}, {"reason": " "},
            {"fidelity_reason": ""}, {"fidelity_reason": False}, {"extra": 1},
            {"evidence": [True]}, {"evidence": ["1"]}, {"evidence": [1, 1]}, {"evidence": [999]},
        ):
            with self.subTest(changes=changes), self.assertRaises(DocumentError):
                judge.parse_assessment(self.pointwise, evaluate.canonical(self.pointwise_value(**changes)))
        for key in self.pointwise_value():
            value = self.pointwise_value()
            del value[key]
            with self.subTest(key=key), self.assertRaises(DocumentError):
                judge.parse_assessment(self.pointwise, evaluate.canonical(value))

    def test_whole_plan_validation_happens_before_artifacts_or_capture(self):
        jobs = self.jobs()
        broken = deepcopy(jobs)
        broken[-1]["request"]["prompt"] += "Injected."
        alternatives = [
            [], broken, [{**jobs[0], "extra": 1}], [jobs[0], deepcopy(jobs[0])],
            [{"id": "../escape", "request": self.preference}],
            [{"id": "plan.json", "request": self.preference}],
            [jobs[0], {"id": "duplicate-observation", "request": jobs[0]["request"]}],
            [jobs[0], {"id": "opposite-duplicate",
                       "request": judge.preference_request(self.root, self.bare, self.full, "fixture-judge-one")}],
        ]
        for plan in alternatives:
            transport = FakeTransport()
            with self.subTest(plan=plan), self.assertRaises(DocumentError):
                self.run_jobs(plan, transport)
            self.assertEqual(transport.calls, [])
            self.assertFalse((self.root / "run").exists())
        for kwargs in ({"concurrency": True}, {"concurrency": 0}, {"concurrency": 1.5},
                       {"order_seed": False}, {"resume": 1}, {"continue_unstarted": True},
                       {"continue_unstarted": 1}):
            with self.subTest(kwargs=kwargs), self.assertRaises(DocumentError):
                self.run_jobs(**kwargs)
        transport = FakeTransport()
        transport.settings["fixture-judge-one"]["api_key"] = "synthetic-not-a-credential"
        with self.assertRaisesRegex(DocumentError, "credential"):
            self.run_jobs(transport=transport)
        self.assertFalse((self.root / "run").exists())

    def test_transport_requires_explicit_model_selection(self):
        transport = FakeTransport()
        transport.settings["fixture-judge-one"].pop("model_selection")
        with self.assertRaisesRegex(DocumentError, "model selection"):
            self.run_jobs(transport=transport)
        self.assertEqual(transport.calls, [])
        self.assertFalse((self.root / "run").exists())

    def test_capture_is_exact_seeded_and_resume_does_not_capture_again(self):
        jobs, transport = self.jobs(), FakeTransport()
        result = self.run_jobs(jobs, transport, concurrency=1)
        self.assertEqual(result["status"], "captured")
        self.assertEqual(result["captured_jobs"], 6)
        expected = sorted(jobs, key=lambda job: job["id"])
        random.Random(731).shuffle(expected)
        self.assertEqual(transport.calls, [(job["request"]["model"], job["request"]["prompt"]) for job in expected])
        plan = evaluate.load_json(self.root / "run/plan.json")
        self.assertEqual(plan["launch_order"], [job["id"] for job in expected])
        self.assertEqual(plan["model_settings"], transport.settings)
        for job in jobs:
            target = self.root / "run" / job["id"]
            request = evaluate.load_json(target / "request.json")
            capture = evaluate.load_json(target / "capture.json")
            assessment = evaluate.load_json(target / "assessment.json")
            self.assertEqual(request, job["request"])
            self.assertEqual(capture["requested_prompt_sha256"], request["prompt_sha256"])
            self.assertEqual(capture["response_sha256"], evaluate.digest(capture["response"]))
            self.assertEqual(assessment["capture_sha256"], evaluate.digest(evaluate.canonical(capture)))
            parsed, evidence = judge.parse_assessment(request, capture["response"])
            self.assertEqual(assessment["assessment"], parsed)
            self.assertEqual(assessment["evidence"], evidence)
            self.assertEqual(assessment["assessor"], "model")
            self.assertNotIn("human_attestation", assessment)
            self.assertNotIn("promotion", assessment)
        resumed = self.run_jobs(jobs, transport, concurrency=1, resume=True)
        self.assertEqual(resumed, result)
        self.assertEqual(self.run_jobs(jobs, transport, concurrency=1, resume=True), result)
        self.assertEqual(len(transport.calls), 6)
        with self.assertRaises(DocumentError):
            self.run_jobs(jobs, transport, concurrency=1)
        self.assertEqual(len(transport.calls), 6)

    def test_concurrency_is_bounded(self):
        transport = FakeTransport()
        self.run_jobs(transport=transport, concurrency=2)
        self.assertEqual(transport.peak, 2)
        self.assertEqual(transport.active, 0)

    def test_fenced_capture_preserves_raw_text_and_literal_unicode_separators(self):
        value = self.preference_value(reason="Synthetic reason.\u2028Second part.\u2029Third part.")
        raw = " \r\n```json\n" + evaluate.canonical(value) + "\n```\r\n "
        jobs, transport = self.jobs()[:1], FakeTransport(raw=raw)
        self.run_jobs(jobs, transport)
        target = self.root / "run" / jobs[0]["id"]
        capture = evaluate.load_json(target / "capture.json")
        self.assertEqual(capture["response"], raw)
        self.assertEqual(capture["response_sha256"], evaluate.digest(raw))
        self.assertEqual(evaluate.load_json(target / "assessment.json")["assessment"], value)

    def test_completed_artifacts_are_verified_without_a_final_summary(self):
        jobs, transport = self.jobs()[:1], FakeTransport()
        self.run_jobs(jobs, transport)
        (self.root / "run/summary.json").unlink()
        result = self.run_jobs(jobs, transport, resume=True)
        self.assertEqual(result["status"], "captured")
        self.assertEqual(len(transport.calls), 1)
        (self.root / "run" / jobs[0]["id"] / "assessment.json").unlink()
        result = self.run_jobs(jobs, transport, resume=True)
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(next(iter(result["jobs"].values()))["status"], "blocked")
        self.assertEqual(len(transport.calls), 1)

    def test_malformed_judges_are_preserved_without_transport_circuit_breaking(self):
        for index, raw in enumerate(("not JSON\u2028not a repair", " \r\n", "")):
            transport = FakeTransport(raw=raw)
            output = self.root / f"malformed-{index}"
            summary = self.run_jobs(transport=transport, output=output, concurrency=1)
            self.assertEqual(len(transport.calls), 6)
            self.assertEqual(summary["status"], "incomplete")
            self.assertEqual(summary["captured_jobs"], 0)
            for name in summary["jobs"]:
                target = output / name
                self.assertEqual(evaluate.load_json(target / "capture.json")["response"], raw)
                failure = evaluate.load_json(target / "failure.json")
                self.assertFalse(failure["transport_failure"])
                self.assertEqual(failure["stage"], "assessment")
                self.assertFalse((target / "assessment.json").exists())
            resumed = self.run_jobs(transport=transport, output=output, concurrency=1, resume=True)
            self.assertTrue(all(row["status"] == "blocked" for row in resumed["jobs"].values()))
            self.assertEqual(len(transport.calls), 6)

    def test_transport_circuit_breaker_and_unstarted_jobs_never_retry(self):
        transport = FakeTransport(error=RuntimeError("Synthetic transport failure."))
        result = self.run_jobs(transport=transport, concurrency=1)
        statuses = [row["status"] for row in result["jobs"].values()]
        self.assertEqual(statuses.count("failed"), 3)
        self.assertEqual(statuses.count("not_started"), 3)
        self.assertEqual(len(transport.calls), 3)
        resumed = self.run_jobs(transport=transport, concurrency=1, resume=True)
        self.assertEqual(len(transport.calls), 3)
        self.assertEqual(resumed["status"], "incomplete")
        self.assertEqual(sum(row["status"] == "blocked" for row in resumed["jobs"].values()), 3)

    def test_explicit_continuation_only_captures_never_started_jobs(self):
        transport = FakeTransport(error=RuntimeError("Synthetic temporary outage."))
        initial = self.run_jobs(transport=transport, concurrency=1)
        original = (self.root / "run/summary.json").read_bytes()
        transport.error = None
        continued = self.run_jobs(transport=transport, concurrency=1, resume=True, continue_unstarted=True)
        self.assertEqual(len(transport.calls), 6)
        self.assertEqual(len(set(transport.calls)), 6)
        self.assertEqual(continued["captured_jobs"], 3)
        self.assertEqual(sum(row["status"] == "blocked" for row in continued["jobs"].values()), 3)
        self.assertEqual(continued["continuation_index"], 1)
        self.assertEqual(continued["previous_summary_sha256"], initial["summary_sha256"])
        self.assertEqual((self.root / "run/summary.json").read_bytes(), original)
        self.assertEqual(self.run_jobs(transport=transport, concurrency=1, resume=True), continued)
        again = self.run_jobs(transport=transport, concurrency=1, resume=True, continue_unstarted=True)
        self.assertEqual(len(transport.calls), 6)
        self.assertEqual(again["continuation_index"], 2)
        self.assertEqual(again["previous_summary_sha256"], continued["summary_sha256"])
        self.assertEqual(len(list((self.root / "run").glob("continuation-*.json"))), 2)

    def test_interrupted_continuation_does_not_retry_its_partial_attempt(self):
        transport = FakeTransport(error=RuntimeError("Synthetic temporary outage."))
        self.run_jobs(transport=transport, concurrency=1)
        transport.error = asyncio.CancelledError()
        with self.assertRaises(asyncio.CancelledError):
            self.run_jobs(transport=transport, concurrency=1, resume=True, continue_unstarted=True)
        attempted = len(transport.calls)
        self.assertGreater(attempted, 3)
        transport.error = None
        continued = self.run_jobs(transport=transport, concurrency=1, resume=True, continue_unstarted=True)
        self.assertEqual(len(transport.calls), 6)
        self.assertEqual(len(set(transport.calls)), 6)
        self.assertEqual(continued["captured_jobs"], 6 - attempted)
        self.assertEqual(continued["continuation_index"], 1)

    def test_deleted_attempt_is_not_reclassified_as_never_started(self):
        transport = FakeTransport(error=RuntimeError("Synthetic temporary outage."))
        initial = self.run_jobs(transport=transport, concurrency=1)
        failed = next(name for name, row in initial["jobs"].items() if row["status"] == "failed")
        shutil.rmtree(self.root / "run" / failed)
        transport.error = None
        with self.assertRaisesRegex(DocumentError, "disappeared"):
            self.run_jobs(transport=transport, concurrency=1, resume=True, continue_unstarted=True)
        self.assertEqual(len(transport.calls), 3)

    def test_failed_capture_bytes_are_checked_before_any_continuation(self):
        jobs, transport = self.jobs()[:1], FakeTransport(raw="Synthetic malformed JSON")
        self.run_jobs(jobs, transport)
        path = self.root / "run" / jobs[0]["id"] / "capture.json"
        capture = evaluate.load_json(path)
        capture["response"] += " Changed."
        capture["response_sha256"] = evaluate.digest(capture["response"])
        path.write_text(evaluate.canonical(capture), encoding="utf-8")
        with self.assertRaisesRegex(DocumentError, "failed capture changed"):
            self.run_jobs(jobs, transport, resume=True, continue_unstarted=True)
        self.assertEqual(len(transport.calls), 1)

    def test_summary_counts_and_continuation_links_are_verified(self):
        transport = FakeTransport(error=RuntimeError("Synthetic temporary outage."))
        self.run_jobs(transport=transport, concurrency=1)
        transport.error = None
        self.run_jobs(transport=transport, concurrency=1, resume=True, continue_unstarted=True)
        path = self.root / "run/summary.json"
        summary = evaluate.load_json(path)
        summary["captured_jobs"] = 1
        path.write_text(evaluate.canonical(reseal(summary, "summary_sha256")), encoding="utf-8")
        with self.assertRaisesRegex(DocumentError, "counts"):
            self.run_jobs(transport=transport, concurrency=1, resume=True, continue_unstarted=True)
        self.assertEqual(len(transport.calls), 6)

    def test_registered_transport_exceptions_are_retained_without_catching_everything(self):
        class SyntheticRpcError(Exception):
            pass

        transport = FakeTransport(error=SyntheticRpcError("Synthetic RPC failure."))
        transport.capture_errors = (SyntheticRpcError,)
        result = self.run_jobs(transport=transport, concurrency=1)
        self.assertEqual(len(transport.calls), 3)
        self.assertEqual(sum(row["status"] == "failed" for row in result["jobs"].values()), 3)
        transport = FakeTransport()
        transport.capture_errors = (Exception,)
        with self.assertRaisesRegex(DocumentError, "specific exception classes"):
            self.run_jobs(transport=transport, output=self.root / "invalid-errors")
        self.assertEqual(transport.calls, [])

    def test_resealed_failure_must_match_original_summary(self):
        jobs = self.jobs()[:1]
        transport = FakeTransport(error=RuntimeError("Synthetic transport failure."))
        self.run_jobs(jobs, transport)
        path = self.root / "run" / jobs[0]["id"] / "failure.json"
        failure = evaluate.load_json(path)
        failure["error"] = "Altered synthetic failure."
        path.write_text(evaluate.canonical(reseal(failure, "failure_sha256")), encoding="utf-8")
        with self.assertRaisesRegex(DocumentError, "saved failure"):
            self.run_jobs(jobs, transport, resume=True)
        self.assertEqual(len(transport.calls), 1)

    def test_interrupted_attempt_is_retained_and_never_retried(self):
        jobs = self.jobs()[:1]
        transport = FakeTransport(error=asyncio.CancelledError())
        with self.assertRaises(asyncio.CancelledError):
            self.run_jobs(jobs, transport, concurrency=1)
        target = self.root / "run" / jobs[0]["id"]
        self.assertTrue((target / "request.json").exists())
        self.assertFalse((target / "capture.json").exists())
        self.assertEqual(self.run_jobs(jobs, transport, concurrency=1, resume=True)["status"], "incomplete")
        self.assertEqual(len(transport.calls), 1)

    def test_bad_capture_hashes_usage_and_timestamps_are_retained_as_failures(self):
        mutations = (
            lambda c: c.update(response_sha256="0" * 64),
            lambda c: c.update(requested_prompt_sha256="0" * 64),
            lambda c: c.update(effective_user_message_sha256="0" * 64),
            lambda c: c["usage"][0].update(model="wrong-observed-model"),
            lambda c: c["usage"][0].update(numToolCalls=1),
            lambda c: c["usage"][0].update(availableToolCount=True),
            lambda c: c["usage"][0].update(contentFilterTriggered=True),
            lambda c: c["usage"][0].pop("numToolCalls"),
            lambda c: c["usage"][0].pop("availableToolCount"),
            lambda c: c.update(usage=[]),
            lambda c: c.update(started_at="not a timestamp"),
            lambda c: c.update(unexpected_metadata=True),
        )
        for index, mutation in enumerate(mutations):
            transport = FakeTransport(mutate=mutation)
            output = self.root / f"bad-receipt-{index}"
            result = self.run_jobs(self.jobs()[:1], transport, output=output)
            row = next(iter(result["jobs"].values()))
            self.assertEqual(row["status"], "failed")
            self.assertEqual(row["stage"], "capture_validation")
            target = output / next(iter(result["jobs"]))
            self.assertTrue((target / "capture.json").exists())
            self.assertTrue(evaluate.load_json(target / "failure.json")["transport_failure"])
            self.assertEqual(len(transport.calls), 1)

    def test_request_and_capture_tampering_on_resume_is_rejected(self):
        def changed_raw(capture):
            capture["response"] = capture["response"].replace("parser fixture", "altered fixture")
            capture["response_sha256"] = evaluate.digest(capture["response"])

        mutations = (
            ("request.json", lambda v: v["data"].update(task="Changed synthetic brief.")),
            ("capture.json", lambda v: v.update(response_sha256="0" * 64)),
            ("capture.json", changed_raw),
            ("assessment.json", lambda v: v["assessment"].update(reason="Changed model opinion.")),
        )
        jobs = self.jobs()[:1]
        for index, (filename, mutation) in enumerate(mutations):
            output, transport = self.root / f"tamper-{index}", FakeTransport()
            self.run_jobs(jobs, transport, output)
            path = output / jobs[0]["id"] / filename
            value = evaluate.load_json(path)
            mutation(value)
            path.write_text(evaluate.canonical(value), encoding="utf-8")
            with self.assertRaises(DocumentError):
                self.run_jobs(jobs, transport, output, resume=True)
            self.assertEqual(len(transport.calls), 1)

    def test_resealed_capture_and_assessment_still_must_match_original_summary(self):
        jobs, transport = self.jobs()[:1], FakeTransport()
        self.run_jobs(jobs, transport)
        target = self.root / "run" / jobs[0]["id"]
        capture = evaluate.load_json(target / "capture.json")
        raw = evaluate.parse_json(capture["response"])
        raw["reason"] = "Different synthetic fixture reason."
        capture["response"] = evaluate.canonical(raw)
        capture["response_sha256"] = evaluate.digest(capture["response"])
        (target / "capture.json").write_text(evaluate.canonical(capture), encoding="utf-8")
        plan = evaluate.load_json(self.root / "run/plan.json")
        assessment = judge._assessment(jobs[0], plan, capture)
        (target / "assessment.json").write_text(evaluate.canonical(assessment), encoding="utf-8")
        with self.assertRaisesRegex(DocumentError, "saved summary"):
            self.run_jobs(jobs, transport, resume=True)
        self.assertEqual(len(transport.calls), 1)

    def test_resume_rejects_settings_plan_and_template_changes(self):
        jobs, transport = self.jobs()[:1], FakeTransport()
        self.run_jobs(jobs, transport)
        original = deepcopy(transport.settings)
        transport.settings["fixture-judge-one"]["temperature"] = 1
        with self.assertRaisesRegex(DocumentError, "model settings changed"):
            self.run_jobs(jobs, transport, resume=True)
        transport.settings = original
        for kwargs in ({"order_seed": 3}, {"concurrency": 1}):
            with self.subTest(kwargs=kwargs), self.assertRaises(DocumentError):
                self.run_jobs(jobs, transport, resume=True, **kwargs)
        template = self.root / judge.TEMPLATES["preference"]
        template.write_bytes(template.read_bytes() + b"Changed synthetic source.\n")
        with self.assertRaises(DocumentError):
            self.run_jobs(jobs, transport, resume=True)
        self.assertEqual(len(transport.calls), 1)

    def test_transport_settings_mutation_during_capture_is_detected(self):
        transport = FakeTransport()
        transport.settings["fixture-judge-one"]["temperature"] = 0
        transport.mutate = lambda capture: transport.settings["fixture-judge-one"].update(temperature=False)
        result = self.run_jobs(self.jobs()[:1], transport)
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(next(iter(result["jobs"].values()))["stage"], "capture_validation")
        self.assertTrue((self.root / "run" / self.jobs()[0]["id"] / "capture.json").exists())


if __name__ == "__main__":
    unittest.main()
