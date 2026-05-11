# longctx-needle-demo — spec

## 機能 list

- F-001: Qwen2.5-7B-Instruct-1M を vllm で local 走行、 literal 1M token context に対応
- F-002: Needle-in-a-Haystack eval harness を 4 context size (128k / 256k / 512k / 1M) で実行
- F-003: GitHub Models 経由で同 eval を GPT-5 / Claude Sonnet / Llama 3.3 で実行、 4 model 比較 table 出力
- F-004: 各点で 所要時間 / メモリ / 正答率 計測、 heatmap PNG 自動生成
- F-005: 自 domain dataset (e-Gov 法令 全文) 1M token + 質問 50 件で eval
- F-006: 30 秒 demo 動画 (OBS 撮影、 1M 文書 local 質問応答)
- F-007: drift CI が README claims を 100% verify

## 非機能要件

- API 課金: クレカ不要 (Qwen local + GitHub Models free tier、 Anthropic API 直接利用は禁止)
- consumer laptop (Windows 11 / 16GB+ RAM、 GPU VRAM 8GB+ 想定) で完走
- 真 1M 推論時間は実測値で決まる (D9 ★★ tier、 24h 超で literal 不能検出時のみ refactor 判断、 設計段階での上限引き下げ禁止 / D-NO-COMPROMISE-IN-DESIGN)
- 4 model 比較は GitHub Models rate limit 内に収まるよう間隔配信

## 依存

- 外部 OSS: `Qwen/Qwen2.5-7B-Instruct-1M` (Apache-2.0)、 `vllm-project/vllm` (Apache-2.0)、 `gkamradt/LLMTest_NeedleInAHaystack` (MIT)
- API: GitHub Models (CC 不要、 GitHub token のみ)
- Dataset: e-Gov 法令 (公的 free)、 Wikipedia 日本語 dump (CC-BY-SA)、 UE5 公式 docs (公開)
- CI: GitHub Actions (free tier)

## 完了条件 (acceptance criteria)

- AC-1: `python eval/run_needle.py --context-size 128000` で baseline heatmap 出力
- AC-2: 同 script を 256k / 512k / 1M で順次実行、 全 4 size の結果 PNG が `artifacts/` に literal 生成
- AC-3: `python eval/run_github_models.py --model gpt-5,claude-sonnet,llama-3.3` で 比較 table 出力
- AC-4: `pytest tests/` で全 test green
- AC-5: `pip-audit` で high severity issue 0 件
- AC-6: GitHub Actions drift-check green
- AC-7: README の `## Verified state` 各項目が drift-check と一致
- AC-8: 30 秒動画 (`docs/demo.mp4`) が repo に存在 (LFS 不要範囲のサイズ)

## Phase 進行

- Phase 0 (current): scaffold + drift CI + memory_bank + .gitignore 配線
- Phase 1: vllm install + Qwen2.5-1M weight DL (~15GB) + Needle-in-a-Haystack clone + baseline 走行
- Phase 2: 4 context size 実測 + 4 model GitHub Models 比較 + heatmap + 動画
- Phase 3: craftstack 統合 + r/LocalLLaMA + HN literal 投稿
