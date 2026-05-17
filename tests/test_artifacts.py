"""Schema integrity checks for committed benchmark evidence.

Each JSON file under artifacts/ is a record of a literal measurement run
(local Qwen / GitHub Models cloud / WSL2 vllm). The drift discipline that
underpins the portfolio thesis requires these records stay parseable and
carry the minimum identifying fields. These checks enforce that invariant.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

BASELINE_REQUIRED = {"task", "model", "context_tokens_target"}
CLOUD_REQUIRED = {"task", "model", "context_tokens_target"}
WSL_VLLM_REQUIRED = {"task", "model"}


def _artifact_files(repo_root: Path) -> list[Path]:
    artifacts = repo_root / "artifacts"
    return sorted(p for p in artifacts.glob("*.json") if p.is_file())


def test_artifacts_dir_populated(repo_root: Path) -> None:
    files = _artifact_files(repo_root)
    assert files, "artifacts/ must contain at least one measurement record"


@pytest.mark.parametrize(
    "artifact_path",
    _artifact_files(Path(__file__).resolve().parent.parent),
    ids=lambda p: p.name,
)
def test_artifact_is_valid_json(artifact_path: Path) -> None:
    with artifact_path.open(encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict), f"{artifact_path.name}: top-level must be object"


@pytest.mark.parametrize(
    "artifact_path",
    _artifact_files(Path(__file__).resolve().parent.parent),
    ids=lambda p: p.name,
)
def test_artifact_has_required_keys(artifact_path: Path) -> None:
    with artifact_path.open(encoding="utf-8") as f:
        data = json.load(f)

    name = artifact_path.name
    if name.startswith("baseline_"):
        required = BASELINE_REQUIRED
    elif name.startswith("cloud_"):
        required = CLOUD_REQUIRED
    elif name.startswith("wsl_vllm_"):
        required = WSL_VLLM_REQUIRED
    else:
        required = {"task", "model"}

    missing = required - data.keys()
    assert not missing, f"{name}: missing required keys {missing}"
