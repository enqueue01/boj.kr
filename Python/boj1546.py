N = int(input())
num = (list(map(int, input().split())))
num.sort()
M = num[-1]
for i in range(N):
    num[i] = num[i] / M * 100
print(sum(num) / N)