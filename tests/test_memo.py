from memo import load_memos
import pytest


def test_load_memos_returns_lines(tmp_path):
    # 準備：2行のファイルを作る
    file_path = tmp_path/"memo.txt"
    file_path.write_text("卵を買う\n牛乳を買う\n", encoding="utf-8")
    # 実行：
    result = load_memos(file_path)
    # 確認：返り値が["卵を買う\n", "牛乳を買う\n"]と等しい
    assert result == ["卵を買う\n", "牛乳を買う\n"]


def test_load_memos_empty_file(tmp_path):
    # 準備：空のファイルを作る
    file_path = tmp_path/"memo.txt"
    file_path.write_text("")
    # 実行：
    result = load_memos(file_path)
    # 確認：返り値が[]と等しい
    assert result == []


def test_load_memos_file_not_found(tmp_path):
    # 準備：ファイルは作らない（パスだけ用意する）
    file_path = tmp_path/"memo.txt"
    # 実行と確認：FileNotFoundErrorが起きること
    with pytest.raises(FileNotFoundError):
        load_memos(file_path)

