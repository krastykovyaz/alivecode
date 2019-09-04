a = int(input())
b = int(input())
if a < b:
    a, b = b, a
el = int(input())
while el != 0:
    if el > a:
        a, b = el, a
    elif el > b:
        b = el
    el = int(input())
print(b)
