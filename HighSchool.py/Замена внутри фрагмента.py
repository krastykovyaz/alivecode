s = str(input())
a = s.find('h') + 1
b = s.rfind('h')
c = s[:a] + s[a:b].replace('h', 'H')
print(c, end=s[b:])
