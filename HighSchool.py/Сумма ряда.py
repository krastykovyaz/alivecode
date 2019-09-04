n = int(input())
i = 1
s = 0
while i <= n:
    a = 1 / (i ** 2)
    i += 1
    s += a
print(s)
