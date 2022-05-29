def factorial(n):
    if n == 0:
        return 1
    return mul(factorial(dec(n)), n)


def mul(b, n, a=0):
    if n == 0:
        return a
    if b == 1:
        return mul(b, dec(n), a + 1)
    return mul(b, dec(n), mul(1, b, a))


def dec(n, r=0):
    if r + 1 == n:
        return r
    return dec(n, r + 1)


print(factorial(5))
