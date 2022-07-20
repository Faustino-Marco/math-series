print("Hello, World!")


def fibonacci(n):
    """
    Recursive function that takes input n and outputs fibonacci number at index 'n'
    Uses recursion to add two immediately preceding fibonacci numbers
    base case: n == 0 and n == 1 both return 1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Same as the fibonacci function, except the base case here is n == 0 returns 2 and n == 1 returns 1
    """
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
    Same as fibonacci and lucas series functions, except in this function we accept optional parameters (set to 1 and 1
    respectively, so as to imitate the fibonacci series.
    New unique series created depending on base case selections in function params.
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

