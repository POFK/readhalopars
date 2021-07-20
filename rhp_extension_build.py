import os
from cffi import FFI
ffibuilder = FFI()

with open("groupstuff.h") as f:
    ffibuilder.cdef(f.read(), override=True)

ffibuilder.set_source("_rhp",  # name of the output C extension
    r"""
    #include "groupstuff.h"
    """,
    sources=['mygroupstuff.c','show_group_py.c'],   # includes pi.c as additional sources
    libraries=['m'])    # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
