#!/usr/bin/env python
# coding=utf-8
import ctypes
import numpy as np

Gnum=[4386162,3831945,2162498,2117511,2117472,1838697,1838697]
N=1  # group rank
so = ctypes.CDLL('./pylib.so')

pos = np.zeros(shape=[Gnum[N]* 3], dtype=np.float32)
Sxyz = np.zeros(shape=[3], dtype=np.float32)
MostboundId = np.zeros(shape=[1], dtype=np.int64)
ppos = ffi.cast("float *", pos.ctypes.data)
psxyz = ffi.cast("float *", Sxyz.ctypes.data)
pmb = ffi.cast("float *", MostboundId.ctypes.data)

Len=so.Mill(1,
        N,
        ppos,
        psxyz,
        pmb
       )
print Sxyz
print Len
print MostboundId
#a = pos.reshape([Gnum[N], 3])
#a.tofile('./data/group%d_pos.bin'%N,format='f4')
#np.save('./data/group%d_pos.npy'%N,a)
