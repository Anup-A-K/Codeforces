n = int(input())
s = input()
i = 0
while i < n-1:
    if s[i] > s[i+1]:
        break
    i += 1
print(s[:i],s[i+1:],sep='')
