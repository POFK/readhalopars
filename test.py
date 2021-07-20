import os
import numpy as np
from cffi import FFI
from _rhp.lib import Mill


ffi = FFI()

class ReadGroupParticle(object):
    def __init__(self, BaseDir=''):
        self.base = BaseDir
        self.spath = os.path.join(BaseDir, "snapdir_063")
        self.ppath = os.path.join(BaseDir, "postproc_063")

    def getpath(self, path):
        ffipath = ffi.new("char[]", path.encode('ascii'))
        return ffipath

    def readgroup(self, npar, group_rank):
        psnap = self.getpath(self.spath)
        ppost = self.getpath(self.ppath)
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
    BaseDir = "/data/inspur_disk02/Simulations/Millennium/"
    Gnum=[4386162,3831945,2162498,2117511,2117472,1838697,1838697] # group particle number
    rank = np.range(len(Gnum)) + 1
    rgp = ReadGroupParticle(BaseDir = BaseDir)
    for i in range(len(Gnum)):
        pos, centre, mb = rgp.readgroup(snap_path, post_path, Gnum[N], N)
        print(centre)
        print(mb)
