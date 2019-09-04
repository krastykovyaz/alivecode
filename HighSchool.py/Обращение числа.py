n = int(input())
a = 0
while n > 0:
    remain = n % 10
    n //= 10
    a *= 10
    a += remain
print(a)
