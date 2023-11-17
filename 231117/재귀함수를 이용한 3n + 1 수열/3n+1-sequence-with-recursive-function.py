n = int(input())


def recur_function(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1 + recur_function(n//2)
    elif n % 2 == 1:
        return 1 + recur_function(n*3+1)


print(recur_function(n))