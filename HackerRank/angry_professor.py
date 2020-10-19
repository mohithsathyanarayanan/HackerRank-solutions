
import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
p=input()
def tf(k, a):
    s = 0 
    for i in a:
        if i<1:
            s+=1
    return "YES" if s<k else "NO"

for i in range(p):
    nk=map(int,raw_input().split())
    n=nk[0]
    k=nk[1]
    timings=map(int,raw_input().split())
    ans=tf(k,timings)
    print(ans)
