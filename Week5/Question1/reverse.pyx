def rev_str(s):
    cdef int i
    cdef int n = len(s)
    cdef list out = []

    # note: loop from end
    for i in range(n - 1, -1, -1):
        out.append(s[i])

    return "".join(out)