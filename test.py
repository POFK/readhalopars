import os
import numpy as np
from cffi import FFI
from _rhp.lib import Mill

BaseDir = "/data/inspur_disk02/Simulations/Millennium/"
snap_path = os.path.join(BaseDir, "snapdir_063")
post_path = os.path.join(BaseDir, "postproc_063")

ffi = FFI()

def readgroup(snap_path, post_path, npar, group_rank):
    psnap = ffi.new("char[]", snap_path.encode('ascii'))
    ppost = ffi.new("char[]", post_path.encode('ascii'))
    pos = np.zeros(shape=[npar * 3], dtype=np.float32)
    Sxyz = np.zeros(shape=[3], dtype=np.float32)
    MostboundId = np.zeros(shape=[1], dtype=np.int64)
    ppos = ffi.cast("float *", pos.ctypes.data)
    psxyz = ffi.cast("float *", Sxyz.ctypes.data)
    pmb = ffi.cast("long long *", MostboundId.ctypes.data)
    group_len = Mill(psnap, ppost, group_rank, ppos, psxyz, pmb)
    assert group_len == npar 
    return pos, Sxyz, MostboundId

if __name__ == "__main__":
    Gnum=[4386162,3831945,2162498,2117511,2117472,1838697,1838697] # group particle number
    N=1  # group rank
    pos, centre, mb = readgroup(snap_path, post_path, Gnum[N], N)
    print(centre)
    print(mb)
