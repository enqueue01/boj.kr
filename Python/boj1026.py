sum = 0
_ = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
for _ in range(len(A)):
    sum += A.pop(A.index(max(A))) * B.pop(B.index(min(B)))
print(sum)
