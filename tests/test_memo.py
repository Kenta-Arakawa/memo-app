import pytest

from memo import load_memos
from memo import search_memos


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


def test_search_memos():
    # 準備：["卵を買う", "牛乳を買う", "牛乳パックを捨てる"]といった内容の入ったメモを作成する
    # 実行："牛乳"で検索をかける
    result = search_memos(["卵を買う\n", "牛乳を買う\n", "牛乳パックを捨てる\n"], "牛乳")
    # 確認：検索できるか確認
    assert result == [(2, "牛乳を買う"), (3, "牛乳パックを捨てる")]


def test_search_memos_keyword_null_zenkaku():
    # 準備：なにもなし
    # 実行：空のキーワードで検索をかける
    # 確認："検索キーワードが空です。"というエラーが生じる
    with pytest.raises(ValueError, match="検索キーワードが空です。"):
        search_memos(["卵を買う\n", "牛乳を買う\n", "牛乳パックを捨てる\n"], "　")


def test_search_memos_keyword_null_hankaku():
    with pytest.raises(ValueError, match="検索キーワードが空です。"):
        search_memos(["卵を買う\n", "牛乳を買う\n", "牛乳パックを捨てる\n"], " ")


def test_search_memos_ignore_lowercase_keyword():
    result = search_memos(["Aがいい\n", "aもいい\n", "Bが大事\n"], "a")
    assert result == [(1, "Aがいい"), (2, "aもいい")]


def test_search_memos_ignore_uppercase_keyword():
    result = search_memos(["Aがいい\n", "aもいい\n", "Bが大事\n"], "A")
    assert result == [(1, "Aがいい"), (2, "aもいい")]


def test_search_memos_no_match():
    result = search_memos(["卵を買う\n", "牛乳を買う\n", "牛乳パックを捨てる\n"], "りんご")
    assert result == []

