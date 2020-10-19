n=int(raw_input())
marks=list()
for i in range(n) :
    w=input()
    marks.append(w)
    
for i in range(len(marks)) :
    rm=marks[i]%5
    if marks[i]<38 :
        marks[i]=marks[i]    
    if marks[i]>=38 and marks[i]<=40 :
        marks[i]=40
    if marks[i]>40 :
        if(rm>=3) :
            d=marks[i]/5
            marks[i]=(d+1)*5
for i in range(len(marks)):
    print marks[i]
    


