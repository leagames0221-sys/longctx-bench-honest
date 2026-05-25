# longctx-bench-honest — PJ-local rules

## PJ Identity

- 案件: long-context benchmark honest measurement repo `longctx-bench-honest`
- 目的: long-context LLM (Qwen2.5-7B-1M local + cloud frontier via GitHub Models) × industry-current benchmarks (RULER + LongBench v2 + NIAH) の literal honest measurement、 全 cell JSON evidence、 全 cost ¥0、 drift-CI で文書/実態 強制同期
- scope: Phase 0 scaffold + 2026-05 overhaul → Phase 1 baseline → Phase 2 全 sweep + honest results → Phase 3 craftstack 統合

## PJ 固有 verify priority

1. `pytest tests/` (eval harness self-test)
2. `pip-audit` (Python deps 監査)
3. RULER baseline (128k subset) が公式 reference 数値範囲内か verify
4. cost-tier table の数値が `artifacts/` JSON evidence と literal 一致するか CI で照合
5. `gh workflow run drift-check`

## PJ 固有 用語

- **benchmark scope**: RULER (13 task) + LongBench v2 (503 MCQ) + NIAH (補助 heatmap)
- **model scope**: Qwen2.5-7B-Instruct-1M (local via vllm) + GPT-5 / Claude Sonnet / Llama 3.3 (cloud via GitHub Models)
- **cost-tier table**: README 上位 fold の 4 model × 3 benchmark + cost + 所要時間 + CC requirement の transparency table
- **honest results**: 失敗 task + 推定原因 + frontier gap を literal 開示する README section
- **prior art**: `NVIDIA/RULER` + `THUDM/LongBench` + `gkamradt/LLMTest_NeedleInAHaystack` + `vllm-project/vllm` + Qwen2.5-1M HuggingFace model card

## PJ 固有 forbidden / required

- 禁止: 受託案件文書 / client 機密 data の dataset 投入 (公開 source 限定)、 GitHub token の commit、 README の cost-tier table 数値を手動編集 (JSON evidence からの自動生成のみ)
- 必須: 全 numeric claim を JSON evidence で literal 裏付け、 失敗 task は `## Honest results` に literal 開示、 model 名 + benchmark 名 + repo 名 canon が README ↔ code ↔ CI で literal 一致

## 関連 doc

- `spec.md`: PJ 仕様 SSoT
- `memory_bank/decisionLog.md`: ADR-001 旧 (Qwen2.5 repo recipes 誤推奨) + ADR-001r1 (Qwen3.6-27B 誤推奨) + ADR-001r2 (Qwen2.5-7B-1M literal 戻し) の 2 度自己訂正記録あり
- `.github/workflows/drift-check.yml`: README claims 自動 verify (model/benchmark/repo 名 canon + Phase declaration + table 構造)
