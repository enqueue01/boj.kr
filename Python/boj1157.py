cnt = []
word = input().upper()
setword = list(set(word))
for i in setword:
    cnt.append(word.count(i))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(setword[(cnt.index(max(cnt)))])