a = int(input())
b = a // 1000
c = a // 100 % 10
d = a // 10 % 10
f = a % 10
print((c - d) % 10 + (b - f) % 10 + 1)
