#!/bin/python
# your code goes here
c=int()
i=0
age=int(raw_input())
heights=map(int,raw_input().split())
heights.sort()
heights.reverse()
for i in range(age):
        if(heights[0]==heights[i]):
            c=c+1      
print(c)