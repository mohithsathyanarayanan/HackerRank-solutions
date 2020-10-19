#!/bin/python
from __future__ import division


import math
import os
import random
import re
import sys
def isInt(x):
# to check n is int or not.if n is an integer then n%1=0
    if x%1 == 0:
        return(True)
    else:
        return(False)

z=map(int,raw_input().split())
x1=z[0]
v1=z[1]
x2=z[2]
v2=z[3]
if((v2-v1)==0):
    print("NO")
if((v2-v1)!=0):
    n=(x1-x2)/(v2-v1)
    if(v1==v2 and x1!=x2):
        print("NO")
    if(isInt(n) is True):
        if(n>0):        
            print("YES")
    if(n<0 or isInt(n) is False):
        print("NO")
