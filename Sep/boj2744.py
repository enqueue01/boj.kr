S = input()
for i in range(len(S)):
    if S[i].islower():
        print(S[i].upper(), end="")
    else:
        print(S[i].lower(), end="")
# S[i].upper()로 하고 나중에 print(S)하면 안되는 이유-> Immutable (변형 불가능)