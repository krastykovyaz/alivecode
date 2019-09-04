def hanoi(n, fr, spare, to):
    if n == 1:
        print(n, fr, to)
    else:
        hanoi((n - 1), to, spare, fr)
        print(n, fr, spare)
        hanoi((n - 1), spare, fr, to)


hanoi(int(input()), 1, 2, 3)
