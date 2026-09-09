"""Explicit synthetic unit-test fixtures, never experimental outputs or human ratings."""

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
from fractions import Fraction
import io
import math
from pathlib import Path
import unittest
from unittest.mock import patch
import uuid

from tests.scripts import evaluate as ev
from tests.scripts import simulate
from tests.scripts.build import assemble
from tests.scripts.modules import CORE, DocumentError, module_layer, source_text


class PowerTests(unittest.TestCase):
    def test_bounded_mean_has_the_requested_power_guarantee(self):
        plan = simulate.power_plan()
        self.assertEqual(plan["minimum_families"], 509)
        self.assertTrue(plan["adequate"])
        self.assertGreaterEqual(plan["power_lower_bound"], 0.8)
        self.assertLess(simulate.power_plan(families=508)["power_lower_bound"], 0.8)
        self.assertAlmostEqual(plan["rejection_threshold"], 0.5601967913408573)

    def test_exact_sign_sample_and_discrete_power(self):
        plan = simulate.power_plan("sign_test")
        self.assertEqual(plan["minimum_families"], 199)
        self.assertEqual(plan["critical_wins"], 114)
        self.assertLessEqual(plan["actual_alpha"], 0.025)
        self.assertAlmostEqual(plan["power"], 0.8037139604108053)
        self.assertFalse(simulate.power_plan("sign_test", 198)["adequate"])
        self.assertFalse(simulate.power_plan("sign_test", 200)["adequate"])
        planned = simulate.power_plan("sign_test", 220)
        self.assertEqual(planned["critical_wins"], 126)
        self.assertAlmostEqual(planned["power"], 0.8147148049349376)
        self.assertEqual(planned["power_basis"], "binary_case_benchmark_approximation")
        for families in (0, -1, True):
            with self.subTest(families=families), self.assertRaises(DocumentError):
                simulate.power_plan(families=families)

    def test_pvalues_and_ties_use_family_units(self):
        scores = [Fraction(1)] * 8 + [Fraction(1, 2)] * 20
        sign = simulate.test_result("sign_test", scores)
        self.assertEqual(sign["p_value"], 1 / 256)
        self.assertEqual(sign["decisive_families"], 8)
        self.assertEqual(sign["tied_families"], 20)
        self.assertFalse(sign["effective_design_adequate"])
        bounded = simulate.test_result("bounded_mean", [Fraction(1)] * 8)
        self.assertAlmostEqual(bounded["p_value"], math.exp(-4))
        self.assertEqual(simulate.test_result("bounded_mean", [Fraction(0)])["p_value"], 1)
        self.assertIsNone(simulate.test_result("sign_test", [])["p_value"])

    def test_raw_220_families_are_not_220_non_tied_sign_observations(self):
        scores = [Fraction(1)] * 6 + [Fraction(0)] * 4 + [Fraction(1, 2)] * 210
        result = simulate.test_result("sign_test", scores)
        self.assertEqual(result["raw_families"], 220)
        self.assertEqual(result["decisive_families"], 10)
        self.assertEqual(result["tied_families"], 210)
        self.assertEqual(result["conditional_sign_preference"], 0.6)
        self.assertAlmostEqual(result["tie_half_credit_mean_preference"], 111 / 220)
        self.assertFalse(result["effective_design_adequate"])
        self.assertIsNone(result["power_at_observed_effect"])
        self.assertIn("not at the raw family count", result["power_qualification"])

    def test_repeated_judges_cases_and_models_do_not_create_independent_families(self):
        plan = {"cases": {"test-a": {"family_id": "test-family-one"},
                          "test-b": {"family_id": "test-family-one"},
                          "test-c": {"family_id": "test-family-two"}}}
        rows = [{"slot": ("test-a", "test", "writer", 1, f"judge-{i}"), "score": Fraction(1)}
                for i in range(20)]
        rows += [{"slot": ("test-b", "test", "writer", 1, "judge"), "score": Fraction(0)},
                 {"slot": ("test-c", "test", "writer", 1, "judge"), "score": Fraction(1)}]
        cases, families = simulate.preferences(rows, plan)
        self.assertEqual(len(cases), 3)
        self.assertEqual(len(families), 2)
        self.assertEqual(families, {"test-family-one": Fraction(1, 2), "test-family-two": Fraction(1)})


