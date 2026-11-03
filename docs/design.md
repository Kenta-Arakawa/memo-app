# memo-app 設計図

## 構成図
```mermaid
flowchart LR
    client[クライアント<br>curl / ブラウザ] --> |HTTP リクエスト| api[FastAPI<br>main.py]
    api --> |SQL| db[(SQLite<br>memo.db)]
```

## シーケンス図
### 一覧(GET /memos)
```mermaid
sequenceDiagram
    participant C as クライアント
    participant A as FastAPI
    participant D as SQLite

    C->>A: GET /memos
    A->>D: memos を全件取得
    D-->>A: メモの行(0件以上)
    A-->>C: 200 [{"id": 1, ...}, ...]
```

### 追加(POST /memos)
```mermaid
sequenceDiagram
    participant C as クライアント
    participant A as FastAPI
    participant D as SQLite

    C->>A: POST /memos {"content": "牛乳を買う"}
    A->>A: contentをチェック

    alt contentが正しい
        A->>D: contentとcreated_atを保存
        D->>D: idを採番
        D-->>A: 保存した行(id=1)
        A-->>C: 201 {"id": 1, "content": "牛乳を買う", "created_at": "..."}
    else contentが空・空白だけ・改行を含む・200文字超え
        A-->>C: 422 {"detail": "（エラーの理由）"}
    end
```

### 検索（GET /memos?keyword=牛乳）
```mermaid
sequenceDiagram
    participant C as クライアント
    participant A as FastAPI
    participant D as SQLite

    C->>A: GET /memos?keyword=牛乳
    A->>A: keywordをチェック

    alt keywordが正しい
        A->>D: keywordを送る
        D->>D: keywordを含むメモを取得
        D-->>A: 該当する行（0件以上）
        A-->>C: 200 [{"id": 2, "content": "牛乳を買う", "created_at": "..."}, ...]
    else keywordが空、空白だけ
        A-->>C: 422 {"detail": "(エラーの内容)"}
    end
```


### 削除（DELETE /memos/{id}）
```mermaid
sequenceDiagram
    participant C as クライアント
    participant A as FastAPI
    participant D as SQLite

    C->>A: DELETE /memos/{id}
    A->>A: idをチェック
    alt idが整数
        A->>D: idを送る
        D->>D: idに該当するメモを探す
        alt idに該当するメモがある
            D->>D: idに該当するメモを削除
            D-->>A: 削除した行
            A-->>C: 200 {"id": 2, "content": "牛乳を買う", "created_at": "..."}
        else idに該当するメモがない
            D-->>A: 該当なし（0件）
            A-->>C: 404 {"detail": "番号9999のメモはありません"}
        end
    else idが整数でない
        A-->>C: 422 {"detail": "削除するメモの番号は整数で指定してください"}
    end
```

## エラー処理の方針
- 入力チェックはクライアントからFastAPIへリクエストが送られたタイミングでFastAPI内で行っている。
- エラーの時、DBは変更されない。
- ステータスコードを決めるのはFastAPI
- 404だけはFastAPIだけでは判断できない。メモがあるかどうかはDBに聞いて初めてわかるので、DBの結果（該当なし）を見て、FastAPIが404を返す
