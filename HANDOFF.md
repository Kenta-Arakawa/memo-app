# memo-app 引き継ぎメモ

Claude Code への指示: このファイルを読んで、ここまでの経緯を把握してから続きを進めてください。

## 私について
- エンジニア初心者。Webエンジニアとして働き始めたばかり(職場では JavaScript と Python を使うらしい)
- 目的: Linux の基本コマンド、git/GitHub、Python を実践で体系的に身につけること

## 進め方の約束
- コードの本体は私が書く。Claude はまずヒントを出し、レビューやエラーの解説をする
- 設定ファイルなどの定型作業は Claude が雛形を作ってよい
- 1機能ごとに issue → ブランチ → PR → セルフレビュー → マージ の流れで進める
- 各フェーズの終わりに README に学んだことを書く

## ロードマップ
1. CLI版(add / list / search / delete): Python の基礎、Linux、git の基本
2. CLI とメモ操作のロジックを分離し、pytest を導入する
3. FastAPI で REST API (CRUD) を作る
4. SQLite + SQLAlchemy に移行し、マイグレーションを扱う
5. フロントエンドを作る(まず素の HTML/JavaScript、余裕があれば React)
6. GitHub Actions (CI)、Docker、デプロイ

## 環境の状況(2026-10-17 時点)
- Windows 11。WSL2 + Ubuntu のインストールと、ユーザー作成まで完了
- Windows 側には Git 2.54 と Node v24 が入っている。gh (GitHub CLI) は未導入
- プロジェクトは Linux 側の `~/projects/memo-app` に置く
- 作業は VS Code を WSL に接続した状態(左下に「WSL: Ubuntu」)で行う。Windows 側から `\\wsl.localhost\...` で開くと、Windows の git が「dubious ownership」エラーを出す
- 残りの小さな片付け: リモートの `feature/1-memo-add` ブランチが未削除

## 次にやること
1. [x] Ubuntu の初期設定: `sudo apt update && sudo apt upgrade -y`、`python3-venv` と `python3-pip` の導入
2. [x] VS Code の WSL 拡張を入れ、`~/projects/memo-app` を `code .` で開く
3. [x] git の初期設定(user.name / user.email。email は GitHub の noreply アドレス)
4. [x] GitHub に SSH 鍵を登録し、リポジトリを作成する(`git@github.com:Kenta-Arakawa/memo-app.git`)
5. [x] `memo add` を実装(#1 → PR #2)、空メモを拒否(#4 → PR #5)
6. [x] `memo list` を実装(#3 → PR #6)
7. [ ] `memo search` を実装する(issue → `feature/<番号>-memo-search` ブランチで。ヒントは出し済み: `in` 演算子で判定、番号は list と同じものを表示する=絞り込み前に enumerate、ヒットなし/ファイルなしのメッセージ)
8. [ ] `memo delete` を実装する
9. [ ] フェーズ1の学んだことを README に書く
