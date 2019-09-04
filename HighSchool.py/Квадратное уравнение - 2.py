from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print(0)
elif a == 0 and b == 0:
    if c == 0:
        print(3)
    else:
        print(0)
elif a == 0:
    x3 = -c / b
    print(1, int(x3))
else:
    x1 = (- b + (sqrt(d))) / (2 * a)
    x2 = (- b - (sqrt(d))) / (2 * a)

    if x1 * 10 % 10 != 0:
        if x1 > x2:
            print(2, x2, x1)
        elif x1 == x2:
            print(1, x1)
        else:
            print(2, x1, x2)
    else:
        if x1 > x2:
            print(2, int(x2), int(x1))
        elif x1 == x2:
            print(1, int(x1))
        else:
            print(2, int(x1), int(x2))
