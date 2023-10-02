num = []
for i in range(30):
    num.append(i + 1)
# num = [ num for num in range(1, 31)]

for _ in range(28):
    num.remove(int(input()))
# num_remove = [num.remove(int(input())) for _ in range(28)]

for i in range(len(num)):
    print(num[i])

# 풀이 확인할것