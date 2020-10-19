#!/bin/python
q = int(raw_input())
def cm(x,y,z) :
    cm1=z-x
    if(cm1<0):
        cm1=cm1*(-1)
    cm2=z-y
    if(cm2<0):
        cm2=cm2*(-1)
    if(cm1<cm2):
        print("Cat A")
    if(cm2<cm1):
        print("Cat B")
    if(cm1==cm2):
        print("Mouse C")
for i in range(q):
    xyz = raw_input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    rslt= cm(x,y,z)
    
