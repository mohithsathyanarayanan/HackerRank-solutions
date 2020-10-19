

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
s=map(int,raw_input().split())
a=raw_input()
alphabet="abcdefghijklmnopqrstuvwxyz"
hl=[]
for i in range(len(a)):
    index=alphabet.find(a[i])
    height=s[index]
    hl.append(height)
hl.sort()
hl.reverse()
area=hl[0]*len(a)
print(area)
