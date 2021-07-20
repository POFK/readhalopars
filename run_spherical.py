#!/usr/bin/env python
# coding=utf-8

import numpy as np
import os

a=np.load('/data/dell4/userdir/maotx/Abell/halocat/halocat_selected.npy')
print a.dtype
print a.shape
rank=np.argsort(a['Halo_M_Crit200'])[::-1]
a=a[rank]
print a
Rad=60
def run(i=0):
    s=a[i]
    SimNum=i
    Sx=s['SubPos_x']
    Sy=s['SubPos_y']
    Sz=s['SubPos_z']
    Mrank=i
    print Sx,Sy,Sz,Rad,Mrank
    os.system("./run %d %f %f %f"%(Mrank, Sx,Sy,Sz))
[run(i) for i in np.arange(19,a.shape[0])]    
#run(0)

