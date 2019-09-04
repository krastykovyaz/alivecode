x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 0 < x1 and 0 < x2 and 0 < y1 and 0 < y2:
    print('YES')
elif x1 < 0 and 0 > x2 and 0 < y1 and 0 < y2:
    print('YES')
elif 0 > x1 and 0 > x2 and 0 > y1 and 0 > y2:
    print('YES')
elif 0 < x1 and 0 < x2 and 0 > y1 and 0 > y2:
    print('YES')
else:
    print('NO')
