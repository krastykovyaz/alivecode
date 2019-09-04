now = int(input())
newMax = now
while now != 0:
    if now > newMax:
        newMax = now
    now = int(input())
print(newMax)
