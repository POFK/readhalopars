import os, sys
from cffi import FFI

os.chdir(os.path.dirname(sys.argv[0]) or ".")

ffibuilder = FFI()

with open(os.path.join(os.path.dirname(__file__),"groupstuff.h")) as f:
    ffibuilder.cdef(f.read(), override=True)

ffibuilder.set_source("rhp._lib",  # name of the output C extension
    "#include <groupstuff.h>",
    sources=['rhp/mygroupstuff.c','rhp/show_group_py.c'],   
    libraries=['m'])    # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
