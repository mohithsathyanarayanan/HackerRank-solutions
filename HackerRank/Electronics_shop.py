bnm=map(int,raw_input().split())
kbd=map(int,raw_input().split())
usb=map(int,raw_input().split())
c=0
sol=-1
for i in range(bnm[1]):
    for j in range(bnm[2]):
        c=kbd[i]+usb[j]
        if(c<=bnm[0]):
         if(c>sol):
            sol=c   
print(sol)
