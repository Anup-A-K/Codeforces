A = int(input())
B = int(input())
tA = abs(A-B)//2
tB =abs (A-B)-tA
tA= tA*(tA+1)//2
tB=tB*(tB+1)//2
tiredness = tA + tB
print(tiredness)
