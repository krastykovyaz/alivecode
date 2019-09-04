n = int(input())
a, b = 0, 1
i = 0
while i < n - 1:
    i += 1
    b, a = b + a, b
print(b)
