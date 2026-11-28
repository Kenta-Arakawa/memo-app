import pytest

from db import init_db, add_memo, list_memos


def test_init_db(tmp_path):
    # データベースファイルのパスを作成する
    db_path = tmp_path/"test.db"
    # データベースを初期化する
    init_db(db_path)
    # list_memosでメモの一覧を取得し、空であることを確認する
    assert list_memos(db_path) == []


def test_add_db(tmp_path):
    db_path = tmp_path/"test.db"
    init_db(db_path)
    memo = add_memo(db_path, "牛乳を買う")
    assert memo["id"] == 1
    assert memo["content"] == "牛乳を買う"
    assert "created_at" in memo


def test_add_db_twice(tmp_path):
    db_path = tmp_path/"test.db"
    init_db(db_path)
    add_memo(db_path, "牛乳を買う")
    add_memo(db_path, "卵を買う")
    memos = list_memos(db_path)
    assert len(memos) == 2
    assert memos[0]["id"] == 1
    assert memos[0]["content"] == "牛乳を買う"
    assert "created_at" in memos[0]
    assert memos[1]["id"] == 2
    assert memos[1]["content"] == "卵を買う"
    assert "created_at" in memos[1]


def test_init_db_twice(tmp_path):
    db_path = tmp_path/"test.db"
    init_db(db_path)
    init_db(db_path)
    assert list_memos(db_path) == []

