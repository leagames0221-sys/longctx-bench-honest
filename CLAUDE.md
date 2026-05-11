# longctx-needle-demo — Tier 2 PJ-local rules

> Tier 1 (~/.claude/SECRETARY_MASTER.md / ARA / Security) を auto-import 済。
> 本 file は PJ 固有規約のみ記述。 universal な doctrine は Tier 1 が担う。

## PJ Identity

- 案件: portfolio 用 long-context (1M token) benchmark demo (HIVE と無関係な独立 artifact)
- 目的: literal 1M token context の needle-in-a-haystack 実用 demo を local Qwen2.5-1M + GitHub Models 比較で構築、 クレカ不要範囲で完走
- scope: Phase 0 scaffold → Phase 1 baseline → Phase 2 1M 実測 + 4 model 比較 + heatmap → Phase 3 craftstack 統合
- target audience: 採用担当 / 受託先 / OSS / r/LocalLLaMA + HN community

## PJ 固有 verify priority

Tier 1 default (D-VERIFY-PRIORITY) を継承、 加えて:
1. `pytest tests/` (eval harness の self-test)
2. `pip-audit` (Python deps 監査)
3. Needle-in-a-Haystack heatmap が公式 baseline 再現範囲内か数値 verify
4. `gh workflow run drift-check`

## PJ 固有 用語

- **needle**: 1M token 文書中に埋め込む特定文字列、 LLM が正しく retrieve できるか測る probe
- **haystack**: needle を埋める長文書 (e-Gov 法令 / Wikipedia dump 等)
- **context size**: 128k / 256k / 512k / 1M の 4 点測定
- **prior art**: `QwenLM/Qwen2.5` + `gkamradt/LLMTest_NeedleInAHaystack` + GitHub Models docs

## PJ 固有 forbidden / required

- 禁止: 受託案件文書 / client 機密 data の haystack 投入 (公開 dataset 限定)、 GitHub token の commit
- 必須: 投入 dataset の出典 + LICENSE を README に明記、 全 4 context size 測定値を memory_bank/logbook.md に literal 記録

## 関連 doc

- `spec.md`: PJ 仕様 SSoT
- `memory_bank/`: Cline pattern 5 file (D-HANDOFF-DUTY)
- `.github/workflows/drift-check.yml`: README claims 自動 verify
- `.gitignore`: HuggingFace cache / dataset cache / .env 除外

## Memory Bank pattern

browser-agent-demo と同一 protocol (D-HANDOFF-DUTY literal 順守):
- session 開始: activeContext → logbook 末尾 § → 必要 ADR
- session 終了: logbook append、 ADR 発生時 decisionLog 新規、 focus 変更時 activeContext 更新
