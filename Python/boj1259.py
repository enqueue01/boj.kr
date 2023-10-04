while True:
    cnt = "yes"
    num = input()
    if num == "0":
        break
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            cnt = "no"
            break
        elif len(num) == 1:
            cnt = "yes"
    print(cnt)

    # if n == n[::-1]: 슬라이싱 알아두기