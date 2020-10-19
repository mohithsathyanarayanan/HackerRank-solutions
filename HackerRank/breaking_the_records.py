#!/bin/python

import math
import os
import random
import re
import sys

n= input()
s= map(int,raw_input().split())
hc=0
lc=0
phs=s[0]
pls=s[0]
for i in range(1,n):
    if(s[i]<pls):
        lc=lc+1
        pls=s[i]
    if(s[i]>phs):
        hc=hc+1
        phs=s[i]
print hc,lc

