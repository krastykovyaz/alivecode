def gcd(a, b):
    if a == 0 and b != 0:
        return b
    elif a != 0 and b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(int(input()), int(input())))
