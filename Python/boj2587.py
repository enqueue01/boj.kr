nums = [int(input()) for _ in range(5)]
print(sum(nums) // 5)
print(sorted(nums, key=lambda x: x)[2])