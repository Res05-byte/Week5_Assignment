from cffi import FFI
ffi = FFI()

# note: declare fn
ffi.cdef("int dot(int* a, int* b, int n);")
lib = ffi.dlopen("./libdot.so")

# note: make arrays
a = [1, 2, 3]
b = [4, 5, 6]

# note: convert to C array
ca = ffi.new("int[]", a)
cb = ffi.new("int[]", b)

n = len(a)

# call
ans = lib.dot(ca, cb, n)

print(ans)