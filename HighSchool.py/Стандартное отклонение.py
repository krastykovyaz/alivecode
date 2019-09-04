from math import sqrt
a = 0
a2 = 0
x = int(input())
i = 0
while x != 0:
    i += 1
    a += x
    a2 += x ** 2
    x = int(input())
print(sqrt((a2 - a ** 2 / i) / (i - 1)))
