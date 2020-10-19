#!/bin/python

import math
import os
import random
import re
import sys
nk= map(int,raw_input().split())

n=nk[0]

k=nk[1]

arr=map(int,raw_input().split())

counter=0

for i in range(n) :
    for j in range(n):
        comp=j
        if(comp>i):
            if((arr[i]+arr[comp])%k==0):
                counter=counter+1
print(counter)
