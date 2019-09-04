k = int(input())
i = 1
while i <= k:
    if k % i == 0 and i > 1:
        print(i)
        break
    i += 1
