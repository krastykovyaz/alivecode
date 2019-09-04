n = int(input())
k = 0
seqSum = 1
while seqSum <= n:
    a = seqSum ** 2
    seqSum += 1
    k += a
print(k)
