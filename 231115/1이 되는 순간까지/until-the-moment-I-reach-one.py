n = int(input())

def moment_toone(x):

    if x == 1:
        return 0
    
    if x % 2 == 0:
        return 1+moment_toone(x//2)
    else:
        return 1+moment_toone(x//3)


print(moment_toone(n))