import sqlite3

from datetime import datetime
from zoneinfo import ZoneInfo



def init_db(db_path):
    """DBを初期化する関数"""
    # 1. connectでDBに接続する
    conn = sqlite3.connect(db_path)
    # 2. CREATE TABLE IF NOT EXISTSをexecuteする
    conn.execute("""
        CREATE TABLE IF NOT EXISTS memos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    # 3. commitしてcloseする
    conn.commit()
    conn.close()


def add_memo(db_path, content):
    """メモを追加する関数"""
    # 1. created_atを作る
    created_at = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat(timespec="seconds")
    # 2. connectして、INSERTをexecuteする（値は？で渡す）。返り値をcursorに入れる
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memos (content, created_at) VALUES (?, ?)", (content, created_at))
    # 3. commitしてcloseする
    conn.commit()
    conn.close()
    # 4. {"id": cursor.lastrowid, "content": content, "created_at": created_at}を返す
    return {"id": cursor.lastrowid, "content": content, "created_at": created_at}


def list_memos(db_path):
    """メモの一覧を取得する関数"""
    # 1. connectして、row_factoryを設定する
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    # 2. SELECT ... ORDER BY ... をexecuteして、fetchall()する
    cursor = conn.cursor()
    cursor.execute("SELECT id, content, created_at FROM memos ORDER BY id")
    rows = cursor.fetchall()
    # 3. closeする
    conn.close()
    # 4. 1行ずつdict(row)で辞書にして、リストにまとめてreturnする
    return [dict(row) for row in rows]