class SimulationTests(unittest.TestCase):
    def setUp(self):
        self.folder = Path("tests") / f".simulate-test-{uuid.uuid4().hex}"
        self.folder.mkdir()
        self.addCleanup(self.clean_scratch)
        self.root = self.folder / "repository"
        self.revision = "1" * 40
        self.pinned = {}
        for name in [*CORE, "domains/medical.md", "domains/legal.md"]:
            text = (
                f"---\nid: synthetic.{Path(name).stem}\nversion: '1.0.0'\n"
                f"layer: {module_layer(name)}\n---\n# Synthetic unit-test module\n\n"
                "## Detect\n\nA synthetic cue.\n\n## Write\n\nPreserve the toy facts.\n"
            )
            if name.startswith("domains/"):
                text += "\n## Safeguards\n\nSynthetic safeguard only.\n"
            text += "\n## Examples\n\n**Toy example**\n\nA synthetic example only.\n"
            ev.write_new(self.root / name, text)
            self.pinned[name] = text
        task = (
            "# Synthetic unit-test task contract\n\n## Shared contract\n\nKeep the toy evidence.\n\n"
            "## Draft\n\nDraft toy prose.\n\n## Edit\n\nEdit toy prose.\n\n"
            "## Review\n\nReview toy prose.\n\n## Completion\n\nCheck the toy evidence.\n"
        )
        ev.write_new(self.root / "stop-the-slop/prompts/task.md", task)
        self.pinned["stop-the-slop/prompts/task.md"] = task

        def fixture_source(root, name, revision=None):
            self.assertEqual(root, self.root)
            if revision is None:
                return source_text(root, name)
            self.assertEqual(revision, self.revision)
            return self.pinned[name]

        for patcher in (patch("tests.scripts.modules.source_text", side_effect=fixture_source),
                        patch.object(simulate, "source_text", side_effect=fixture_source)):
            patcher.start()
            self.addCleanup(patcher.stop)
        self.serial = 0
        self.pairs = {}

    def clean_scratch(self):
        for path in sorted(self.folder.rglob("*"), key=lambda item: len(item.parts), reverse=True):
            if path.is_symlink() or path.is_file():
                path.unlink()
            else:
                path.rmdir()
        self.folder.rmdir()

    def toy_case(self, index):
        return {
            "schema_version": 1, "id": f"synthetic-test-case-{index}", "split": "held_out",
            "operation": "edit", "task": "Synthetic unit-test task: retain the recorded toy count.",
            "input": f"Synthetic unit-test ledger: {index + 3} toy entries.",
            "source_kind": "synthetic",
            "facts": [{"id": "f1", "text": f"The synthetic toy ledger has {index + 3} entries."}],
            "modules": [], "safeguards": [],
            "checks": {"required_facts": ["f1"], "forbidden_additions": [], "preserve": [],
                       "expected_action": "edit"},
        }

    def make_protocol(self, *, cases=None, family_ids=None, phase="pilot", test="bounded_mean",
                      compact=False, writers=1, judges=1, replicates=1,
                      candidate="full", baseline="task-only", outcome=None, sample_roles=None):
        self.serial += 1
        base = self.folder / f"study-{self.serial}"
        cases = cases or [self.toy_case(0), self.toy_case(1)]
        family_ids = family_ids or [f"synthetic-test-family-{i}" for i in range(len(cases))]
        contrasts = [{"id": "primary", "candidate": candidate, "baseline": baseline, "primary": True}]
        if compact:
            contrasts.append({"id": "exploratory", "candidate": "compact", "baseline": "full", "primary": False})
        variants = sorted({variant for contrast in contrasts
                           for variant in (contrast["candidate"], contrast["baseline"])})
        entries = []
        for index, (case, family) in enumerate(zip(cases, family_ids)):
            requests = {}
            for variant in variants:
                request = ev.prepare(self.root, case, variant)
                path = f"requests/{case['id']}-{variant}.json"
                ev.write_json(base / path, request)
                requests[variant] = {"path": path, "sha256": request["request_sha256"]}
            entries.append({"id": case["id"], "family_id": family, "split": case["split"],
                            "case_sha256": ev.digest(ev.canonical(case)), "requests": requests})
            if sample_roles is not None:
                entries[-1]["sample_role"] = sample_roles[index]
        protocol = ev.seal({
            "schema_version": 1, "kind": "synthetic_protocol", "id": f"synthetic-test-study-{self.serial}",
            "phase": phase, "instruction_revision": self.revision,
            "design": {"test": test, "independent_families": len({
                item["family_id"] for item in entries
                if item["split"] == "held_out" and item.get("sample_role", "primary") == "primary"
            })},
            "contrasts": contrasts, "cases": entries,
            "writers": [{"id": f"writer-{i}", "model": f"synthetic-test-writer-{i}",
                         "family": f"synthetic-writer-family-{i}", "settings": {"temperature": 0}}
                        for i in range(writers)],
            "judges": [{"id": f"judge-{i}", "model": f"synthetic-test-judge-{i}",
                        "family": f"synthetic-judge-family-{i}", "settings": {"temperature": 0}}
                       for i in range(judges)],
            "replicates": replicates, "seed": 731,
            "judge_instructions": "Synthetic unit-test judge instructions, not an actual assessment.",
            **({"primary_outcome": outcome} if outcome is not None else {}),
        }, "protocol_sha256")
        path = base / "protocol.json"
        ev.write_json(path, protocol)
        return protocol, path

    def make_observation(self, protocol, path, *, case_id=None, contrast_id="primary",
                         writer_id="writer-0", judge_id="judge-0", replicate=1,
                         status="assessed", raw=None, fidelity=False, regression=False, winner="candidate"):
        case_id = case_id or protocol["cases"][0]["id"]
        slot = {"case_id": case_id, "contrast_id": contrast_id, "writer_id": writer_id,
                "replicate": replicate, "judge_id": judge_id}
        if status == "writer_failed":
            return simulate.capture_judgment(
                self.root, protocol, base_dir=path.parent, **slot, pair_key=None,
                judge_prompt=None, judge_response=None, status=status,
                error="Synthetic test-only writer failure, not an actual request.",
            )
        key_id = (protocol["protocol_sha256"], case_id, contrast_id, writer_id, replicate)
        if key_id not in self.pairs:
            case = next(case for case in protocol["cases"] if case["id"] == case_id)
            contrast = next(c for c in protocol["contrasts"] if c["id"] == contrast_id)
            writer = next(w for w in protocol["writers"] if w["id"] == writer_id)
            group = f"{case_id}-{contrast_id}-{writer_id}-{replicate}"
            results = []
            for index, variant in enumerate((contrast["candidate"], contrast["baseline"])):
                request = ev.load_json(path.parent / case["requests"][variant]["path"])
                result = ev.record(
                    self.root, request, f"Synthetic unit-test output {index + 1}: preserve the toy ledger.",
                    writer["model"], writer["family"], writer["settings"],
                )
                result_path = path.parent / "records" / group / f"output-{index}.json"
                ev.write_json(result_path, result)
                results.append(result_path)
            directory = path.parent / "pairs" / group
            ev.blind(self.root, *results, directory,
                     simulate.pair_seed(protocol, case_id, contrast_id, writer_id, replicate))
            key, records = ev.read_pair(self.root, directory / "key.json")
            responses = {side: record["response"] for side, record in records.items()}
            candidate = next(side for side, record in records.items()
                             if record["request"]["variant"] == contrast["candidate"])
            prompt = simulate.judge_prompt(protocol, records["a"]["request"]["case"], responses)
            self.pairs[key_id] = (str((directory / "key.json").relative_to(path.parent)),
                                  key, records, responses, candidate, prompt)
        pair_path, _, _, responses, candidate, prompt = self.pairs[key_id]
        assessment = {
            "winner": (candidate if winner == "candidate" else
                       ("b" if candidate == "a" else "a") if winner == "baseline" else winner),
            "rationale": {**responses, "reason": "Synthetic test fixture only; not a real AI or human judgment."},
            "hard_failures": {"a": [], "b": []},
            "important_regressions": {"a": False, "b": False},
        }
        if fidelity:
            assessment["hard_failures"][candidate] = [{
                "category": "changed_meaning", "passage": responses[candidate],
                "requirement": "f1: retain the synthetic ledger count",
                "reason": "A planted test-only fidelity failure.",
            }]
        if regression:
            assessment["important_regressions"][candidate] = True
        if simulate.editorial_case(protocol, case_id):
            assessment["editorial"] = {
                dimension: {
                    side: {"level": "professional" if side == candidate else "generic",
                           "passage": responses[side],
                           "reason": "Synthetic editorial-schema test fixture only, not a real rating."}
                    for side in ("a", "b")
                } for dimension in simulate.EDITORIAL_DIMENSIONS
            }
        if protocol.get("evidence_format") == "line-ranges":
            for side in ("a", "b"):
                assessment["rationale"][side] = [1, 1]
                for flag in assessment["hard_failures"][side]:
                    flag["passage"] = [1, 1]
                for ratings in assessment.get("editorial", {}).values():
                    ratings[side]["passage"] = [1, 1]
        return simulate.capture_judgment(
            self.root, protocol, base_dir=path.parent, **slot, pair_key=pair_path,
            judge_prompt=prompt,
            judge_response=(None if status == "judge_failed" else
                            raw if raw is not None else " \r\n" + ev.canonical(assessment) + "\r\n"),
            status=status, error="Synthetic test-only judge failure." if status == "judge_failed" else None,
        )

    def with_runner_settings(self, protocol, path, content="Synthetic test-only neutral role."):
        protocol = deepcopy(protocol)
        for index, model in enumerate([*protocol["writers"], *protocol["judges"]]):
            system = {"mode": "customize", "content": content,
                      "sections": {"preamble": {"action": "remove"}}}
            model["settings"] = {
                "transport": "synthetic-test-transport", "runtime_version": "test-version",
                "model_selection": model["model"],
                "reasoning_effort": "low" if index == 0 else "service-default",
                "temperature": "service-default-uncontrolled",
                "generation_seed": "service-default-uncontrolled",
                "session_options": {"available_tools": [], "enable_managed_settings": True,
                                    "system_message": system},
                "system_message_config_sha256": ev.digest(ev.canonical(system)),
            }
        protocol.pop("protocol_sha256")
        protocol = ev.seal(protocol, "protocol_sha256")
        path.write_bytes(ev.canonical(protocol).encode("utf-8"))
        return protocol

    def saved_pilot(self, *, line_evidence=False, malformed_pair=None, regressions=False):
        self.serial += 1
        directory = self.folder / f"saved-pilot-{self.serial}"
        case = self.toy_case(0)
        case["split"] = "tuning"
        models = ["synthetic-pilot-model-a", "synthetic-pilot-model-b"]
        for number in (1, 2):
            writer_index = number - 1
            writer, judge = models[writer_index], models[1 - writer_index]
            paths = []
            for index, variant in enumerate(("full", "task-only")):
                request = ev.prepare(self.root, case, variant)
                result = ev.record(
                    self.root, request, f"Synthetic pilot unit-test output {index}.\nToy ledger preserved.\n",
                    writer, f"synthetic-family-{writer_index}", {"temperature": 0},
                )
                path = directory / "writers" / f"pair-{number}" / f"record-{index}.json"
                ev.write_json(path, result)
                paths.append(path)
            pair_dir = directory / f"pair-{number:03d}"
            key = ev.blind(self.root, *paths, pair_dir, 731 + number)
            _, records = ev.read_pair(self.root, pair_dir / "key.json")
            responses = {side: record["response"] for side, record in records.items()}
            packet = {field: case[field] for field in ("task", "operation", "input", "facts", "checks")}
            packet["requested_modules"] = case["modules"]
            packet.update({
                side: [{"line": index, "text": line}
                       for index, line in enumerate(response.splitlines(keepends=True), 1)]
                if line_evidence else response for side, response in responses.items()
            })
            prompt = "Synthetic unit-test pilot judge prompt; not an experiment.\nINPUT DATA:\n" + ev.canonical(packet)
            ev.write_json(pair_dir / "judge-request.json", {
                "pair": number, "pair_id": key["pair_id"], "case_id": case["id"],
                "judge_model": judge, "prompt": prompt, "prompt_sha256": ev.digest(prompt),
            })
            candidate = next(side for side, record in records.items() if record["request"]["variant"] == "full")
            assessment = {
                "winner": candidate,
                "rationale": {
                    "a": [1, 1] if line_evidence else responses["a"],
                    "b": [1, 1] if line_evidence else responses["b"],
                    "reason": "Synthetic test-only rating fixture, not a real model or human assessment.",
                },
                "hard_failures": {"a": [], "b": []},
                "important_regressions": {"a": False, "b": False},
            }
            if regressions:
                assessment["important_regressions"][candidate] = True
            raw = "```json\n" + ev.canonical(assessment) + "\n```"
            if malformed_pair == number:
                raw = "Synthetic intentionally malformed judge output."
            ev.write_json(pair_dir / "judge-capture.json", {
                "assessor": "model", "model": judge, "settings": {"temperature": 0},
                "requested_prompt_sha256": ev.digest(prompt),
                "response": raw, "response_sha256": ev.digest(raw),
                "effective_user_message": prompt, "effective_user_message_sha256": ev.digest(prompt),
                "usage": [{"model": judge, "availableToolCount": 0, "numToolCalls": 0}],
                "started_at": "2026-01-01T00:00:00Z", "completed_at": "2026-01-01T00:00:01Z",
            })
            if malformed_pair == number:
                ev.write_json(pair_dir / "failure.json", {
                    "status": "failed", "error_type": "SyntheticFixtureError", "error": "Synthetic malformed output.",
                })
            else:
                saved = deepcopy(assessment)
                if line_evidence:
                    for side in ("a", "b"):
                        saved["rationale"][side] = responses[side].splitlines(keepends=True)[0]
                ev.write_json(pair_dir / "assessment.json", {
                    "assessor": "model", "pair_id": key["pair_id"], "model": judge,
                    "assessment": saved, "raw_response_sha256": ev.digest(raw),
                    "evidence_source": "model-selected line ranges" if line_evidence else "model-quoted excerpts",
                })
        ev.write_json(directory / "capture-summary.json", {
            "assessor": "model", "planned_pairs": 2, "distinct_tuning_cases": 1, "held_out_cases": 0,
            "captured": 1 if malformed_pair else 2, "invalid": 1 if malformed_pair else 0,
        })
        return directory

    def write_observations(self, path, observations):
        target = path.parent / "observations.jsonl"
        target.write_bytes("".join(ev.canonical(item) + "\n" for item in observations).encode("utf-8"))
        return target

    def summarize(self, path, observations):
        return simulate.report(self.root, path, self.write_observations(path, observations))

    def test_protocol_validates_current_payloads_and_combined_safeguards(self):
        case = self.toy_case(0)
        case["safeguards"] = ["medical", "legal"]
        protocol, path = self.make_protocol(cases=[case], compact=True)
        self.assertEqual(simulate.validate_protocol(self.root, protocol, base_dir=path.parent), protocol)
        reference = protocol["cases"][0]["requests"]["full"]
        request = ev.load_json(path.parent / reference["path"])
        rendered, manifest = assemble(self.root, [], operation="edit", safeguards=case["safeguards"])
        self.assertEqual((request["instructions"], request["manifest"]), (rendered, manifest))
        self.assertGreater(request["prompt_tokens"], request["manifest"]["tokens"])

    def test_declared_bare_and_focused_comparisons_are_not_locked_to_full_task_only(self):
        protocol, path = self.make_protocol(candidate="focused", baseline="bare-task")
        simulate.validate_protocol(self.root, protocol, base_dir=path.parent)
        reference = protocol["cases"][0]["requests"]["bare-task"]
        request = ev.load_json(path.parent / reference["path"])
        self.assertEqual(request["instructions"], "")
        self.assertEqual(request["manifest"]["modules"], [])
        self.assertNotIn("# Editorial task:", request["prompt"])
        observation = self.make_observation(protocol, path)
        report = self.summarize(path, [observation])
        self.assertEqual(report["contrasts"][0]["comparison_scope"], "repository-guidance-versus-bare-task")
        self.assertEqual(report["contrasts"][0]["comparison_kind"], "repository-instruction-comparison")
        contaminated = deepcopy(request)
        reference = protocol["cases"][0]["requests"]["focused"]
        module = ev.load_json(path.parent / reference["path"])["manifest"]["modules"][0]
        contaminated["manifest"]["modules"] = [module]
        contaminated.pop("request_sha256")
        contaminated = ev.seal(contaminated, "request_sha256")
        bare_reference = protocol["cases"][0]["requests"]["bare-task"]
        (path.parent / bare_reference["path"]).write_bytes(ev.canonical(contaminated).encode("utf-8"))
        bare_reference["sha256"] = contaminated["request_sha256"]
        protocol.pop("protocol_sha256")
        contaminated_protocol = ev.seal(protocol, "protocol_sha256")
        with self.assertRaisesRegex(DocumentError, "bare-task manifest"):
            simulate.validate_protocol(self.root, contaminated_protocol, base_dir=path.parent)
        request["instructions"] = "An impermissible repository contract."
        with self.assertRaisesRegex(DocumentError, "no repository"):
            simulate.verify_revision(self.root, request, self.revision, {})
        reversed_protocol, reversed_path = self.make_protocol(candidate="task-only", baseline="full")
        simulate.validate_protocol(self.root, reversed_protocol, base_dir=reversed_path.parent)

    def test_newsroom_primary_sample_and_editorial_dimensions_exclude_regression_votes(self):
        protocol, path = self.make_protocol(
            candidate="full", baseline="bare-task", outcome="newsroom-editorial-preference",
            sample_roles=["primary", "regression"],
        )
        primary = self.make_observation(protocol, path, case_id=protocol["cases"][0]["id"])
        regression = self.make_observation(
            protocol, path, case_id=protocol["cases"][1]["id"], winner="baseline", fidelity=True,
        )
        self.assertIn("editorial", primary["assessment"])
        self.assertNotIn("editorial", regression["assessment"])
        self.assertIn("not primarily factuality or task compliance", primary["judge_prompt"])
        self.assertIn("REGRESSION COVERAGE ONLY", regression["judge_prompt"])
        report = self.summarize(path, [primary, regression])
        contrast = report["contrasts"][0]
        self.assertEqual(report["primary_outcome"], "newsroom-editorial-preference")
        self.assertEqual(report["coverage"]["planned_held_out_families"], 1)
        self.assertEqual(report["coverage"]["planned_regression_cases"], 1)
        self.assertEqual(contrast["wins"], 1)
        self.assertEqual(contrast["losses"], 0)
        self.assertEqual(contrast["case_weighted_preference"], 1)
        self.assertEqual(contrast["regression_coverage"]["assessed_slots"], 1)
        self.assertEqual(contrast["fidelity"]["candidate_flags"], 1)
        self.assertEqual(len(report["editorial_assessments"]), 1)
        self.assertEqual(set(report["editorial_assessments"][0]["dimensions"]), set(simulate.EDITORIAL_DIMENSIONS))

    def test_newsroom_roles_are_explicit_and_broad_regressions_cannot_inflate_power(self):
        protocol, _ = self.make_protocol(outcome="newsroom-editorial-preference")
        with self.assertRaisesRegex(DocumentError, "sample_role"):
            simulate.protocol_shape(protocol)
        protocol, _ = self.make_protocol(
            outcome="newsroom-editorial-preference", sample_roles=["primary", "regression"],
        )
        protocol["design"]["independent_families"] = 2
        protocol.pop("protocol_sha256")
        with self.assertRaisesRegex(DocumentError, "not regression coverage"):
            simulate.protocol_shape(ev.seal(protocol, "protocol_sha256"))

    def test_regression_only_split_overlap_is_flagged_not_promoted_to_primary_families(self):
        cases = [self.toy_case(i) for i in range(3)]
        cases[0]["split"] = "tuning"
        cases[1]["split"] = "tuning"
        protocol, path = self.make_protocol(
            cases=cases, family_ids=["newsroom-tuning", "old-regression", "old-regression"],
            outcome="newsroom-editorial-preference", sample_roles=["primary", "regression", "regression"],
            baseline="bare-task",
        )
        plan = simulate.protocol_shape(protocol)
        self.assertEqual(plan["regression_split_overlaps"], ["old-regression"])
        self.assertEqual(plan["primary_families"], {"newsroom-tuning"})
        self.assertEqual(protocol["design"]["independent_families"], 0)
        report = simulate.report(self.root, path, path.parent / "missing.jsonl")
        self.assertEqual(report["status"], "incomplete")
        self.assertIsNone(report["design"]["power"])
        self.assertEqual(report["coverage"]["regression_split_overlap_families"], ["old-regression"])
        protocol["cases"][1]["sample_role"] = "primary"
        protocol.pop("protocol_sha256")
        with self.assertRaisesRegex(DocumentError, "primary scenario family cannot span"):
            simulate.protocol_shape(ev.seal(protocol, "protocol_sha256"))
    def test_newsroom_line_ratings_require_all_dimensions_and_real_selected_evidence(self):
        protocol, path = self.make_protocol(
            cases=[self.toy_case(0)], baseline="bare-task", outcome="newsroom-editorial-preference",
            sample_roles=["primary"],
        )
        protocol["evidence_format"] = "line-ranges"
        protocol.pop("protocol_sha256")
        protocol = ev.seal(protocol, "protocol_sha256")
        path.write_bytes(ev.canonical(protocol).encode("utf-8"))
        observation = self.make_observation(protocol, path)
        self.assertEqual(observation["assessment"]["editorial"]["lead"]["a"]["passage"], [1, 1])
        report = self.summarize(path, [observation])
        self.assertIsInstance(report["editorial_assessments"][0]["dimensions"]["lead"]["a"]["passage"], str)
        changed = deepcopy(observation["assessment"])
        del changed["editorial"]["ap_mechanics"]
        invalid = self.make_observation(protocol, path, raw=ev.canonical(changed))
        self.assertEqual(invalid["status"], "malformed_judge")
        changed = deepcopy(observation["assessment"])
        del changed["editorial"]
        invalid = self.make_observation(protocol, path, raw=ev.canonical(changed))
        self.assertEqual(invalid["status"], "malformed_judge")
        changed = deepcopy(observation["assessment"])
        changed["editorial"]["ap_mechanics"]["a"] = {
            "level": "not_applicable", "passage": None,
            "reason": "Synthetic test fixture without a relevant mechanics feature.",
        }
        accepted = self.make_observation(protocol, path, raw=ev.canonical(changed))
        self.assertEqual(accepted["status"], "assessed")
        changed = deepcopy(observation["assessment"])
        changed["editorial"]["specificity"]["a"]["passage"] = [1, 999]
        invalid = self.make_observation(protocol, path, raw=ev.canonical(changed))
        self.assertEqual(invalid["status"], "malformed_judge")
    def test_pinned_revision_and_corrupted_request_are_rejected(self):
        path = self.root / CORE[0]
        path.write_bytes(path.read_bytes().replace(b"Preserve the toy facts.", b"Changed synthetic rule."))
        protocol, protocol_path = self.make_protocol()
        with self.assertRaisesRegex(DocumentError, "pinned revision"):
            simulate.validate_protocol(self.root, protocol, base_dir=protocol_path.parent)
        path.write_bytes(self.pinned[CORE[0]].encode("utf-8"))
        protocol, protocol_path = self.make_protocol()
        request_path = protocol_path.parent / protocol["cases"][0]["requests"]["full"]["path"]
        request = ev.load_json(request_path)
        request["prompt_tokens"] += 1
        request_path.write_bytes(ev.canonical(request).encode("utf-8"))
        with self.assertRaisesRegex(DocumentError, "hash mismatch"):
            simulate.validate_protocol(self.root, protocol, base_dir=protocol_path.parent)

    def test_protocol_rejects_renamed_cases_split_leakage_and_model_aliases(self):
        original = self.toy_case(0)
        renamed = {**deepcopy(original), "id": "synthetic-test-renamed"}
        protocol, path = self.make_protocol(cases=[original, renamed])
        with self.assertRaisesRegex(DocumentError, "renamed duplicate"):
            simulate.validate_protocol(self.root, protocol, base_dir=path.parent)
        tuning = self.toy_case(1)
        tuning["split"] = "tuning"
        protocol, _ = self.make_protocol(cases=[original, tuning], family_ids=["shared", "shared"])
        with self.assertRaisesRegex(DocumentError, "cannot span"):
            simulate.protocol_shape(protocol)
        protocol, _ = self.make_protocol(judges=2)
        protocol["judges"][1]["model"] = protocol["judges"][0]["model"]
        protocol.pop("protocol_sha256")
        with self.assertRaisesRegex(DocumentError, "duplicate judge model"):
            simulate.protocol_shape(ev.seal(protocol, "protocol_sha256"))

    def test_compact_primary_and_credential_settings_are_rejected(self):
        protocol, _ = self.make_protocol()
        for change in (
            lambda value: value["contrasts"][0].update(candidate="compact"),
            lambda value: value["judges"][0]["settings"].update(api_key="synthetic-not-a-secret"),
            lambda value: value["design"].update(independent_families=500),
            lambda value: value["judges"][0].update(model=value["writers"][0]["model"]),
            lambda value: value["contrasts"].append({
                "id": "renamed-contrast", "candidate": "task-only", "baseline": "full", "primary": False,
            }),
        ):
            with self.subTest(change=change), self.assertRaises(DocumentError):
                changed = deepcopy(protocol)
                change(changed)
                changed.pop("protocol_sha256")
                simulate.protocol_shape(ev.seal(changed, "protocol_sha256"))

    def test_report_pins_shared_runner_and_exact_model_settings(self):
        protocol, path = self.make_protocol(writers=2, judges=2)
        protocol = self.with_runner_settings(protocol, path)
        plan = simulate.protocol_shape(protocol)
        shared = plan["runner_configuration"]
        self.assertNotIn("model_selection", shared)
        self.assertNotIn("reasoning_effort", shared)
        report = simulate.report(self.root, path, path.parent / "missing.jsonl")
        identity = report["runner_identity"]
        self.assertEqual(identity["shared_settings"], shared)
        self.assertEqual(identity["shared_settings_sha256"], ev.digest(ev.canonical(shared)))
        self.assertEqual(identity["writer_settings_sha256"]["writer-0"],
                         ev.digest(ev.canonical(protocol["writers"][0]["settings"])))
        self.assertNotEqual(identity["writer_settings_sha256"]["writer-0"],
                            identity["writer_settings_sha256"]["writer-1"])

    def test_system_or_transport_changes_cannot_be_pooled_across_models(self):
        protocol, path = self.make_protocol(writers=2, judges=2)
        protocol = self.with_runner_settings(protocol, path)
        for setting in ("runtime_version", "system", "permissions"):
            with self.subTest(setting=setting), self.assertRaisesRegex(DocumentError, "mixed runner"):
                changed = deepcopy(protocol)
                settings = changed["writers"][1]["settings"]
                if setting == "runtime_version":
                    settings["runtime_version"] = "another-test-version"
                elif setting == "system":
                    settings["session_options"]["system_message"]["content"] = "Another synthetic role."
                    settings["system_message_config_sha256"] = ev.digest(
                        ev.canonical(settings["session_options"]["system_message"])
                    )
                else:
                    settings["session_options"]["enable_managed_settings"] = False
                changed.pop("protocol_sha256")
                simulate.protocol_shape(ev.seal(changed, "protocol_sha256"))

    def test_system_configuration_text_and_hash_are_checked(self):
        protocol, path = self.make_protocol()
        protocol = self.with_runner_settings(protocol, path)
        original = protocol["writers"][0]["settings"]
        for change in (
            lambda settings: settings.pop("system_message_config_sha256"),
            lambda settings: settings["session_options"].pop("system_message"),
            lambda settings: settings.update(system_message_config_sha256="0" * 64),
            lambda settings: settings["session_options"]["system_message"].update(content="Changed test role."),
        ):
            with self.subTest(change=change), self.assertRaises(DocumentError):
                settings = deepcopy(original)
                change(settings)
                simulate.runner_configuration(settings)

    def test_old_system_records_cannot_be_relabelled_into_a_new_protocol(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)])
        protocol = self.with_runner_settings(protocol, path, "Synthetic test-only coding-agent role.")
        observation = self.make_observation(protocol, path)
        revised = self.with_runner_settings(protocol, path, "Synthetic test-only neutral text role.")
        relabelled = deepcopy(observation)
        relabelled["protocol_sha256"] = revised["protocol_sha256"]
        relabelled["judge"] = {key: value for key, value in revised["judges"][0].items() if key != "id"}
        relabelled.pop("observation_sha256")
        with self.assertRaisesRegex(DocumentError, "pair writer model/family/settings"):
            simulate.validate_observation(
                self.root, revised, simulate.protocol_shape(revised),
                ev.seal(relabelled, "observation_sha256"), path.parent,
            )

    def test_capture_is_exact_automated_and_cannot_enter_the_human_gate(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)])
        observation = self.make_observation(protocol, path)
        self.assertTrue(observation["judge_response"].startswith(" \r\n"))
        self.assertEqual(observation["judge_response_sha256"], ev.digest(observation["judge_response"]))
        self.assertEqual(observation["assessor"], "model")
        key_id = (protocol["protocol_sha256"], protocol["cases"][0]["id"], "primary", "writer-0", 1)
        records = self.pairs[key_id][2]
        with self.assertRaises(DocumentError):
            ev.validate_judgment(observation, records)
        with self.assertRaises(DocumentError):
            changed = {**observation, "assessor": "human"}
            changed.pop("observation_sha256")
            simulate.validate_observation(self.root, protocol, simulate.protocol_shape(protocol),
                                          ev.seal(changed, "observation_sha256"), path.parent)

    def test_tuning_only_cross_family_protocol_has_no_powered_sample(self):
        cases = [self.toy_case(0)]
        cases[0]["split"] = "tuning"
        protocol, path = self.make_protocol(cases=cases, writers=2, judges=2)
        for index in (0, 1):
            protocol["writers"][index]["family"] = f"synthetic-family-{index}"
            protocol["judges"][index]["family"] = f"synthetic-family-{index}"
        protocol["judge_assignment"] = "opposite-family"
        protocol.pop("protocol_sha256")
        protocol = ev.seal(protocol, "protocol_sha256")
        path.write_bytes(ev.canonical(protocol).encode("utf-8"))
        plan = simulate.protocol_shape(protocol)
        self.assertEqual(len(simulate.planned_slots(protocol, plan)), 2)
        observations = [
            self.make_observation(protocol, path, writer_id="writer-0", judge_id="judge-1"),
            self.make_observation(protocol, path, writer_id="writer-1", judge_id="judge-0"),
        ]
        with self.assertRaisesRegex(DocumentError, "assignment"):
            self.make_observation(protocol, path, writer_id="writer-0", judge_id="judge-0")
        report = self.summarize(path, observations)
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(report["design"]["planned_families"], 0)
        self.assertIsNone(report["design"]["power"])
        self.assertIsNone(report["contrasts"][0]["inference"]["p_value"])
        self.assertEqual(report["contrasts"][0]["case_weighted_preference"], 1)

    def test_modern_regression_flags_and_legacy_assessments_are_distinct(self):
        responses = {"a": "Synthetic test A.", "b": "Synthetic test B."}
        modern = {"winner": "tie", "rationale": {**responses, "reason": "Synthetic test rationale."},
                  "hard_failures": {"a": [], "b": []}, "important_regressions": {"a": True, "b": False}}
        self.assertEqual(simulate.validate_assessment(modern, responses), modern)
        for value in (1, "true", None):
            changed = deepcopy(modern)
            changed["important_regressions"]["a"] = value
            with self.assertRaises(DocumentError):
                simulate.validate_assessment(changed, responses)
        legacy = {"winner": "tie", "rationale": modern["rationale"], "fidelity_failures": {"a": [], "b": []}}
        self.assertEqual(simulate.validate_assessment(legacy, responses), legacy)

    def test_prospective_line_evidence_keeps_raw_ranges_and_resolves_only_selected_text(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)])
        protocol["evidence_format"] = "line-ranges"
        protocol["response_envelope"] = "json-or-fence"
        protocol.pop("protocol_sha256")
        protocol = ev.seal(protocol, "protocol_sha256")
        path.write_bytes(ev.canonical(protocol).encode("utf-8"))
        observation = self.make_observation(protocol, path, fidelity=True)
        self.assertEqual(observation["status"], "assessed")
        self.assertEqual(observation["assessment"]["rationale"]["a"], [1, 1])
        self.assertEqual(ev.parse_json(observation["judge_response"]), observation["assessment"])
        self.assertIn('"line":1', observation["judge_prompt"])
        fenced = "```json\n" + ev.canonical(observation["assessment"]) + "\n```"
        preserved = self.make_observation(protocol, path, raw=fenced)
        self.assertEqual(preserved["status"], "assessed")
        self.assertEqual(preserved["judge_response"], fenced)
        self.assertEqual(preserved["assessment"], observation["assessment"])
        report = self.summarize(path, [observation])
        self.assertEqual(report["method"]["evidence_format"], "line-ranges")
        self.assertIsInstance(report["fidelity_failures"][0]["passage"], str)
        self.assertIn("Synthetic unit-test output", report["fidelity_failures"][0]["passage"])
        malformed = deepcopy(observation["assessment"])
        malformed["rationale"]["a"] = [1, 999]
        invalid = self.make_observation(protocol, path, raw=ev.canonical(malformed))
        self.assertEqual(invalid["status"], "malformed_judge")
        self.assertEqual(invalid["judge_response"], ev.canonical(malformed))
        with self.assertRaises(DocumentError):
            simulate.judge_json(fenced, "json-only")

    def test_saved_pilot_adapter_retains_raw_model_data_and_regressions(self):
        for line_evidence in (False, True):
            with self.subTest(line_evidence=line_evidence):
                directory = self.saved_pilot(line_evidence=line_evidence, regressions=True)
                before = (directory / "pair-001/judge-capture.json").read_bytes()
                report = simulate.pilot_report(self.root, directory, expected_pairs=2)
                self.assertEqual(report["status"], "incomplete")
                self.assertEqual(report["coverage"]["assessed_pairs"], 2, report["exclusions"])
                self.assertEqual(report["coverage"]["distinct_tuning_cases"], 1)
                self.assertIsNone(report["coverage"]["independent_families"])
                self.assertIsNone(report["p_value"])
                self.assertIsNone(report["protocol_sha256"])
                self.assertFalse(report["promotion_eligible"])
                self.assertEqual(len(report["important_regressions"]), 2)
                self.assertEqual(before, (directory / "pair-001/judge-capture.json").read_bytes())
                self.assertEqual(report["evidence"][0]["json_envelope"], "single-json-fence")
                output = directory / "synthetic-test-pilot-report.json"
                with redirect_stdout(io.StringIO()):
                    code = simulate.main(["--root", str(self.root), "pilot-report", str(directory),
                                          "--expected-pairs", "2", "--output", str(output)])
                self.assertEqual(code, 1)
                self.assertEqual(ev.load_json(output)["coverage"]["assessed_pairs"], 2)

    def test_saved_pilot_failures_missing_jobs_and_corruption_are_explicit(self):
        directory = self.saved_pilot(malformed_pair=2)
        report = simulate.pilot_report(self.root, directory, expected_pairs=2)
        self.assertEqual(report["coverage"]["assessed_pairs"], 1)
        self.assertIsNone(report["case_weighted_preference"])
        self.assertEqual(report["valid_subset_case_weighted_preference"], 1)
        self.assertIn("valid subset only", report["preference_scope"])
        self.assertEqual(report["failures"][0]["status"], "malformed_judge")
        self.assertIsNotNone(report["failures"][0]["preserved_failure"])
        report = simulate.pilot_report(self.root, directory, expected_pairs=3)
        self.assertTrue(report["exclusions"])
        saved_path = directory / "pair-001/assessment.json"
        saved = ev.load_json(saved_path)
        saved["assessment"]["winner"] = "tie"
        saved_path.write_bytes(ev.canonical(saved).encode("utf-8"))
        report = simulate.pilot_report(self.root, directory, expected_pairs=2)
        self.assertEqual(report["coverage"]["assessed_pairs"], 0)
        self.assertTrue(any("preserved model response" in item["reason"] for item in report["exclusions"]))

    def test_saved_pilot_never_repairs_invalid_model_line_ranges(self):
        responses = {"a": "Synthetic A.\n", "b": "Synthetic B.\n"}
        raw = ev.canonical({
            "winner": "tie", "rationale": {"a": [1, 50], "b": [1, 1], "reason": "Synthetic test."},
            "hard_failures": {"a": [], "b": []}, "important_regressions": {"a": False, "b": False},
        })
        with self.assertRaisesRegex(DocumentError, "outside"):
            simulate.pilot_assessment(raw, responses, line_evidence=True)

    def test_missing_data_writes_honest_incomplete_report(self):
        protocol, path = self.make_protocol()
        missing = path.parent / "missing-observations.jsonl"
        report = simulate.report(self.root, path, missing)
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(len(report["coverage"]["missing_slots"]), 2)
        self.assertFalse(report["promotion_eligible"])
        self.assertFalse(report["human_verified"])
        self.assertIsNone(report["contrasts"][0]["case_weighted_preference"])
        self.assertIsNone(report["contrasts"][0]["inference"]["p_value"])
        output = path.parent / "synthetic-test-report.json"
        with redirect_stdout(io.StringIO()):
            code = simulate.main(["--root", str(self.root), "report", str(path), str(missing),
                                  "--output", str(output)])
        self.assertEqual(code, 1)
        self.assertEqual(ev.load_json(output)["status"], "incomplete")

    def test_failures_and_malformed_judges_remain_in_coverage(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(i) for i in range(3)])
        observations = [
            self.make_observation(protocol, path, case_id=protocol["cases"][0]["id"], status="writer_failed"),
            self.make_observation(protocol, path, case_id=protocol["cases"][1]["id"], status="judge_failed"),
            self.make_observation(protocol, path, case_id=protocol["cases"][2]["id"], raw="not JSON: test-only"),
        ]
        self.assertEqual(observations[2]["status"], "malformed_judge")
        self.assertEqual(observations[2]["judge_response"], "not JSON: test-only")
        report = self.summarize(path, observations)
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(report["coverage"]["failed_slots"], 3)
        self.assertFalse(report["coverage"]["missing_slots"])
        self.assertEqual({failure["status"] for failure in report["failures"]},
                         {"writer_failed", "judge_failed", "malformed_judge"})
        self.assertIsNone(report["contrasts"][0]["inference"]["p_value"])

    def test_invalid_lines_duplicate_slots_and_pair_judge_duplicates_are_not_counted(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)], replicates=2)
        first = self.make_observation(protocol, path)
        repeated = self.make_observation(protocol, path, replicate=2)
        report = self.summarize(path, [first, repeated])
        self.assertEqual(report["coverage"]["assessed_slots"], 1)
        self.assertIn("duplicate pair/judge", report["exclusions"][0]["reason"])
        report = self.summarize(path, [first, first])
        self.assertIn("duplicate planned", report["exclusions"][0]["reason"])
        observations = self.write_observations(path, [first])
        with observations.open("ab") as output:
            output.write(b'{"bad": NaN}\nnot json\n')
        report = simulate.report(self.root, path, observations)
        self.assertEqual(len(report["exclusions"]), 2)
        self.assertEqual(report["status"], "incomplete")

    def test_unicode_separators_inside_json_strings_are_not_record_boundaries(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)])
        plan = simulate.protocol_shape(protocol)
        original = self.make_observation(protocol, path)
        for separator in ("\u0085", "\u2028", "\u2029"):
            with self.subTest(separator=repr(separator)):
                assessment = deepcopy(original["assessment"])
                assessment["rationale"]["reason"] = (
                    f"Synthetic{separator}unit-test reason, not a real judgment."
                )
                raw = ev.canonical(assessment)
                observation = self.make_observation(protocol, path, raw=raw)
                self.assertEqual(observation["status"], "assessed")
                self.assertEqual(observation["judge_response"], raw)
                simulate.validate_observation(self.root, protocol, plan, observation, path.parent)
                report = self.summarize(path, [observation])
                self.assertEqual(report["coverage"]["assessed_slots"], 1)
                self.assertFalse(report["coverage"]["missing_slots"])
                self.assertFalse(report["exclusions"])
                self.assertTrue(report["contrasts"][0]["primary_sample_complete"])

    def test_order_prompt_hash_and_parsed_assessment_controls(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)])
        observation = self.make_observation(protocol, path)
        plan = simulate.protocol_shape(protocol)
        for change in (
            lambda value: value.update(judge_prompt=value["judge_prompt"] + "changed"),
            lambda value: value.update(judge_response_sha256="0" * 64),
            lambda value: value["assessment"].update(winner="tie"),
        ):
            with self.subTest(change=change), self.assertRaises(DocumentError):
                altered = deepcopy(observation)
                change(altered)
                altered.pop("observation_sha256")
                simulate.validate_observation(self.root, protocol, plan,
                                              ev.seal(altered, "observation_sha256"), path.parent)
        key_path = path.parent / observation["pair_key"]
        key = ev.load_json(key_path)
        key["a"], key["b"] = key["b"], key["a"]
        a, b = key_path.parent / "a.txt", key_path.parent / "b.txt"
        first, second = a.read_bytes(), b.read_bytes()
        a.write_bytes(second)
        b.write_bytes(first)
        key.pop("key_sha256")
        key_path.write_bytes(ev.canonical(ev.seal(key, "key_sha256")).encode("utf-8"))
        with self.assertRaisesRegex(DocumentError, "order control"):
            simulate.validate_observation(self.root, protocol, plan, observation, path.parent)

    def test_fidelity_is_separate_and_pilots_never_support_a_signal(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)], compact=True)
        primary = self.make_observation(protocol, path, fidelity=True)
        exploratory = self.make_observation(protocol, path, contrast_id="exploratory")
        report = self.summarize(path, [primary, exploratory])
        self.assertEqual(report["status"], "incomplete")
        contrast = report["contrasts"][0]
        self.assertEqual(contrast["case_weighted_preference"], 1)
        self.assertEqual(contrast["fidelity"]["candidate_flags"], 1)
        self.assertEqual(len(report["fidelity_failures"]), 1)
        self.assertFalse(report["contrasts"][1]["promotion_eligible"])

    def test_complete_test_only_sign_design_stays_provisional_and_fidelity_can_block_it(self):
        cases = [self.toy_case(i) for i in range(200)]
        protocol, path = self.make_protocol(
            cases=cases, phase="confirmatory", test="sign_test", sample_roles=["primary"] * 199 + ["regression"],
        )
        observations = [self.make_observation(protocol, path, case_id=case["id"]) for case in cases]
        report = self.summarize(path, observations)
        self.assertEqual(report["status"], "synthetic_signal")
        self.assertEqual(len(report["contrasts"][0]["held_out_complete_families"]), 199)
        self.assertFalse(report["promotion_eligible"])
        self.assertFalse(report["human_verified"])
        self.assertIn("Model judgments can be wrong", report["warnings"][0])
        self.assertIn("traceability, not judge correctness", report["warnings"][0])
        self.assertEqual(report["flag_status"], "unadjudicated-model-assertions")
        observations[-1] = self.make_observation(protocol, path, case_id=cases[-1]["id"], fidelity=True)
        regression_blocked = self.summarize(path, observations)
        self.assertEqual(regression_blocked["status"], "inconclusive")
        self.assertEqual(regression_blocked["contrasts"][0]["wins"], 199)
        observations[-1] = self.make_observation(protocol, path, case_id=cases[-1]["id"])
        observations[0] = self.make_observation(protocol, path, case_id=cases[0]["id"], fidelity=True)
        blocked = self.summarize(path, observations)
        self.assertEqual(blocked["status"], "inconclusive")
        self.assertTrue(blocked["contrasts"][0]["stylistic_signal"])
        observations[0] = self.make_observation(protocol, path, case_id=cases[0]["id"], regression=True)
        regressed = self.summarize(path, observations)
        self.assertEqual(regressed["status"], "inconclusive")
        self.assertEqual(regressed["contrasts"][0]["important_regressions"]["candidate_flags"], 1)
        incomplete = self.summarize(path, observations[1:])
        self.assertEqual(incomplete["status"], "incomplete")
        self.assertIsNone(incomplete["contrasts"][0]["inference"]["p_value"])
        self.assertIsNone(incomplete["contrasts"][0]["case_weighted_preference"])
        self.assertIsNone(incomplete["contrasts"][0]["held_out_family_preference"])
        self.assertIsNone(incomplete["contrasts"][0]["cluster_bootstrap_ci95"])
        self.assertEqual(incomplete["contrasts"][0]["valid_subset_case_weighted_preference"], 1)

    def test_sign_signal_follows_family_directions_not_mean_magnitude(self):
        cases = [self.toy_case(i) for i in range(199)]
        protocol, path = self.make_protocol(
            cases=cases, phase="confirmatory", test="sign_test", writers=3,
        )
        for winning_families, winning_votes, losing_votes, status in (
            (130, 2, 0, "synthetic_signal"),
            (70, 3, 1, "inconclusive"),
        ):
            with self.subTest(winning_families=winning_families):
                observations = []
                for index, case in enumerate(cases):
                    candidate_votes = winning_votes if index < winning_families else losing_votes
                    for writer_index, writer in enumerate(protocol["writers"]):
                        observations.append(self.make_observation(
                            protocol, path, case_id=case["id"], writer_id=writer["id"],
                            winner="candidate" if writer_index < candidate_votes else "baseline",
                        ))
                report = self.summarize(path, observations)
                contrast = report["contrasts"][0]
                inference = contrast["inference"]
                self.assertTrue(contrast["complete"])
                self.assertTrue(inference["effective_design_adequate"])
                self.assertEqual(inference["decisive_families"], 199)
                self.assertEqual(inference["conditional_sign_preference"], winning_families / 199)
                self.assertAlmostEqual(
                    inference["p_value"],
                    sum(math.comb(199, k) for k in range(winning_families, 200)) / 2 ** 199,
                )
                mean = (
                    winning_families * winning_votes + (199 - winning_families) * losing_votes
                ) / (199 * 3)
                self.assertAlmostEqual(contrast["held_out_family_preference"], mean)
                self.assertEqual(contrast["stylistic_signal"], status == "synthetic_signal")
                self.assertEqual(report["status"], status)
                self.assertFalse(report["promotion_eligible"])
                self.assertFalse(report["human_verified"])

    def test_validate_cli_and_output_no_overwrite(self):
        protocol, path = self.make_protocol(cases=[self.toy_case(0)])
        with redirect_stdout(io.StringIO()):
            self.assertEqual(simulate.main(["--root", str(self.root), "validate", str(path)]), 0)
        observations = self.write_observations(path, [self.make_observation(protocol, path)])
        output = path.parent / "synthetic-test-report.json"
        args = ["--root", str(self.root), "report", str(path), str(observations), "--output", str(output)]
        with redirect_stdout(io.StringIO()):
            self.assertEqual(simulate.main(args), 1)
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(simulate.main(args), 2)


if __name__ == "__main__":
    unittest.main()
