"""Shared parsing and accounting for the Markdown instruction library."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
from pathlib import Path
import re
import subprocess
from typing import Any
from collections.abc import Iterator
import unicodedata

import tiktoken
import yaml


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIRS = ("core", "domain", "citation", "user-interface")
CORE = tuple(
    f"core/{name}.md"
    for name in ("accuracy", "restraint", "voice", "anti-slop", "formatting", "rhythm")
)
OPERATIONS = ("draft", "edit", "review")
PACK_VARIANTS = ("full", "compact", "focused")


class DocumentError(ValueError):
    pass


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader: UniqueLoader, node: yaml.MappingNode) -> dict[str, Any]:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise yaml.YAMLError(f"{key_node.start_mark}: keys must be strings")
        if key in result:
            raise yaml.YAMLError(f"{key_node.start_mark}: duplicate key {key!r}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def read_yaml(text: str, label: str) -> dict[str, Any]:
    try:
        value = yaml.load(text, Loader=UniqueLoader)
    except yaml.YAMLError as error:
        raise DocumentError(f"{label}: invalid YAML: {error}") from error
    if not isinstance(value, dict):
        raise DocumentError(f"{label}: expected a mapping")
    return value


def string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise DocumentError(f"{label}: expected a list of strings")
    if len(value) != len(set(value)):
        raise DocumentError(f"{label}: duplicate entries")
    return value


def required_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise DocumentError(f"{label}: expected a nonempty string")
    return value


def iso_date(value: Any, label: str) -> str:
    if type(value) is date:
        return value.isoformat()
    if not isinstance(value, str):
        raise DocumentError(f"{label}: expected an ISO date")
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise DocumentError(f"{label}: invalid ISO date {value!r}") from error


def local_path(root: Path, name: str) -> Path:
    required_string(name, "path")
    path = Path(name)
    if path.is_absolute() or ".." in path.parts or "\\" in name or "\x00" in name or path.as_posix() != name:
        raise DocumentError(f"{name}: expected a repository-relative path")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise DocumentError(f"{name}: path leaves the repository")
    parts = {part.casefold() for part in resolved.relative_to(root.resolve()).parts}
    if parts & {"raw-data", ".git", ".venv", "node_modules"}:
        raise DocumentError(f"{name}: private or dependency material cannot be loaded")
    return resolved


def source_text(root: Path, name: str, revision: str | None = None) -> str:
    path = local_path(root, name)
    if revision is not None:
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise DocumentError("revision must be a full, lowercase Git commit ID")
        result = subprocess.run(
            ["git", "-C", str(root), "show", f"{revision}:{name}"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if result.returncode:
            raise DocumentError(f"{name}@{revision}: {result.stderr.strip()}")
        return result.stdout
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise DocumentError(f"{name}: {error}") from error


def unfenced_lines(content: str) -> Iterator[tuple[int, str]]:
    offset = 0
    fence: tuple[str, int] | None = None
    for line in content.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if marker:
            run, tail = marker.groups()
            if fence is None:
                fence = (run[0], len(run))
            elif run[0] == fence[0] and len(run) >= fence[1] and not tail.strip():
                fence = None
        elif fence is None:
            yield offset, line
        offset += len(line)
    if fence is not None:
        raise DocumentError("unclosed fenced code block")


def section_ranges(content: str) -> dict[str, tuple[int, int]]:
    headings = []
    for offset, line in unfenced_lines(content):
        heading = re.match(r"^## (.+?)\s*$", line)
        if heading:
            name = heading.group(1)
            if any(previous == name for previous, _ in headings):
                raise DocumentError(f"duplicate level-two heading: {name}")
            headings.append((name, offset))
    return {
        name: (start, headings[index + 1][1] if index + 1 < len(headings) else len(content))
        for index, (name, start) in enumerate(headings)
    }


@dataclass(frozen=True)
class Module:
    path: str
    metadata: dict[str, Any]
    text: str
    content: str
    sections: dict[str, tuple[int, int]]

    @classmethod
    def load(cls, root: Path, name: str, revision: str | None = None) -> Module:
        parts = Path(name).parts
        if not parts or parts[0] not in (*MODULE_DIRS, "sources") or not name.endswith(".md"):
            raise DocumentError(f"{name}: not a module or source dossier")
        text = source_text(root, name, revision)
        match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
        if match is None:
            raise DocumentError(f"{name}: missing YAML frontmatter")
        metadata = read_yaml(match.group(1), name)
        if metadata.get("layer") != parts[0]:
            raise DocumentError(f"{name}: layer must be {parts[0]!r}")
        required_string(metadata.get("id"), f"{name}: id")
        required_string(metadata.get("version"), f"{name}: version")
        if parts[0] == "user-interface":
            if metadata.get("kind") not in ("medium", "overlay"):
                raise DocumentError(f"{name}: kind must be medium or overlay")
            if "standalone" in metadata and type(metadata["standalone"]) is not bool:
                raise DocumentError(f"{name}: standalone must be a boolean")
            if metadata.get("standalone") is True and metadata["kind"] != "overlay":
                raise DocumentError(f"{name}: only overlays can be standalone")
        content = text[match.end():].strip()
        try:
            sections = section_ranges(content)
        except DocumentError as error:
            raise DocumentError(f"{name}: {error}") from error
        return cls(name, metadata, text, content, sections)

    @property
    def body(self) -> str:
        end = self.sections.get("Examples", (len(self.content), len(self.content)))[0]
        return self.content[:end].strip()

    @property
    def title(self) -> str:
        match = re.search(r"(?m)^# (.+)$", self.content)
        if match is None:
            raise DocumentError(f"{self.path}: missing document title")
        return match.group(1)

    def section(self, name: str) -> str:
        if name not in self.sections:
            raise DocumentError(f"{self.path}: missing ## {name}")
        start, end = self.sections[name]
        return self.content[start:end].strip()

    def render(self, variant: str, examples: bool = False) -> str:
        if variant not in PACK_VARIANTS:
            raise DocumentError(f"unknown variant: {variant}")
        if self.path.startswith("sources/"):
            raise DocumentError(f"{self.path}: source dossiers are not prompt modules")
        if variant == "compact" and self.metadata.get("layer") == "core":
            result = f"# {self.title}\n\n{self.section('Write')}"
        else:
            result = self.body
            if variant == "focused" and "Detect" in self.sections:
                start, end = self.sections["Detect"]
                result = (result[:start] + result[end:]).strip()
        if examples:
            result += f"\n\n{self.section('Examples')}"
        return result

    def example_sections(self) -> tuple[str, dict[str, str]]:
        section = self.section("Examples")
        matches = [
            (offset, match.group(1))
            for offset, line in unfenced_lines(section)
            if (match := re.match(r"^\*\*([^*\n]+)\*\*\s*$", line))
        ]
        if not matches:
            raise DocumentError(f"{self.path}: examples need named, standalone bold headings")
        examples = {}
        for index, (offset, heading) in enumerate(matches):
            normalized = unicodedata.normalize("NFKD", heading).encode("ascii", "ignore").decode()
            slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
            if not slug or slug in examples:
                raise DocumentError(f"{self.path}: ambiguous example heading {heading!r}")
            end = matches[index + 1][0] if index + 1 < len(matches) else len(section)
            examples[slug] = section[offset:end].strip()
        return section[:matches[0][0]].strip(), examples

    def render_examples(self, slugs: list[str]) -> str:
        preamble, examples = self.example_sections()
        for slug in slugs:
            if slug not in examples:
                raise DocumentError(f"{self.path}: unknown example {slug!r}")
        return "\n\n".join([preamble, *(examples[slug] for slug in slugs)])


def module_names(root: Path, include_sources: bool = False) -> list[str]:
    directories = (*MODULE_DIRS, "sources") if include_sources else MODULE_DIRS
    return sorted(
        path.relative_to(root).as_posix()
        for directory in directories
        for path in (root / directory).rglob("*.md")
    )


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def token_count(text: str) -> int:
    return len(tiktoken.get_encoding("o200k_base").encode(text, disallowed_special=()))


def load_profile(root: Path, name: str) -> dict[str, Any]:
    if not re.fullmatch(r"[a-z][a-z0-9-]*", name):
        raise DocumentError(f"invalid profile name: {name!r}")
    path = f"profiles/{name}.yaml"
    profile = read_yaml(source_text(root, path), path)
    allowed = {"name", "description", "modules", "safeguards"}
    if set(profile) - allowed:
        raise DocumentError(f"{path}: unknown fields: {sorted(set(profile) - allowed)}")
    if profile.get("name") != name:
        raise DocumentError(f"{path}: name must match the filename")
    required_string(profile.get("description"), f"{path}: description")
    string_list(profile.get("modules"), f"{path}: modules")
    string_list(profile.get("safeguards", []), f"{path}: safeguards")
    return profile


def validate_selection(modules: list[Module], safeguards: list[str]) -> None:
    paths = [module.path for module in modules]
    if len(paths) != len(set(paths)):
        raise DocumentError("module selection contains duplicates")
    if any(module.metadata.get("layer") in ("core", "sources") for module in modules):
        raise DocumentError("core is automatic; source dossiers cannot be selected")
    genres = [module for module in modules if module.path.startswith("domain/") and module.path.count("/") == 1]
    citations = [module for module in modules if module.path.startswith("citation/")]
    readers = [module for module in modules if module.path.startswith("domain/education-level/")]
    media = [module for module in modules if module.metadata["layer"] == "user-interface" and module.metadata["kind"] == "medium"]
    for label, selected in (("primary genre", genres), ("citation style", citations), ("classroom preset", readers), ("UI medium", media)):
        if len(selected) > 1:
            raise DocumentError(f"select at most one {label}")
    for module in modules:
        if module.metadata["layer"] == "user-interface" and module.metadata["kind"] == "overlay" and not media and module.metadata.get("standalone") is not True:
            raise DocumentError(f"{module.path}: requires a UI medium")
    for name in safeguards:
        if name not in ("medical", "legal"):
            raise DocumentError(f"unknown safeguard: {name!r}")
        if f"domain/{name}.md" in paths:
            raise DocumentError(f"{name} safeguards are already included in the primary domain")
