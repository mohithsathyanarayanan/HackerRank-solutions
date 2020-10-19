arr=map(int,raw_input().split())
min_sum=0
max_sum=0
x=len(arr)
arr.sort()
for i in range(0,x-1) :
    min_sum=min_sum + arr[i]
for i in range(1,len(arr)) :
    max_sum=max_sum+arr[i]

print min_sum,max_sum    

