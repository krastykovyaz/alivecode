def soch(n, k):
    if k == n or k == 0:
        return 1
    return soch(n - 1, k) + soch(n - 1, k - 1)


print(soch(int(input()), int(input())))
