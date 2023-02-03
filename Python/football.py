a=(input())
b=a.count('0000000')
c=a.count('1111111')
if b>0 or c>0:
    print('YES')
else:
    print('NO')
