a = int(input())
b = int(input())
i = 0
while a != b:
    i += 1
    if a % 2 == 0 and a // 2 >= b:
        a /= 2
        print(':2')
    else:
        a -= 1
        print('-1')
