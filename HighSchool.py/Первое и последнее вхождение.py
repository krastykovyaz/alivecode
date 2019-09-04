s = str(input())
if s.find('f') != -1:
    a = s.find('f')
    s1 = s[::-1]
    b = len(s) - s1.find('f') - 1
    if a != b:
        print(a, b)
    elif a == b:
        print(a)
else:
    print('')
