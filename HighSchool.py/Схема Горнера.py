import math
n = int(input())
x = float(input())
p = 0
while n > 0:
    a = float(input())
    p = (p + a) * x
    n -= 1
a = float(input())
p += a
print(p)
