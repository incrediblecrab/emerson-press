"""Capture real, isolated Copilot responses; never grade writing or invent results."""

from __future__ import annotations

import argparse
import asyncio
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import random
import re
import shutil
import subprocess
import sys
from typing import Any

from scripts import evaluate
from scripts.modules import ROOT, DocumentError, digest


SDK_VERSION = "1.0.13"
WRITING_SYSTEM = {
    "mode": "customize",
    "sections": {
        name: {"action": "remove"}
        for name in (
            "preamble", "tone", "tool_efficiency", "code_change_rules", "guidelines",
            "tool_instructions", "last_instructions",
        )
    },
    "content": (
        "You are a text-only writing assistant. Carry out the supplied drafting, editing, "
        "or reviewing task. Tools, browsing, persistent memory and other agents are "
        "unavailable. Do not narrate or invent calls to them. Return the requested output."
    ),
}
USAGE_FIELDS = (
    "model", "inputTokens", "outputTokens", "cacheReadTokens", "cacheWriteTokens",
    "reasoningTokens", "duration", "finishReason", "contentFilterTriggered",
    "availableToolCount", "numToolCalls", "maxOutputTokens", "maxPromptTokens",
)
SESSION_OPTIONS = {
    "available_tools": [],
    "excluded_tools": ["builtin:*", "mcp:*", "custom:*"],
    "skip_custom_instructions": True,
    "enable_config_discovery": False,
    "enable_session_store": False,
    "enable_skills": False,
    "enable_file_hooks": False,
    "enable_host_git_operations": False,
    "enable_managed_settings": True,
    "memory": {"enabled": False},
    "infinite_sessions": {"enabled": False},
    "system_message": WRITING_SYSTEM,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def runtime_version(executable: str) -> str:
    result = subprocess.run(
        [executable, "--no-auto-update", "--version"], capture_output=True, text=True, check=True,
    )
    match = re.search(r"\b\d+\.\d+\.\d+(?:-\d+)?\b", result.stdout)
    evaluate.require(match is not None, "cannot establish the Copilot runtime version")
    return match.group(0)


def settings_for(model: str, runtime: str, low_reasoning: bool) -> dict:
    return {
        "transport": "github-copilot-sdk",
        "sdk_version": SDK_VERSION,
        "runtime_version": runtime,
        "client_mode": "empty",
        "model_selection": model,
        "session_options": SESSION_OPTIONS,
        "reasoning_effort": "low" if low_reasoning else "service-default",
        "temperature": "service-default-uncontrolled",
        "generation_seed": "service-default-uncontrolled",
        "system_prompt": "neutral writing role; runtime safety and policy sections retained",
        "system_message_config_sha256": digest(evaluate.canonical(WRITING_SYSTEM)),
        "user_message_wrapper": "runtime current_datetime; effective message captured separately",
    }


def evidence_from_events(events: list[dict], prompt: str, model: str) -> dict:
    users, messages, usage = [], [], []
    for event in events:
        kind, data = event["type"], event["data"]
        evaluate.require(
            not kind.startswith(("tool.", "permission.")),
            "tool or permission event occurred in a writing-only session",
        )
        evaluate.require(kind != "session.error", f"runtime reported a session error: {data.get('errorType', 'unknown')}")
        if kind == "user.message":
            users.append({
                "content": data.get("content"),
                "effective_content": data.get("transformedContent", data.get("content")),
            })
        elif kind == "assistant.message":
            evaluate.require(not data.get("toolRequests"), "assistant requested a tool")
            if data.get("content"):
                messages.append(data["content"])
        elif kind == "assistant.usage":
            evaluate.require(data.get("model") == model, "observed model differs from requested model")
            for field in ("numToolCalls", "availableToolCount"):
                evaluate.require(type(data.get(field)) is int and data[field] == 0,
                                 f"runtime must explicitly report zero {field}")
            evaluate.require(not data.get("contentFilterTriggered", False), "provider reported a content filter")
            item = {key: data[key] for key in USAGE_FIELDS if key in data}
            observed_cost = data.get("copilotUsage", {})
            if "totalNanoAiu" in observed_cost:
                item["nano_ai_credits"] = observed_cost["totalNanoAiu"]
            usage.append(item)
    evaluate.require(len(users) == 1 and users[0]["content"] == prompt,
                     "session does not contain exactly the requested user prompt")
    evaluate.require(len(messages) == 1, "expected exactly one completed assistant text")
    evaluate.require(bool(usage), "runtime supplied no observed model/usage evidence")
    return {
        "requested_prompt_sha256": digest(prompt),
        "effective_user_message": users[0]["effective_content"],
        "effective_user_message_sha256": digest(users[0]["effective_content"]),
        "response": messages[0],
        "response_sha256": digest(messages[0]),
        "usage": usage,
    }


class LiveTransport:
    """One runtime, a fresh no-tool session for every independent response."""

    def __init__(self, directory: Path, models: set[str], timeout: float = 180):
        self.directory, self.models, self.timeout = directory, models, timeout
        self.client: Any = None
        self.settings: dict[str, dict] = {}
        self.reject_permission: Any = None
        self.capture_errors: tuple[type[Exception], ...] = ()

    async def __aenter__(self):
        try:
            from copilot import CopilotClient, RuntimeConnection
            from copilot.generated.rpc import PermissionDecisionReject
            from copilot._jsonrpc import JsonRpcError, ProcessExitedError
        except ModuleNotFoundError as error:
            raise DocumentError("install optional requirements-simulation.txt before live execution") from error
        evaluate.require(importlib.metadata.version("github-copilot-sdk") == SDK_VERSION,
                         f"live runner requires github-copilot-sdk=={SDK_VERSION}")
        self.capture_errors = (JsonRpcError, ProcessExitedError)
        executable = shutil.which("copilot")
        evaluate.require(executable is not None, "Copilot CLI is not installed")
        runtime = runtime_version(executable)
        token = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True,
        ).stdout.strip()
        evaluate.require(bool(token), "GitHub CLI did not provide authentication")
        self.reject_permission = lambda request, invocation: PermissionDecisionReject(
            feedback="Tools are not permitted in this writing-only experiment.",
        )
        self.client = CopilotClient(
            connection=RuntimeConnection.for_stdio(
                path=executable,
                args=("--no-auto-update", "--disable-builtin-mcps", "--no-remote-export"),
            ),
            working_directory=str(self.directory),
            base_directory=str(self.directory / "runtime-state"),
            github_token=token,
            mode="empty",
            log_level="error",
        )
        try:
            await self.client.start()
            available = {model.id: model for model in await self.client.list_models()}
            for name in sorted(self.models):
                evaluate.require(name in available, f"model is unavailable: {name}")
                model = available[name]
                low = "low" in (model.supported_reasoning_efforts or [])
                self.settings[name] = settings_for(name, runtime, low)
        except BaseException:
            await self.client.stop()
            raise
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.client.stop()

    async def capture(self, model: str, prompt: str) -> dict:
        events: list[dict] = []
        options = dict(SESSION_OPTIONS)
        if self.settings[model]["reasoning_effort"] == "low":
            options["reasoning_effort"] = "low"
        started = utc_now()
        async with await self.client.create_session(
            model=model, on_permission_request=self.reject_permission, **options,
        ) as session:
            def collect(event):
                kind = event.type.value
                if kind in ("user.message", "assistant.message", "assistant.usage", "session.error") \
                        or kind.startswith(("tool.", "permission.")):
                    events.append(event.to_dict())

            session.on(collect)
            response, = await asyncio.gather(
                session.send_and_wait(prompt, timeout=self.timeout), return_exceptions=True,
            )
            if isinstance(response, BaseException):
                # The pinned SDK uses bare Exception for observed session errors.
                reported = [event for event in events if event["type"] == "session.error"]
                if reported:
                    kind = reported[0]["data"].get("errorType", "unknown")
                    raise DocumentError(f"runtime reported a session error: {kind}") from response
                raise response
            evaluate.require(response is not None, "session ended without an assistant response")
            evidence = evidence_from_events(events, prompt, model)
            evaluate.require(response.data.content == evidence["response"], "final response disagrees with event record")
        return {**evidence, "started_at": started, "completed_at": utc_now()}


