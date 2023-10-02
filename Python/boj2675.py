T = int(input())
for i in range(T):
    j, k = input().split(" ")
    words = ""
    for n in range(len(k)):
        words += k[n] * int(j)
    print(words)