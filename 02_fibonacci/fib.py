# encoding: UTF-8

from utilities import time_it
import fibonacci

@time_it
def fib_py(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = a + b, a
    return a

@time_it
def fib_c(n):
    return fibonacci.fib(n)

if __name__ == '__main__':
    n = 10000
    fib_py(n)
    fib_c(n)
