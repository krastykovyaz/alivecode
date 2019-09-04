def sum1(a, b):
    if a == 0 and b != 0:
        return b
    elif b == 0 and a != 0:
        return a
    elif a == 0 and b == 0:
        return 0
    return sum1(a, b - 1) + 1


print(sum1(int(input()), int(input())))
