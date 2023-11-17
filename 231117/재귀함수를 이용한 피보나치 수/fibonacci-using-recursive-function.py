n = int(input())

def pivo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    return pivo(n-2) + pivo(n-1)


print(pivo(n))