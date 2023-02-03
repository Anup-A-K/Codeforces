n= input()+" "
a = "YES"
for i in range(len(n)-1):
    if n[i] not in "naeiou" and n[i+1] not in "aeiou":
        a = "NO"
print(a)
