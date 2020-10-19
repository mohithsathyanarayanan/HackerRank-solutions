n=2
a=0
b=0
for i in range(0,1):
    r1=map(int,raw_input().split())
    r2=map(int,raw_input().split())
if r1[0]>r2[0] :
    a=a+1
if r1[0]<r2[0] :
    b=b+1
if r1[1]>r2[1] :
    a=a+1
if r1[1]<r2[1] :
    b=b+1
if r1[2]>r2[2] :
    a=a+1
if r1[2]<r2[2] :
    b=b+1
print a,b
