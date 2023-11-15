n = int(input())

def print_words(n):
    if n == 0:
        return
    else:
        print_words(n-1)
        print("HelloWorld")


print_words(n)