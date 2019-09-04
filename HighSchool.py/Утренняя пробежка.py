x = int(input())
y = int(input())
k = 1
i = 0
while i + x < y:
    i += ((i + x) * 0.1)
    k += 1
print(k)
