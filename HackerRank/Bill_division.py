nk=map(int,raw_input().split())
lst=map(int,raw_input().split())
bill=input()
lst1=list()
c=0
for i in range(nk[0]): 
    lst1.append(lst[i])
del lst1[nk[1]]
for i in range(nk[0]-1) :
    c=c+lst1[i]
c=c/2    
if(bill==c):
    print("Bon Appetit")
if(bill!=c):
    actual=bill-c
    print(actual)
