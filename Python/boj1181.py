N = int(input())
words = []
for _ in range(N):
    words.append(input())
for word in (sorted(set(words), key=lambda x: (len(x), x))):
    print(word)

# set comprehension ->  words = {input() for _ in range(N)}