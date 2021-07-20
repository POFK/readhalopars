import os
import numpy as np
from cffi import FFI
from _rhp.lib import Mill

BaseDir = "/data/inspur_disk02/Simulations/Millennium/"
snap_path = os.path.join(BaseDir, "snapdir_063")
post_path = os.path.join(BaseDir, "postproc_063")

ffi = FFI()
pos = np.zeros(shape=[Gnum[N]* 3], dtype=np.float32)
Sxyz = np.zeros(shape=[3], dtype=np.float32)
MostboundId = np.zeros(shape=[1], dtype=np.int64)
ppos = ffi.cast("float *", pos.ctypes.data)
psxyz = ffi.cast("float *", Sxyz.ctypes.data)
pmb = ffi.cast("float *", MostboundId.ctypes.data)
psnap = ffi.new("char[]", snap_path)
ppost = ffi.new("char[]", post_path)

Gnum=[4386162,3831945,2162498,2117511,2117472,1838697,1838697]
N=1  # group rank

Mill(psnap, N, ppos, psxyz, pmb)

print Sxyz
print Len
print MostboundId

