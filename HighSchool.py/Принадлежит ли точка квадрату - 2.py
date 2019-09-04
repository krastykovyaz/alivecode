def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1 and -1 <= x + y <= 1 and x - y <= 1 or x == y == 0


if IsPointInSquare(float(input()), float(input())):
    print('Yes')
else:
    print('No')
