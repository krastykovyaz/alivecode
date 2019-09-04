h = int(input())
a = int(input())
b = int(input())
if b < a or h > b:
    if a > h:
        print(a)
    else:
        print(h)
else:
    print(b)