def load_jobs(root: Path, path: Path) -> tuple[dict, list[dict]]:
    plan = evaluate.load_json(path)
    evaluate.fields(plan, {"schema_version", "jobs"}, "generation plan")
    evaluate.version(plan)
    evaluate.require(isinstance(plan["jobs"], list) and bool(plan["jobs"]), "jobs must be a nonempty list")
    jobs, seen = [], set()
    for item in plan["jobs"]:
        evaluate.fields(item, {"id", "request", "model", "family"}, "generation job")
        name = evaluate.nonempty(item["id"], "job id")
        evaluate.require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None, "invalid job id")
        evaluate.require(name not in seen, "duplicate job id")
        seen.add(name)
        evaluate.nonempty(item["request"], "request path")
        evaluate.nonempty(item["model"], "model")
        evaluate.require(item["model"] != "auto", "automatic model selection is not an experimental condition")
        family = evaluate.nonempty(item["family"], "family")
        evaluate.require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", family) is not None, "invalid family")
        request = evaluate.validate_request(root, evaluate.load_json(path.parent / item["request"]))
        jobs.append({**item, "request_value": request})
    return plan, jobs


def transport_errors(transport: Any) -> tuple[type[Exception], ...]:
    extra = getattr(transport, "capture_errors", ())
    evaluate.require(
        isinstance(extra, tuple) and all(
            isinstance(error, type) and issubclass(error, Exception) and error is not Exception
            for error in extra
        ),
        "capture_errors must contain specific exception classes",
    )
    return (DocumentError, OSError, RuntimeError, TimeoutError, ValueError, *extra)


