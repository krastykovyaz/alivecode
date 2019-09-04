i = 0
k = 1
n = int(input())
while n != 0:
    k += n
    if n % 2 == 0:
        i += 1
    n = int(input())
print(i)
