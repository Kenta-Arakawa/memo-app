import pytest

from memo import load_memos
from memo import search_memos
from memo import delete_memo
from memo import save_memos
from memo import add_memo


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


def test_delete_memo_middle_delete():
    remaining, deleted = delete_memo(["卵を買う\n", "牛乳を買う\n", "Pythonの勉強\n"], 2)
    assert remaining == ["卵を買う\n", "Pythonの勉強\n"]
    assert deleted == "牛乳を買う"


def test_delete_memo_zero_delete():
    with pytest.raises(ValueError, match="番号0のメモはありません。"):
        delete_memo(["卵を買う\n", "牛乳を買う\n", "Pythonの勉強\n"], 0)


def test_delete_memo_over_number():
    with pytest.raises(ValueError, match="番号4のメモはありません。"):
        delete_memo(["卵を買う\n", "牛乳を買う\n", "Pythonの勉強\n"], 4)


def test_delete_memo_minus():
    with pytest.raises(ValueError, match="番号-1のメモはありません。"):
        delete_memo(["卵を買う\n", "牛乳を買う\n", "Pythonの勉強\n"], -1)


def test_save_memos(tmp_path):
    # 書き込むメモのリストとファイルのパスを用意する
    file_path = tmp_path/"memo.txt"
    memos = ["卵を買う\n", "牛乳を買う\n"]
    # save_memosにパスとリストを渡して、ファイルに書き込む
    save_memos(file_path, memos)
    # load_memosでそのファイルを読み返すと、準備したリストと同じになる
    assert load_memos(file_path) == memos


def test_add_memo_new_file(tmp_path):
    # 準備：ファイルパスを作成する
    file_path = tmp_path/"memo.txt"
    # 実行
    add_memo(file_path, "牛乳を買う")
    # 確認
    assert load_memos(file_path) == ["牛乳を買う\n"]


def test_add_memo_existing_file(tmp_path):
    file_path = tmp_path/"memo.txt"
    file_path.write_text("卵を買う\n", encoding="utf-8")
    add_memo(file_path, "牛乳を買う")
    assert load_memos(file_path) == ["卵を買う\n", "牛乳を買う\n"]


def test_add_memo_trim(tmp_path):
    file_path = tmp_path/"memo.txt"
    add_memo(file_path, "　牛乳を買う ")
    assert load_memos(file_path) == ["牛乳を買う\n"]


def test_add_memo_no_words(tmp_path):
    file_path = tmp_path/"memo.txt"
    with pytest.raises(ValueError, match="メモの内容が空です。追加できません。"):
        add_memo(file_path, "　")
    assert not file_path.exists()


def test_add_memo_with_n(tmp_path):
    file_path = tmp_path/"memo.txt"
    with pytest.raises(ValueError, match="メモの内容に改行は含められません。"):
        add_memo(file_path, "牛乳\n卵")
    assert not file_path.exists()
