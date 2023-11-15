n = int(input())

def sum_numbers(x):
    if x == 1:
        return 1

    return x + sum_numbers(x-1)

print(sum_numbers(n))