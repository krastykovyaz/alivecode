def MinDivisor(n):
    if n ** 0.5 <= n:
        if n % 2 == 0:
            print('2')
        elif n % 3 == 0:
            print('3')
        else:
            print(n)
    return


MinDivisor(int(input()))
