
x = float(input())
y = float(input())

if (x + 1) ** 2 + (y - 1) ** 2 <= 4 and y >= -x and y >= (2 * x) + 2:
    print('Yes')
elif y <= -x and y <= (2 * x) + 2 and (x + 1) ** 2 + (y - 1) ** 2 >= 4:
    print('Yes')
else:
    print('No')
