num = int(input())
cnt = 0

while num >= 0:
    try:
        if num % 5 == 0:
            cnt += num // 5
            print(cnt)
            break
        num -= 3
        cnt += 1
    except:
        break
else:
    print(-1)