a = int(input())
b = int(input())
d = 0 ** (a % b)
print(d * 'Yes', (1 - d) * 'No', sep='')
