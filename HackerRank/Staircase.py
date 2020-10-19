n=input()
a=" "
b="#"
j=a+b
k=1
for i in range(n-1,-1,-1):
    j= a*i + b*k
    k=k+1
    print(j)
