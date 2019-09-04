def distance(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    c = (a ** 2 + b ** 2) ** 0.5
    return c


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
