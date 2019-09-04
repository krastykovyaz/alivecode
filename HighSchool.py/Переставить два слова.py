s = str(input())
a = s.find(' ') + 1
print(s[a:], '', end=s[:a])
