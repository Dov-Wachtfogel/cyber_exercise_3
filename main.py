def factorial(n):
    if n == 0:
        return 1
    return add_mul(0, factorial(dec(n, 0)), n)


def add_mul(a, b, n):
    if n == 0:
        return a
    if b == 1:
        return add_mul(a + 1, b, dec(n, 0))
    return add_mul(add_mul(a, 1, b), b, dec(n, 0))


def dec(n, r):
    if r + 1 == n:
        return r
    return dec(n, r + 1)


print(factorial(5))
