#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
n=input()
s=raw_input()
pl=0
l=[0]
counter=0

for i in range(len(s)):
    if(s[i]=="U"):
        pl=pl+1
        l.append(pl)
    if(s[i]=="D"):
        pl=pl-1
        l.append(pl)


for i in range(len(l)-1):
    if(l[i]==0):
        if(l[i+1]==-1):
            counter=counter+1

print counter

