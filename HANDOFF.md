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

## 次にやること
1. [ ] Ubuntu の初期設定: `sudo apt update && sudo apt upgrade -y`、`python3-venv` と `python3-pip` の導入
2. [ ] VS Code の WSL 拡張を入れ、`~/projects/memo-app` を `code .` で開く
3. [ ] git の初期設定(user.name / user.email)
4. [ ] GitHub に SSH 鍵を登録し、リポジトリを作成する
5. [ ] フェーズ1の最初の機能 `memo add` を issue → ブランチ → PR の流れで実装する
