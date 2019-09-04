a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
if b1 == a2 and a3 == b2:
    print(0)
elif b1 < a2 and a3 == b2:
    print(1)
elif b1 > a2 and a3 == b2:
    print(1)
elif b1 == a2 and a3 > b2:
    print(3)
elif b1 == a2 and a3 < b2:
    print(3)

elif b1 > a2 and b2 < a3:
    print(0)
elif b1 > a2 and a3 < b2:
    print(1)
elif b1 < a2 and a3 < b2:
    print(1)
elif b1 > a2 and a3 > b2:
    print(3)
elif b1 < a2 and b2 < a3:
    print(3)
else:
    print(-1)
