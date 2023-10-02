code = list(map(int, input().split()))
asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = asc[:]
des.sort(reverse=True)

if code == asc:
    print("ascending")
elif code == des:
    print("descending")
else:
    print("mixed")

# re