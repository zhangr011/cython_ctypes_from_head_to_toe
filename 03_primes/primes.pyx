
def primes(int nb_primes):
    cdef int n, i, len_p
    cdef int p[1000]
    if nb_primes > 1000:
        nb_primes = 1000

    len_p = 0
    n = 2
    while len_p < nb_primes:
        for i in p[:len_p]:
            if n % i == 0:
                break
        # If no break occured in the loop
        else:
            p[len_p] = n
            len_p += 1
        n += 1

    # return the python list
    return [prime for prime in p[:len_p]]


def primes_py(nb_primes):
    p = []
    n = 2
    len_p = 0
    while len_p < nb_primes:
        for i in p:
            if n % i == 0:
                break
        else:
            p.append(n)
            len_p += 1
        n += 1
    return p
