# sum of squares fn
def sum_sq(int n):
    cdef int i
    cdef int total = 0

    # note: add squares
    for i in range(1, n + 1):
        total += i * i

    return total