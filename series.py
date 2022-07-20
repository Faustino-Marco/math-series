print("Hello, World!")


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


tryLucas = lucas(8)

print(tryLucas)


def sum_series(n, a=1, b=1):
    """
    Hi Kassie!!!!!!
    """
    # print(a)
    # print(b)
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        # print(b)
        # print(n)
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)


print(fibonacci(8))


print(sum_series(2, 3, 4))

