def IsPrime(n):
    dlt = 2
    while dlt * dlt <= n and n % dlt != 0:
        dlt += 1
    return dlt * dlt > n

a = IsPrime(int(input()))
if a:
    print('Yes')
else:
    print('No')