async def run_jobs(
    root: Path, plan: dict, jobs: list[dict], output: Path, transport: Any, *,
    concurrency: int = 4, order_seed: int = 731, resume: bool = False,
) -> dict:
    evaluate.require(concurrency > 0, "concurrency must be positive")
    errors = transport_errors(transport)
    signature = {
        "schema_version": 1, "kind": "live-generation-plan",
        "plan_sha256": digest(evaluate.canonical(plan)),
        "requests": {job["id"]: job["request_value"]["request_sha256"] for job in jobs},
        "model_settings": transport.settings, "order_seed": order_seed,
    }
    if resume:
        evaluate.require(evaluate.load_json(output / "plan.json") == signature,
                         "resume plan, request hashes or model settings changed")
    else:
        output.mkdir(parents=True, exist_ok=False)
        evaluate.write_json(output / "plan.json", signature)
    shuffled = list(jobs)
    random.Random(order_seed).shuffle(shuffled)
    semaphore = asyncio.Semaphore(concurrency)
    results: dict[str, dict] = {}
    failures = 0

    async def execute(job: dict) -> None:
        nonlocal failures
        async with semaphore:
            name, request = job["id"], job["request_value"]
            target = output / name
            record_path = target / "record.json"
            if resume and record_path.exists():
                record = evaluate.validate_result(root, evaluate.load_json(record_path))
                evaluate.require(
                    record["request"]["request_sha256"] == request["request_sha256"]
                    and record["model"] == job["model"] and record["family"] == job["family"]
                    and record["settings"] == transport.settings[job["model"]],
                    "existing response does not match its planned job",
                )
                results[name] = {"status": "captured", "record_sha256": record["result_sha256"]}
                return
            if target.exists():
                results[name] = {"status": "blocked", "reason": "prior incomplete attempt retained; no silent retry"}
                return
            if failures >= 3:
                results[name] = {"status": "not_started", "reason": "transport circuit breaker"}
                return
            target.mkdir()
            evaluate.write_json(target / "request.json", request)
            try:
                capture = await transport.capture(job["model"], request["prompt"])
                evaluate.write_json(target / "capture.json", capture)
                record = evaluate.record(
                    root, request, capture["response"], job["model"], job["family"],
                    transport.settings[job["model"]],
                )
                evaluate.write_json(record_path, record)
                results[name] = {"status": "captured", "record_sha256": record["result_sha256"]}
            except errors as error:
                failures += 1
                failure = {"status": "failed", "error_type": type(error).__name__, "error": str(error)}
                evaluate.write_json(target / "failure.json", failure)
                results[name] = failure
            print(json.dumps({"job": name, **results[name]}), flush=True)

    await asyncio.gather(*(execute(job) for job in shuffled))
    summary = {
        "schema_version": 1, "kind": "live-generation-summary",
        "status": "captured" if all(item["status"] == "captured" for item in results.values()) else "incomplete",
        "planned_jobs": len(jobs),
        "captured_jobs": sum(item["status"] == "captured" for item in results.values()),
        "jobs": dict(sorted(results.items())),
        "completed_at": utc_now(),
    }
    filename = "summary.json" if not resume else f"resume-{digest(evaluate.canonical(summary))[:16]}.json"
    evaluate.write_json(output / filename, summary)
    return summary


async def main_async(args) -> int:
    plan, jobs = load_jobs(args.root, args.plan)
    runtime_dir = args.output.parent / f"{args.output.name}-runtime"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    async with LiveTransport(runtime_dir, {job["model"] for job in jobs}, args.timeout) as transport:
        result = await run_jobs(
            args.root, plan, jobs, args.output, transport,
            concurrency=args.concurrency, order_seed=args.order_seed, resume=args.resume,
        )
    print(json.dumps({"status": result["status"], "captured": result["captured_jobs"],
                      "planned": result["planned_jobs"]}))
    return int(result["status"] != "captured")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--order-seed", type=int, default=731)
    parser.add_argument("--timeout", type=float, default=180)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args(argv)
    try:
        evaluate.require(args.timeout > 0 and args.concurrency > 0, "timeout and concurrency must be positive")
        return asyncio.run(main_async(args))
    except (DocumentError, OSError, subprocess.CalledProcessError) as error:
        print(f"generate: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
