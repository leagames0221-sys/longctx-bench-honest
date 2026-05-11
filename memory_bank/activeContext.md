# Active Context — longctx-needle-demo

## Current phase

**Phase 1** — Prior art clone + audit + vllm install + Qwen 1M DL + baseline 128k eval (next session に着手予定)

## Current focus

Phase 0 完了 (drift-check workflow success run 25669544190)、 次 session の Phase 1 着手準備。

## Next concrete steps (Phase 1)

1. 3 prior art を `~/tmp/prior-art/` に隔離 clone:
   - `git clone https://github.com/vllm-project/vllm.git` (Apache-2.0)
   - `git clone https://github.com/QwenLM/Qwen2.5.git` (recipes 参照)
   - `git clone https://github.com/gkamradt/LLMTest_NeedleInAHaystack.git` (MIT)
2. 各 audit (star / commit / LICENSE / open Issues red flag)
3. vllm install path literal 実測 (Windows host vs WSL2)、 結果を ADR-005 として decisionLog に append
4. `Qwen2.5-7B-Instruct-1M` HuggingFace DL (~15GB)、 disk + VRAM 実測、 BF16 / Q4 quant 判断
5. NeedleInAHaystack の `eval/` + `pretty_graph.py` を 自 repo に literal copy、 commit msg attribution
6. baseline 128k 走行で公式 sample 数値範囲内一致 verify
7. pip 配線: `pyproject.toml` / `uv.lock` / `pip-audit` CI / Dependabot
8. GitHub Models sample call (small context) で接続 + free tier rate limit 実測
9. README Status を Phase 1 に更新、 drift-check workflow を Phase 1 用に拡張

## Blockers

なし (Phase 1 着手 OK)。

## Open questions (next session で literal 解消)

- Windows host で vllm install するか、 WSL2 経由か (literal 試して安定 path 選定、 ADR-005 起草)
- VRAM 不足時 quant level (Q4_K_M / Q5 / FP16 のどれが consumer GPU で 1M context 完走可能か実測)
- GitHub Models free tier の 1 日 quota 実測 (Phase 2 で 4 model 走行に十分か)

## Out of scope (current phase)

- 4 size × 4 model 16 cell 実測 (Phase 2)
- 動画撮影 (Phase 2)
- craftstack 統合 (Phase 3)
