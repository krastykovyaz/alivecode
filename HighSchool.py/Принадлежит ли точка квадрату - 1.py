def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


a = float(input())
b = float(input())
z = IsPointInSquare(a, b)
if z:
    print('Yes')
else:
    print('No')
