import sys

input = sys.stdin.readline

def myround(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

N = int(input())
if N != 0:
    level = []
    for _ in range(N):
        level.append(int(input()))

    level.sort()
    nonper = myround(N * 0.15)
    try:
        if nonper > 0:
            print(myround(sum(level[nonper:-nonper]) / len(level[nonper:-nonper])))
        else:
            print(myround(sum(level) / len(level)))
    except:
        print(0)
else:
    print(0)
#hard