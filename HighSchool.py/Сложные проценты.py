import math
p = (int(input()) / 100) + 1
x = int(input())
y = float(input()) / 100
k = int(input())
total = x + y
i = 1
while i < k:
    i += 1
    total2 = int(100 * total * p) / 100
    total = total2
t = total * p
newt = int(t * 100 % 100)
print(math.floor(t), newt)
