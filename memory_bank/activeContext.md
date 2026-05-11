# Active Context — longctx-needle-demo

## Current phase

**Phase 0** — Scaffold install (in progress, completing in this session)

## Current focus

GitHub repo の Phase 0 scaffold install を完遂し、 initial push で drift-check workflow が green になることを実測 verify する。

## Next concrete steps

1. PJ_REGISTRY.yaml (`~/.claude/PJ_REGISTRY.yaml`) に `longctx_needle_demo` entry 追加
2. `git add . && git commit -m "Phase 0: scaffold install"` + `git push`
3. `gh run watch` で drift-check workflow が green になるか実測
4. green 確認後、 logbook に Phase 0 完了 entry append
5. Phase 1 着手 (vllm install / Qwen 1M DL / NeedleInAHaystack clone + audit / baseline 走行)

## Blockers

なし (Phase 0 scope 内)。

## Open questions (next session で literal 解消)

- Windows host で vllm install するか、 WSL2 経由か (literal 試して安定 path 選定)
- VRAM 不足時 quant level (Q4_K_M / Q5 / FP16 のどれが consumer GPU で 1M context 完走可能か実測)
- GitHub Models free tier の 1 日 quota 実測 (Phase 2 で 4 model 走行に十分か)

## Out of scope (current phase)

- 実 eval 実行 (Phase 1)
- 4 size × 4 model 比較 (Phase 2)
- 動画撮影 (Phase 2)
- craftstack 統合 (Phase 3)
