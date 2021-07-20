import numpy as np
from cffi import FFI
from _rhp.lib import Mill

ffi = FFI()

Gnum=[4386162,3831945,2162498,2117511,2117472,1838697,1838697] # group particle number
N=1  # group rank

def readgroup(npar, group_rank):
    pos = np.zeros(shape=[npar * 3], dtype=np.float32)
    Sxyz = np.zeros(shape=[3], dtype=np.float32)
    MostboundId = np.zeros(shape=[1], dtype=np.int64)
    ppos = ffi.cast("float *", pos.ctypes.data)
    psxyz = ffi.cast("float *", Sxyz.ctypes.data)
    pmb = ffi.cast("long long *", MostboundId.ctypes.data)
    group_len = Mill(1, group_rank, ppos, psxyz, pmb)
    assert group_len == npar 
    return pos, Sxyz, MostboundId

pos, centre, mb = readgroup(Gnum[N], N)
print(centre)
print(mb)
