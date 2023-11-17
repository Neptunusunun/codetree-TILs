n = int(input())

def num_rule(n):

    if n == 1:
        return 2
    elif n == 2:
        return 4

    return (num_rule(n-1) * num_rule(n-2)) % 100


print(num_rule(n))