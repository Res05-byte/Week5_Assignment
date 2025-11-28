# make cffi module
from cffi import FFI
ffi = FFI()

# note: declare fn
ffi.cdef("int dot(int* a, int* b, int n);")

# note: load file
lib = ffi.dlopen("./libdot.so")
