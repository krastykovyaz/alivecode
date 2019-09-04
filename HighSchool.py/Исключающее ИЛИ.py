def xor(x, y):
    return x == 0 and y == 1 or x == 1 and y == 0


x = float(input())
y = float(input())
if xor(x, y):
    print('1')
else:
    print('0')
