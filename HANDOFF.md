# memo-app 引き継ぎメモ

Claude Code への指示: このファイルを読んで、ここまでの経緯を把握してから続きを進めてください。

## 私について
- エンジニア初心者。Webエンジニアとして働き始めたばかり(職場では JavaScript と Python を使うらしい)
- 目的: Linux の基本コマンド、git/GitHub、Python を実践で体系的に身につけること

## 各月末までに身に着けたい能力
# 2026.10月
 - Linuxの基本コマンド、GitとGitHub、Pythonの基礎
 # 11月
  - HTTPとREST、API設計、ER図と正規化、構成図、シーケンス図、構造化ロジックの設計
  - 前半で基本設計（API一覧、テーブル定義、構成図）、中旬でシーケンス図とエラー処理（詳細設計）、月末ではFast APIの公式チュートリアルを一通りこなせるようになる
# 12月
 - Fast APIとSQLiteによるAPI実装、pytestによる単体、結合テスト、PRの運用
 - 実装し、単体テストと受入テストをpytestで自動化する
 - AIDLC v2をもちいた開発を行う。(上記2つを経験し、ある程度身に着けてから)
 # 2027.1月
 - AWSコンソールでLambda, S3, Cloud Watch Logsを実際に触る。AWSを触りながらAWSの基本的な操作は一通りできるようになる。
 - AWSを活用するうえで月5000円未満の範囲であれば課金してもいい

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

## 次にやること
1. [x] Ubuntu の初期設定: `sudo apt update && sudo apt upgrade -y`、`python3-venv` と `python3-pip` の導入
2. [x] VS Code の WSL 拡張を入れ、`~/projects/memo-app` を `code .` で開く
3. [x] git の初期設定(user.name / user.email。email は GitHub の noreply アドレス)
4. [x] GitHub に SSH 鍵を登録し、リポジトリを作成する(`git@github.com:Kenta-Arakawa/memo-app.git`)
5. [x] `memo add` を実装(#1 → PR #2)、空メモを拒否(#4 → PR #5)
6. [x] `memo list` を実装(#3 → PR #6)
7. [x] `memo search` を実装する(issue → `feature/<番号>-memo-search` ブランチで。ヒントは出し済み: `in` 演算子で判定、番号は list と同じものを表示する=絞り込み前に enumerate、ヒットなし/ファイルなしのメッセージ)
8. [x] `memo delete` を実装する
9. [x] フェーズ1の学んだことを README に書く
10. [x] フェーズ2:CLI とメモ操作のロジックを分離し、pytest を導入する(venv・pytest 導入 #14 → PR #15、関数の分離と TDD #16 → PR #17、学習ログ PR #19)
    - memo.py は「main() = 引数・表示・エラー表示」「関数 = 処理(print しない)」に分かれた。関数: `load_memos` / `search_memos` / `delete_memo` / `save_memos` / `add_memo`、ファイル名は定数 `MEMO_FILE`
    - テストは `tests/test_memo.py` に 19 件。main() のテストはまだない(別 issue にした。12月の結合テストで扱う)
    - 空キーワードのチェックが main() と `search_memos` の2か所にあるのは意図的(main() 側は「ファイルを読む前に入力を確かめる」役割)

### フェーズ3の準備(11月):設計と HTTP/REST
11. [ ] HTTP と REST の基礎:リクエスト / レスポンス、メソッド(GET / POST / PUT / DELETE)、ステータスコード、JSON。`curl` で公開 API を叩いて確かめる
12. [ ] memo-app の API 一覧を作る(CLI の add / list / search / delete を、URL・メソッド・ステータスコードに対応させる)
13. [ ] ER 図とテーブル定義(メモに id・作成日時などを持たせる。正規化の考え方)
14. [ ] 構成図とシーケンス図(正常系とエラー系)、エラー処理の方針
15. [ ] FastAPI の公式チュートリアルを一通り進める(月末)
16. [ ] 12月:設計をもとに FastAPI + SQLite で実装し、pytest で単体・結合テストを書く(main() の結合テストの issue もここで扱う)

## 作業上の注意
- SSH 鍵にパスフレーズがあるので、push / fetch / pull はユーザーが行う
- 動作確認は本物の memo.txt を使わず、一時フォルダで行う
- pytest が緑でも CLI が壊れることがある(main() はテストされていない)。main() を変えたら CLI でも確認する
