n = int(input())
i = 0
while 1 <= n:
    if 100 < n <= 1000:
        if n % 10 == n // 100:
            i += 1
    elif 1000 < n <= 10000:
        if n % 100 == n // 100:
            i += 1
    elif n % 10 == n // 10 or n < 10:
        i += 1
    n -= 1
print(i)
