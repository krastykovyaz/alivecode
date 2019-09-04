x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(y1 - x1) % 2 == 0 and (y2 - x2) % 2 == 0:
    if abs(y1 - x1) <= abs(y2 - x2):
        if x1 - x2 < 0 and y1 - y2 < 0:
            print('YES')
        else:
            print('NO')
    elif abs(y1 - x1) >= abs(y2 - x2):
        print('NO')
elif abs(y1 - x1) % 2 != 0 and (y2 - x2) % 2 != 0:
    if abs(y1 - x1) < abs(y2 - x2):
        print('YES')
        if x1 - x2 < 0 and y1 - y2 < 0:
            print('YES')
        else:
            print('NO')
    elif abs(y1 - x1) >= abs(y2 - x2):
        print('NO')
else:
    print('NO')
