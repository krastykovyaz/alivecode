def fastup(a, n):
    if n % 2 == 0:
        x = (a ** 2) ** (n / 2)
    else:
        x = a * a ** (n - 1)
    return x


print(fastup(float(input()), int(input())))
