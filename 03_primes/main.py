from primes import primes, primes_py
from utilities import time_it

@time_it
def primes_c(n):
    return primes(n)

@time_it
def primes_python(n):
    return primes_py(n)


if __name__ == '__main__':
    primes_c(1000)
    primes_python(1000)
