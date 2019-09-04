n = int(input())
if 4 < n % 10 <= 9 or 10 < n < 20:
    print(n, 'korov')
elif n % 10 == 0:
    print(n, 'korov')
elif n % 10 == 1 and 20 < n < 101:
    print(n, 'korova')
elif n == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
