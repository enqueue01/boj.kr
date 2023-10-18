N = int(input())
nums = sorted([int(input()) for _ in range(N)],key= lambda x : x)
for i in nums:
    print(i)