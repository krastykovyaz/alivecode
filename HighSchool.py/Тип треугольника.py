a = int(input())
b = int(input())
c = int(input())
if (c ** 2) / 2 < a ** 2 + b ** 2 < c ** 2:
    print('obtuse')
elif (a ** 2) / 2 < c ** 2 + b ** 2 < a ** 2:
    print('obtuse')
elif (b ** 2) / 2 < a ** 2 + c ** 2 < b ** 2:
    print('obtuse')
elif a ** 2 + b ** 2 == c ** 2:
    print('rectangular')
elif c ** 2 + b ** 2 == a ** 2:
    print('rectangular')
elif a ** 2 + c ** 2 == b ** 2:
    print('rectangular')
elif a ** 2 + b ** 2 > c ** 2 and a + b != c:
    if c ** 2 + b ** 2 > a ** 2 and c + b != a:
        if a ** 2 + c ** 2 > b ** 2 and a + c != b:
            print('acute')
else:
    print('impossible')
