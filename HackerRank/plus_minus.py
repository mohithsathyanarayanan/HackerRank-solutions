from __future__ import division
n=int(input())
k=list()
f=list()
for i in range(0,1):
    k=map(int, raw_input().split())
p=0
w=0
z=0
for i in range(0,n):
    if(k[i]<0):
        w=w+1
    if(k[i]>0):
        p=p+1
    if(k[i]==0):
        z=z+1
pf=p/n
nf=w/n
if(z!=0):
    zf=z/n
else :
    zf=0.0000000    
print(pf)
print(nf)
print(zf) 
