
import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
s=map(int,raw_input().split())
n=s[0]
k=s[1]
l=map(int,raw_input().split())
l.sort()
l.reverse()
if(k>=l[0]):
    ans=0
if(k<l[0]):
    ans=l[0]-k
print(ans)

