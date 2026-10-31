# memo-app

ターミナルで使うメモアプリ。Linux、git/GitHub、Python の学習用。

## 使い方

Python 3.12 以上が必要です。メモは、コマンドを実行したフォルダの `memo.txt` に保存されます。

### メモを追加する
    python3 memo.py add "牛乳を買う"

前後の空白は取り除いて保存されます。空のメモや、改行を含むメモは保存できません。

### メモを一覧表示する
    python3 memo.py list

    メモ一覧:
    1. 卵を買う
    2. 牛乳を買う

### メモを検索する
    python3 memo.py search 牛乳

    「牛乳」の検索結果:
    2. 牛乳を買う

キーワードを含むメモを表示します(英字の大文字・小文字は区別しません)。番号は list と同じです。

### メモを削除する
    python3 memo.py delete 2

    「牛乳を買う」を削除しました。

番号は list・search で表示される番号です。削除すると、後ろのメモの番号が1つずつ繰り上がります。

## 開発

### 準備
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

### テストの実行
```bash
source .venv/bin/activate   # ターミナルを開くたびに必要
pytest -v
```

## 学習ログ
### フェーズ0: 環境構築
- WSL2、git、SSH の環境構築

### フェーズ1: CLI 版(2026年10月)
 - add, list, search, delete機能を実装
 - python, linuxコマンド, git/GitHubを駆使して実装することで下記の要素を学んだ
#### Python
 - argparseライブラリを用いて、コマンドの設定と各コマンドでの処理について整理した
 - 基本文法に加え、関数や例外処理についても整理した
 - クラス、venvについては現状まだ携われていない
- try は、エラーが起きる1行だけを囲む、入力のチェックは、ファイルを読む前に行う
#### Linux
 - pwd, ls, cd, cat, mkdir, cp, rm, touchについて学ぶ
 - ハイフンでのオプションについても一部習得、-d, -s, -cなど。こちらはまだまだ慣れが必要
 - 終了コード(echo $?。0 は成功、2 は使い方の誤り)
 - diff で2つのファイルの違いを確かめる
 - cat -E(行末を表示)、wc -l(行数を数える)
#### git / GitHub
 - clone, branch, commit, pull, push, add, git switch, git branch -d / git push origin --delete について学ぶ
 - --oneline, -d, -uなども知る
 - PRもできるようになった
 - git add -p で変更の一部だけをコミットする
 - push 前は amend で直せるが、push 後は新しいコミットで直す
 - git branch(作るだけ)と git switch -c(作って切り替える)の違い
#### 要件定義・レビュー
 - 少しかじったが正直未習得、今後設計も行う中で身に着けていく
#### つまずいたこと・気づいたこと
 - 要件と異なる文言でエラー文言を書いていた。Issueで設定した仕様と照らし合わせながらコードを作成していく必要がある。
 - VS Code で保存し忘れて、古いコードのままテスト・コミットした(2回)
 - git branch でブランチを作っただけで、main のまま作業していた
 - try / except の位置を間違えて SyntaxError になった
