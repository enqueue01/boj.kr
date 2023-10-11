result, ac = 0, 1
for i in range(int(input())):
    score = input()
    for j in score:
        if j == "O":
            result += ac
            ac += 1
        else:
            ac = 1
    print(result)
    result, ac = 0, 1