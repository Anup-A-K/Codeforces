text=input()
count=0
n=len(text)
for i in range(n):
    if text[i]!=text[n-i-1]:
        count=count+1
if n%2==0 and count/2==1 :
    print("YES")
elif n%2==1 and count/2<=1 :
    print("YES")
else:
    print("NO")
