k = int(input()) #meat balls on the plate
m = int(input()) #minute
n = int(input()) #meat balls
if k < n:
    onetime = n / k
    total = onetime * m * 2
    print(total)
else:
    total = k * m * 2
    print(total)
