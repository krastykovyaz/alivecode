import math
p = (int(input()) / 100) + 1
x = int(input())
y = float(input()) / 100
total = (x + y) * p
newt = int(total * 100 % 100)
print(math.floor(total), newt)
