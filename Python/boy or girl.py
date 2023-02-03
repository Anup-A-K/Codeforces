from collections import Counter
s=input()
a=Counter(s)
b=len(a)
if b%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
