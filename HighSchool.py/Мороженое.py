k = int(input())
m = k % 5
n = k % 3
if k % 3 == 0 or k % 5 == 0:
    print('YES')
else:
    if k // 5 >= 1:
        if m == 1:
            print('YES')
        elif m == 2:
            print('NO')
        elif m == 3:
            print('YES')
        elif m == 4:
            print('YES')
    elif k // 3 >= 1:
        if n == 1:
            print('NO')
        elif n == 2:
            print('YES')
    else:
        print('NO')
