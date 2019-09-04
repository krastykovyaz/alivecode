def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        i = 1
        x = a
        while i < n:
            i += 1
            a *= x
        return a
    else:
        i = 1
        x = a
        while i < (-n):
            i += 1
            a *= x
        z = 1 / a
        return z


print(power(float(input()), int(input())))
