a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d or b <= d or c <= d:
    if a <= e or b <= e or c <= e:
        if a * b <= d * e:
            print('YES')
        elif a * c <= d * e:
            print('YES')
        else:
            print('NO')
    else:
        print('No')
else:
    print('NO')
