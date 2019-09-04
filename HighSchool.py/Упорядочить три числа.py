a, b, c = int(input()), int(input()), int(input())

if a >= b and a >= c:
    if b >= c:
        print(c, b, a)
    elif c > b:
        print(b, c, a)

elif c >= b and c >= a:
    if b >= a:
        print(a, b, c)
    elif a > b:
        print(b, a, c)
elif b >= a and b >= c:
    if a > c:
        print(c, a, b)
    elif c >= a:
        print(a, c, b)
