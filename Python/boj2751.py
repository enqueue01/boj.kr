import sys

input = sys.stdin.readline
N = int(input())
num = []
for i in range(N):
    a = int(input())
    num.append(a)
num.sort()
for i in range(N):
    print(num[i])