N = int(input())
result = 0
while True:
    if N>0:
        result += N
        N -= 1
    else:
        break
print(result)