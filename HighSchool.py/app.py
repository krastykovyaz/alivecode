def hanoi(n, a, b, c):
    if n == 1:
        print(n, a, c)
    else:
        hanoi((n-1), a, c, b)
        print(n, a, c)
        hanoi((n - 1), b, a, c)


hanoi(int(input()), 1, 2, 3)