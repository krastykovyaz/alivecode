a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a <= c and b <= d:
    if a % 2 == 1 and b % 2 == 1:
        if c % 2 == 1 and d % 2 == 1:
            print("Yes")
        elif c % 2 == 0 and d % 2 == 0:
            print('Yes')
        else:
            print('No')
    elif a % 2 == 0 and b % 2 == 0:
        if c % 2 == 1 and d % 2 == 1:
            print("Yes")
        elif c % 2 == 0 and d % 2 == 0:
            print('Yes')
        else:
            print('No')
else:
    print('No')
