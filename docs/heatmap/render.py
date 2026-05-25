"""Render NIAH Phase 1 results into a heatmap PNG.

Reads ../../artifacts/*.json and emits docs/heatmap/niah_phase1.png.
matplotlib + numpy only, no network egress.

Each cell represents a single (model, context-length) measurement
(n=1 per cell — single seed=42 × single depth=50% × single 7-digit
magic-number needle), color-coded by status: PASS / OOM / TOKEN_LIMIT
/ ERROR / no-data.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = ROOT / "artifacts"
OUT = Path(__file__).resolve().parent / "niah_phase1.png"

STATUS_COLORS = {
    "PASS": "#3FB950",
    "OOM": "#F85149",
    "TOKEN_LIMIT": "#D29922",
    "ERROR": "#DA3633",
    "N/A": "#30363D",
}
STATUS_INDEX = {s: i for i, s in enumerate(STATUS_COLORS)}

MODEL_LABEL = {
    "Qwen/Qwen2.5-7B-Instruct-1M": "Qwen2.5-7B-1M (local, Windows native)",
    "Qwen/Qwen2.5-7B-Instruct-1M [WSL2 vLLM]": "Qwen2.5-7B-1M (local, WSL2 vLLM)",
    "deepseek/deepseek-v3-0324": "DeepSeek-V3 (cloud)",
    "meta/llama-3.3-70b-instruct": "Llama-3.3-70B (cloud)",
    "openai/gpt-4.1-mini": "GPT-4.1-mini (cloud)",
    "openai/gpt-5": "GPT-5 (cloud)",
}

CONTEXTS = [2000, 4000, 5000, 6000, 8000]


def load_cells() -> dict[tuple[str, int], tuple[str, str]]:
    cells: dict[tuple[str, int], tuple[str, str]] = {}
    for fp in sorted(ARTIFACTS.glob("*.json")):
        d = json.loads(fp.read_text(encoding="utf-8"))
        model = d.get("model")
        ctx = d.get("context_tokens_target")
        if not model or not ctx:
            continue
        status = d.get("status") or ("PASS" if d.get("output_text") else "ERROR")
        runtime = d.get("runtime", "")
        if runtime in ("vllm", "wsl2_vllm"):
            key = (f"{model} [WSL2 vLLM]", int(ctx))
        else:
            key = (model, int(ctx))
        cells[key] = (status, runtime)
    return cells


def main() -> int:
    cells = load_cells()
    models = list(MODEL_LABEL.keys())

    grid = np.full((len(models), len(CONTEXTS)), STATUS_INDEX["N/A"], dtype=int)
    annotations: list[tuple[int, int, str]] = []

    for (model, ctx), (status, _) in cells.items():
        if model not in models or ctx not in CONTEXTS:
            continue
        i = models.index(model)
        j = CONTEXTS.index(ctx)
        grid[i, j] = STATUS_INDEX.get(status, STATUS_INDEX["ERROR"])
        annotations.append((i, j, status))

    fig, ax = plt.subplots(figsize=(10, 4.5), facecolor="#0d1117")
    ax.set_facecolor("#0d1117")

    cmap = plt.matplotlib.colors.ListedColormap(list(STATUS_COLORS.values()))
    bounds = list(range(len(STATUS_COLORS) + 1))
    norm = plt.matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    ax.imshow(grid, cmap=cmap, norm=norm, aspect="auto")

    ax.set_xticks(range(len(CONTEXTS)))
    ax.set_xticklabels([f"{c:,}" for c in CONTEXTS], color="#c9d1d9", fontsize=11)
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels([MODEL_LABEL[m] for m in models], color="#c9d1d9", fontsize=10)
    ax.set_xlabel("Context length (tokens)", color="#c9d1d9", fontsize=12, labelpad=10)
    ax.set_title(
        "NIAH single-needle 7-digit magic number — Phase 1 (n=1 per cell)",
        color="#f0f6fc",
        fontsize=13,
        pad=14,
    )

    for i, j, label in annotations:
        text_color = "#0d1117" if STATUS_COLORS[label] in ("#3FB950", "#D29922") else "#f0f6fc"
        ax.text(j, i, label, ha="center", va="center", color=text_color, fontsize=9, fontweight="bold")

    ax.set_xticks(np.arange(-0.5, len(CONTEXTS), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(models), 1), minor=True)
    ax.grid(which="minor", color="#0d1117", linewidth=2)
    ax.tick_params(which="minor", length=0)
    ax.spines[:].set_visible(False)

    legend_patches = [
        plt.matplotlib.patches.Patch(facecolor=color, edgecolor="#30363D", label=label)
        for label, color in STATUS_COLORS.items()
    ]
    legend = ax.legend(
        handles=legend_patches,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.18),
        ncol=5,
        frameon=False,
        labelcolor="#c9d1d9",
        fontsize=10,
    )

    plt.tight_layout()
    fig.savefig(OUT, dpi=130, bbox_inches="tight", facecolor="#0d1117", pad_inches=0.3)
    plt.close(fig)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
