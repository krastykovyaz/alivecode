s = str(input())
if s.find('h') != -1:
    a = s.find('h')
    s1 = s[::-1]
    b = len(s) - s1.find('h')
    if a != b:
        print(s[:a], end=s[b:])
    elif a == b:
        print(a)
else:
    print('')
