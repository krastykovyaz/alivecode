def min4(a):
    i = 1
    while i < 4:
        b = int(input())
        a = min(a, b)
        i += 1
    return a

print(min4(int(input())))
