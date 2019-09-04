from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
A = a * d - b * c
x = (1 / A) * (d * e + (-b) * f)
y = (1 / A) * ((-c) * e + a * f)
print(x, y)
