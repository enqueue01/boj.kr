def fac(n):
    result = 1
    if n > 0:
        for i in range(1, 1+n):
            result = result * i
    print(result)

n = int(input())
fac(n)