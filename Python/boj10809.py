from string import ascii_lowercase

alphabet = list(ascii_lowercase)
S = input()
for i in range(len(alphabet)):
    print(S.find(ascii_lowercase[i]), end=" ")