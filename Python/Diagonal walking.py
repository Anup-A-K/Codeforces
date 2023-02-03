x=int(input())
s=input()
c = 0
i = 0
while i < x-1:
  if s[i]== 'U' and s[i+1] == 'R':
    c += 1
    i += 2
  elif s[i] == 'R' and s[i+1] == 'U':
    c += 1
    i += 2
  else :
    i += 1
print(x-c)
