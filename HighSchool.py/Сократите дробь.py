def gcd(a, b):
    if a == 0 and b != 0:
        return b
    elif a != 0 and b == 0:
        return a
    else:
        return gcd(b, a % b)


def ReduceFraction(n, m):
    k = gcd(n, m)
    return (n // k, m // k)


print(*ReduceFraction(int(input()), int(input())))
