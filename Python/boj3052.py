array = []
for i in range(10):
    num = int(input())
    array.append(str(num % 42))
print(len(set(array)))