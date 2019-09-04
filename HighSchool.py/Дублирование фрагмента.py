s = str(input())
a = s.find('h') + 1
s1 = s[::-1]
b = len(s) - s1.find('h') - 1
print(s[:b], end=s[a:])
