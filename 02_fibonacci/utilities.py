# encoding: UTF-8

from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__} took {t2 - t1} seconds")
        return result
    return measure_time
