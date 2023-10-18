import sys

input = sys.stdin.readline
S = set()
M = int(input())
for _ in range(M):
    x = None
    words = input().split(" ")
    if len(words) == 2:
        command, x = words[0], int(words[1])
    else:
        command = words[0].strip()

    if command == "add":
        S.add(x)
    elif command == "remove":
        if x in S:
            S.remove(x)
    elif command == "check":
        print("1" if x in S else "0")
    elif command == "toggle":
        if x in S:
            S.remove(x)
        elif x not in S:
            S.add(x)
    elif command == "all":
        S = {num for num in range(1, 21)}
    elif command == "empty":
        S.clear()
