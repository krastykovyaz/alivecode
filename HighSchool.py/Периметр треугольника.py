def distance(x1, y1, x2, y2, x3, y3):
    a = x1 - x2
    b = y1 - y2
    c = (a ** 2 + b ** 2) ** 0.5
    i = x2 - x3
    f = y2 - y3
    g = (i ** 2 + f ** 2) ** 0.5
    k = x1 - x3
    z = y1 - y3
    m = (k ** 2 + z ** 2) ** 0.5
    p = m + c + g
    return p


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
print(distance(x1, y1, x2, y2, x3, y3))
