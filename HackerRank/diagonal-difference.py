n=input()
c=[]
for i in range(0,n):
    r=map(int,raw_input().split())
    c.append(r) 
d1 = 0
d2 = 0
for i in range(0, n): 
    d1 = d1 + c[i][i] 
    d2 = d2 + c[i][n - i - 1] 
d=0
d=d1-d2
if d<0 :
    d=d*-1
print d
