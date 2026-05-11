# Product Context — longctx-needle-demo

## What

literal 1M token context の needle-in-a-haystack benchmark を local Qwen2.5-1M + GitHub Models 4 model 比較で構築。 公開 dataset (e-Gov 法令 / Wikipedia / UE5 docs) で 再現可能、 クレカ不要、 heatmap PNG + 動画 + 4 model 比較 table を 1 つの GitHub public repo に集約。

## Why

portfolio で strong hire 級 signal を立てる 2 件目 (1 件目 = browser-agent-demo)。 「クレカ無し / local 1M context 実用化」 は 2026-05 時点で literal 希少 keyword、 r/LocalLLaMA + Hacker News コミュニティで反応強い領域。 採用側に **コスト感覚 + 技術選定力 + measurement-first** の三重 signal を literal 一度に示す。

## Target audience

- 採用担当 (AI lab / 上位 startup / 受託 premium 帯)
- 受託案件先 (4 社: BCG / ミスミ / Goodpatch / ロフト、 long-context LLM 適用検討中の可能性)
- r/LocalLLaMA / Hacker News / Reddit AI 系 community (passive distribution 経路)

## Success signals (採用側が読み取るもの)

1. **literal 1M 達成**: heatmap PNG が 4 context size 全点で出力、 詐称不能
2. **4 model 比較**: Qwen local vs GPT-5 vs Claude Sonnet vs Llama 3.3 が同 eval で literal 比較
3. **コスト transparency**: 全工程の API 課金額 (= 0 円) + DL 容量 + 推論時間 を literal 数値開示
4. **drift CI**: README claims が code reality と literal 同期
5. **失敗 transparency**: 1M で literal 不能箇所が出ても、 失敗 process + 数値を honest に公開 (D9-CalibratedHonesty)

## Anti-signals (構造的に避けるもの)

- Phase 0 で literal な数値 claim を README に置かない (drift 必至、 CI fail)
- 受託機密 / client doc の haystack 投入
- GitHub token の commit 混入
- HuggingFace cache (15GB+) を repo に commit (`.gitignore` で literal 除外)
- 「1M で完璧動作」 claim、 実測値 (時間 / メモリ / 正答率) のみ literal 開示
