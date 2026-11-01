import argparse


def load_memos(file_path):
    """
    memo.txtを読み込み、メモのリストを返す
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        memos = f.readlines()
    return memos


def search_memos(memos, keyword):
    """
    メモのリストから、キーワードを含むメモを探す。
    大文字、小文字は区別しない。
    （番号, メモ）のリストを返す。番号は1から始まる行番号。
    キーワードが空（空白だけを含む）の時はValueErrorを発生させる。
    """
    search_word = keyword.strip()
    if search_word == "":
        raise ValueError("検索キーワードが空です。")
    found_memos = []
    for i, memo in enumerate(memos, start=1):
        if search_word.lower() in memo.lower():
            found_memos.append((i, memo.rstrip('\n')))
    return found_memos


def main():
    parser = argparse.ArgumentParser(description="メモアプリ")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="メモを追加する")
    add_parser.add_argument("memo", help="追加するメモの内容")

    list_parser = subparsers.add_parser("list", help="メモ一覧を表示する")

    search_parser = subparsers.add_parser("search", help="メモを検索する")
    search_parser.add_argument("keyword", help="検索するキーワード")

    delete_parser = subparsers.add_parser("delete", help="メモを削除する")
    delete_parser.add_argument("index", help="削除するメモの番号")

    args = parser.parse_args()

    # メモの追加処理
    if args.command == "add":
        memo_content = args.memo.strip()
        if memo_content == "":
            add_parser.error("メモの内容が空です。追加できません。")
        if "\n" in memo_content or "\r" in memo_content:
            add_parser.error("メモの内容に改行は含められません。")
        with open("memo.txt", "a", encoding="utf-8") as f:
            f.write(memo_content + "\n")
        print("メモを追加しました。")
    # メモの一覧表示処理
    elif args.command == "list":
        try:
            memos = load_memos("memo.txt")
            if not memos:
                print("メモはまだありません。")
            else:
                print("メモ一覧:")
                for i, memo in enumerate(memos, start=1):
                    print(f"{i}. {memo.rstrip('\n')}")
        except FileNotFoundError:
            print("メモファイルが見つかりません。")
    # メモの検索処理
    elif args.command == "search":
        keyword = args.keyword.strip()
        if keyword == "":
            search_parser.error("検索キーワードが空です。")
        try:
            memos = load_memos("memo.txt")
            found_memos = search_memos(memos, keyword)
            if not memos:
                print("メモはまだありません。")
            elif not found_memos:
                print(f"「{keyword}」を含むメモは見つかりませんでした。")
            else:
                print(f"「{keyword}」の検索結果:")
                for i, memo in found_memos:
                    print(f"{i}. {memo}")
        except FileNotFoundError:
            print("メモファイルが見つかりません。")
    # メモの削除
    elif args.command == "delete":
        try:
            index = int(args.index)
        except ValueError:
            delete_parser.error("削除するメモの番号は整数で指定してください。")
        try:
            memos = load_memos("memo.txt")
            if not memos:
                print("メモはまだありません。")
            else:
                if index < 1 or index > len(memos):
                    delete_parser.error(f"番号{index}のメモはありません。")
                deleted_memo = memos.pop(index - 1)
                with open("memo.txt", "w", encoding="utf-8") as f:
                    f.writelines(memos)
                print(f"「{deleted_memo.rstrip('\n')}」を削除しました。")
        except FileNotFoundError:
            print("メモファイルが見つかりません。")


if __name__ == "__main__":
    main()
