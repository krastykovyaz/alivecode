a = int(input())
if a == 0:
    print(0)
else:
    f0 = 0
    f1 = 1
    i = 1
    while f1 <= a:
        if f1 == a:
            print(i)
            break
        f0, f1 = f1, f1 + f0
        i += 1
    else:
        print(-1)
