import sys

def function_check(args):
    if len(args) < 3:
        return "Not enough arguments"
    
    # コマンドによって処理を変更
    if args[1] == "add":
        return args[2]
    else:
        return "Invalid operation"


print(function_check(sys.argv))