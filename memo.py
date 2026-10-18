import argparse

parser = argparse.ArgumentParser(description="メモアプリ")
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add", help="メモを追加する")
add_parser.add_argument("memo", type = str, help="追加するメモの内容")



args = parser.parse_args()

if args.command == "add":
    memo_content = args.memo
    with open("memo.txt", "a", encoding="utf-8") as f:
        f.write(memo_content + "\n")
    print("メモを追加しました。")