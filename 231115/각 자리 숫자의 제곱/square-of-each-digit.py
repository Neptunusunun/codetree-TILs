n = int(input())

def square_nums(x):
    if x < 10:
        return x*x

    return square_nums(x//10) + (x % 10)*(x % 10)

print(square_nums(n))