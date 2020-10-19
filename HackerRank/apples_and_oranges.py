import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
c1=0
c2=0
st = map(int,raw_input().split())

s = st[0]

t = st[1]

ab = map(int,raw_input().split())

a = ab[0]

b = ab[1]

mn = map(int,raw_input().split())

m = mn[0]

n = mn[1]

apples = map(int, raw_input().split())

oranges = map(int, raw_input().split())

for i in range(m):
    apples[i]=a+apples[i]

for i in range(n):
    oranges[i]=b+oranges[i]

for i in range(m):
    if (s<=apples[i] and apples[i]<=t):
        c1=c1+1
for i in range(n):
    if(s<=oranges[i] and oranges[i]<=t):
        c2=c2+1
print(c1)
print(c2)
