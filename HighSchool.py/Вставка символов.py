s = str(input())
if len(s) > 2:
    a = s[1:-1]
    print(s[0] + a.replace('', '*') + s[-1])
else:
    print(s)
