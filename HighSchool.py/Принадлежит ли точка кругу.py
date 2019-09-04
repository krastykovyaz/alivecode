def IsPointInCircle(x, y, xc, yc, r):
    return xc - r <= x <= xc + r and yc - r <= y <= yc + r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('Yes')
else:
    print('No')
