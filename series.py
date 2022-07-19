print("Hello, World!")

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

firstTry = fibonacci(9)

print(firstTry)

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
tryLucas = lucas(8)

print(tryLucas)

def sum_series(n, option1=0, option2=1):
