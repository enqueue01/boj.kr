N = int(input())
result, ac = 0, 1
for i in range(N):
    score = input()
    for j in score:
        if j == "O":
            result = result + ac
            ac = ac + 1
        else:
            ac = 1
    print(result)
    result, ac = 0, 1