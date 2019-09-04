s = str(input())
b = s.find('f')
if b == -1:
    print(-2)
else:
    i = 0
    n = 0
    while n != 2:
        a = s.find('f', i)
        i = s.find('f', i) + 1
        n += 1
    if n == 1:
        print(-1)
    else:
        print(a)
