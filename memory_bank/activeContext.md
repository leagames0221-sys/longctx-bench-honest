# Active Context — longctx-bench-honest

## Current phase

**Phase 0 (overhaul commit pending)** — repo rename + scope literal 全面書き換え (Qwen2.5-7B-1M + RULER + LongBench v2 + 補助 NIAH に literal 確定、 ADR-001/003 archive + ADR-001-r2 / ADR-003-r1 新規) 完了見込、 overhaul commit + drift-check 再 verify 待ち。

## Current focus

repo rename (longctx-needle-demo → longctx-bench-honest) + 中身全面書き換えを literal commit、 drift-check workflow が new claim 群 (4 model 名 + 3 benchmark 名 + repo 名 canon + Phase declaration + cost-tier table 構造) を 全件 green で verify することを実測。

## Next concrete steps (Phase 1)

1. 3 prior art を `~/tmp/prior-art/` に literal 隔離 clone:
   - `git clone --depth 1 https://github.com/NVIDIA/RULER.git` (Apache 2.0、 既 clone 済 = 不要)
   - `git clone --depth 1 https://github.com/THUDM/LongBench.git` (Apache 2.0 想定、 audit で確定)
   - `gkamradt/LLMTest_NeedleInAHaystack` は既 clone 済 (補助 visual 用に literal 残す、 MIT 確認済)
   - `vllm-project/vllm` は既 clone 済 (Apache 2.0 確認済)
2. LongBench v2 LICENSE 詳細確認 (repo root LICENSE file Read)
3. vllm install path literal 実測 (Windows host 直接 → failure 時 WSL2 経由)、 結果を ADR-005 に literal 追記
4. `Qwen2.5-7B-Instruct-1M` HuggingFace DL (~15GB)、 disk + VRAM 実測、 BF16 / Q4 quant 判断
5. RULER 13 task generator を `eval/ruler/` に literal copy、 commit msg `derived from NVIDIA/RULER@<sha>`
6. LongBench v2 evaluation script を `eval/longbench/` に literal copy、 commit msg attribution
7. NIAH の `pretty_graph.py` を `eval/niah/` に literal copy (補助 visual 用)、 commit msg attribution
8. baseline 128k RULER subset 走行、 公式 reference 数値範囲内一致 verify
9. pip 配線: `pyproject.toml` + `uv.lock` commit + `pip-audit` CI step + `.github/dependabot.yml` for pip
10. GitHub Models sample call (small context) で接続 + free tier rate limit 実測
11. README Status を Phase 1 に更新、 drift-check workflow を Phase 1 用に拡張

## Blockers

なし (overhaul commit + drift-check 再 verify 後、 Phase 1 着手 OK)。

## Open questions (Phase 1 で literal 解消)

- Windows host で vllm install するか、 WSL2 経由か (literal 試して安定 path 選定、 ADR-005 起草)
- VRAM 不足時 quant level (Q4_K_M / Q5 / FP16 のどれが consumer GPU で 1M context 完走可能か実測)
- LongBench v2 LICENSE 詳細 (repo audit で確定)
- GitHub Models free tier の 1 日 quota 実測 (Phase 2 で 4 model 走行に十分か)

## Out of scope (current phase)

- 4 model × 3 benchmark 全 sweep (Phase 2)
- cost-tier table 数値 populate (Phase 2、 JSON evidence 由来自動生成)
- Honest results section literal 開示 (Phase 2)
- 30s 動画撮影 (Phase 2)
- craftstack 統合 (Phase 3)
- 日本語 domain dataset (literal scope 外、 ADR-004 で確定)
