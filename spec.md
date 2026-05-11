# longctx-bench-honest — spec

## 機能 list

- F-001: Qwen2.5-7B-Instruct-1M を vllm で local 走行、 literal 1M token context
- F-002: RULER benchmark (NVIDIA、 13 task) を 4 model (Qwen2.5-7B-1M local + GPT-5 / Claude Sonnet / Llama 3.3 via GitHub Models) で実行、 4×13 cell の table 出力
- F-003: LongBench v2 (THUDM、 503 MCQ) を同 4 model で実行、 accuracy 比較 table 出力
- F-004: NIAH (gkamradt) を Qwen2.5-7B-1M で実行、 補助 heatmap PNG 1 枚を視覚資料として生成
- F-005: 各 cell に 所要時間 / メモリ / 正答率 / cost を計測、 JSON evidence を `artifacts/` 配下に literal 保存
- F-006: README の cost-tier transparency table を artifact JSON から自動生成、 手動編集禁止
- F-007: `## Honest results` section に 失敗 task + 推定原因 + frontier gap を literal 記載 (D9 順守)
- F-008: drift CI が README claims (table 構造 / 数値 / model 名 / benchmark 名 / repo 名) を 100% verify

## 非機能要件

- API 課金: クレカ不要 (Qwen local + GitHub Models free tier、 Anthropic API / OpenAI API 直接利用は禁止)
- consumer laptop (Windows 11 / 16GB+ RAM、 GPU VRAM 8-12GB 想定) で完走
- 真 1M 推論時間は実測値で決まる (D9 ★★ tier、 24h timeout 設定、 不能検出時は honest 公開、 設計上限引き下げ禁止 / D-NO-COMPROMISE-IN-DESIGN)
- GitHub Models rate limit 内に収まるよう 1 model ずつ間隔配信
- 投入文書は公開 dataset のみ (受託案件 / client 機密 literal 禁止)

## 依存

- 外部 OSS:
  - `Qwen/Qwen2.5-7B-Instruct-1M` (Apache-2.0)
  - `vllm-project/vllm` (Apache-2.0)
  - `NVIDIA/RULER` (Apache-2.0、 13 task long-context benchmark)
  - `THUDM/LongBench` (LongBench v2、 ACL 2025、 license は repo audit で確認)
  - `gkamradt/LLMTest_NeedleInAHaystack` (MIT、 補助 visual)
- API: GitHub Models (CC 不要、 GitHub token のみ)
- Dataset: RULER は generator 同梱、 LongBench v2 は HuggingFace `zai-org/LongBench-v2`、 NIAH は haystack 自動生成
- CI: GitHub Actions (free tier)

## 完了条件 (acceptance criteria)

- AC-1: `python eval/run_ruler.py --model qwen2.5-7b-1m --context-size 1000000` で 13 task 全件走行、 JSON evidence 出力
- AC-2: 同 script を GPT-5 / Claude Sonnet / Llama 3.3 GitHub Models 経由で走行、 全 4 model × 13 task = 52 cell の JSON 揃う (or honest 不能宣言)
- AC-3: LongBench v2 を 4 model 走行、 accuracy + JSON evidence
- AC-4: NIAH heatmap 1M PNG 出力 (Qwen2.5-7B-1M のみ、 補助 visual)
- AC-5: README cost-tier table が JSON evidence と literal 一致 (手書き編集 ZERO、 自動生成 script で生成)
- AC-6: README `## Honest results` section が literal populate (失敗 task + 原因 + frontier gap)
- AC-7: `pytest tests/` 全 green、 `pip-audit` high severity 0 件
- AC-8: GitHub Actions drift-check workflow が cost-tier table の数値整合性 + 各 model/benchmark 名 + Phase declaration + repo 名 canon を verify、 green
- AC-9: Dependabot enabled、 weekly schedule 配信確認
- AC-10: 30 秒録画 (`docs/demo.mp4`) で 「1M 文書 local 質問応答 + 4 model 比較 dashboard」 を視覚化

## Phase 進行

- Phase 0 (closed): scaffold install + 2026-05 overhaul commit (Qwen3.6-27B 案撤回、 Qwen2.5-7B-1M に literal 戻し、 RULER + LongBench v2 に literal 更新、 repo rename `longctx-needle-demo` → `longctx-bench-honest`)
- Phase 1 (next): vllm install path 検証 (Win vs WSL2、 ADR-005 起草) + Qwen2.5-7B-1M weight DL (~15GB) + RULER/LongBench v2/NIAH 3 repo clone/audit + baseline 128k 走行
- Phase 2: 4 model × 3 benchmark 全 sweep + JSON evidence + cost-tier table 自動生成 + Honest results section + 30s 動画
- Phase 3: craftstack 統合 + r/LocalLLaMA + HN post + GitHub Profile mirror
