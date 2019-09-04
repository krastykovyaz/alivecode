def squad():
    n = int(input())
    if n != 0:
        squad()
        if n ** 0.5 % 1 == 0:
            global t
            t = 0
            print(n, end=' ')


t = 1
squad()
if t:
    print(0)
