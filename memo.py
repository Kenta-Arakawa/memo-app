import argparse


def load_memos(file_path):
    """
    memo.txtを読み込み、メモのリストを返す
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        memos = f.readlines()
    return memos


parser = argparse.ArgumentParser(description="メモアプリ")
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add", help="メモを追加する")
add_parser.add_argument("memo", help="追加するメモの内容")

list_parser = subparsers.add_parser("list", help="メモ一覧を表示する")

search_parser = subparsers.add_parser("search", help="メモを検索する")
search_parser.add_argument("keyword", help="検索するキーワード")

args = parser.parse_args()

if args.command == "add":
    memo_content = args.memo.strip()
    if memo_content == "":
        add_parser.error("メモの内容が空です。追加できません。")
    with open("memo.txt", "a", encoding="utf-8") as f:
        f.write(memo_content + "\n")
    print("メモを追加しました。")
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
elif args.command == "search":
    keyword = args.keyword.strip()
    if keyword == "":
        search_parser.error("検索キーワードが空です。")
    try:
        memos = load_memos("memo.txt")
        if not memos:
            print("メモはまだありません。")
        else:
            found_memos = []
            for i, memo in enumerate(memos, start=1):
                if keyword.lower() in memo.lower():
                    found_memos.append((i, memo))
            if not found_memos:
                print(f"「{keyword}」に一致するメモは見つかりませんでした。")
            else:
                print(f"「{keyword}」の検索結果:")
                for i, memo in found_memos:
                    print(f"{i}. {memo.rstrip('\n')}")
    except FileNotFoundError:
        print("メモファイルが見つかりません。")
