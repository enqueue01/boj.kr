word = input()
for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        print("0")
        exit(0)
print("1")