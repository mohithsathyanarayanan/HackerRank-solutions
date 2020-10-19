n=input()
p=input()
fcount=0
rcount=0
if(n%2==1):
    rcount=-1
    i=1
    while(i<p):
        fcount=fcount+1
        i=i+2
    while(n>=p):
        rcount=rcount+1
        n=n-2

if(n%2==0):
    i=1
    while(i<p):
        fcount=fcount+1
        i=i+2
    while(n>p):
        rcount=rcount+1
        n=n-2
if(fcount>=rcount):
    print(rcount)
if(rcount>fcount):
    print(fcount)

