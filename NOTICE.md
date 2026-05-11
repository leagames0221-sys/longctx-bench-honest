# NOTICE — Derived Sources

Files in `eval/` are derived from upstream open-source projects under their respective licenses.
D-PRIOR-ART-FIRST: ゼロから生成せず、 成熟したひな形から literal 抽出 + attribution。

---

## NVIDIA/RULER (Apache 2.0)

- **Source**: https://github.com/NVIDIA/RULER
- **Commit SHA**: `ab17b7853df4e0a30b78cd5d2b463ac7dff6ee13`
- **License**: Apache 2.0 — https://github.com/NVIDIA/RULER/blob/main/LICENSE
- **Audit (D-PRIOR-ART-SECURITY-GATE)**: 2026-05-11
  - stars: 1,536
  - last push: 2025-11-13 (6 months ago, stable mature)
  - open issues: 19 (small, well-maintained)
  - red flag: ZERO
- **Files derived to `eval/ruler/`**:
  - `scripts/synthetic.yaml` — 13 task configuration
  - `scripts/run.sh` — orchestration
  - `scripts/config_models.sh` + `config_tasks.sh` — config helpers
  - `scripts/data/{manifest_utils,prepare,template,tokenizer}.py` — pipeline core
  - `scripts/data/synthetic/*.py` — 13 task generators (niah, qa, variable_tracking, common_words_extraction, freq_words_extraction, etc.)
- **Modification scope**: Phase 1 = verbatim. Phase 2 customization ≤ 20% (model wrapper for Qwen2.5-7B-1M + GitHub Models OpenAI-compat)

---

## THUDM/LongBench (MIT)

- **Source**: https://github.com/THUDM/LongBench
- **Commit SHA**: `2e00731f8d0bff23dc4325161044d0ed8af94c1e`
- **License**: MIT — https://github.com/THUDM/LongBench/blob/main/LICENSE
- **Audit**: 2026-05-11
  - stars: 1,168
  - last push: 2025-01-15 (4 months ago, ACL 2025 publication frozen)
  - open issues: 67
  - red flag: ZERO
- **Files derived to `eval/longbench/`**:
  - `pred.py` — prediction loop
  - `result.py` — accuracy aggregation
  - `requirements.txt` — original deps reference
  - `config/` — model + task configs (entire dir)
  - `prompts/` — eval prompts (entire dir)
- **Modification scope**: Phase 1 = verbatim. Phase 2 customization ≤ 20%

---

## gkamradt/LLMTest_NeedleInAHaystack (MIT)

- **Source**: https://github.com/gkamradt/LLMTest_NeedleInAHaystack
- **Commit SHA**: `7b90d285651b68d39a94f3d3bd3672f84192c989`
- **License**: MIT — https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/LICENSE.txt
- **Audit**: 2026-05-11
  - stars: 2,282
  - last push: 2024-08-17 (stale ~2 years, but eval pattern foundational)
  - open issues: 25
  - red flag: ZERO (stale but methodology stable, NIAH saturated per industry but visual still useful)
- **Files derived to `eval/niah/`**:
  - `viz/` — heatmap visualization (supplementary, kept for portfolio visual)
  - `needlehaystack/` — Python package source
  - `requirements.txt` — original deps
- **Modification scope**: Phase 1 = verbatim. Phase 2 = supplementary heatmap PNG only (main eval is RULER + LongBench v2)

---

## Qwen/Qwen2.5-7B-Instruct-1M (Apache 2.0) — model weight

- **Source**: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M
- **License**: Apache 2.0
- **DL location**: `D:\hf_cache\hub` (via `HF_HOME` env var redirect, ~15GB)
- **No model files committed** (loaded at runtime via huggingface_hub)
- **Audit date**: 2026-05-11

---

## vllm-project/vllm (Apache 2.0) — used as library dependency

- **Source**: https://github.com/vllm-project/vllm
- **Audit**: 2026-05-11 (stars: 79,644, last push: 2026-05-11, license: Apache 2.0)
- **Usage**: declared in `pyproject.toml` as `vllm>=0.7.0; platform_system != 'Windows'` (WSL2 path on Windows host, see ADR-005)
- **No files copied** (library import only)

---

## License compatibility note

This repository is MIT-licensed. All derived files are Apache 2.0 (RULER, Qwen, vllm) or MIT (LongBench, NIAH). Both are compatible with this repo's MIT license. No GPL / AGPL dependencies.
