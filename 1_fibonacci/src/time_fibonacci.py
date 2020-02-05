from naive_fibonacci import *
import time

def time_fib(n, periods = 10000):
    start = time.time()
    for i in range(0, periods):
        fib(n)
    end = time.time()
    return str(n) +"th: " + str((end - start) / periods * 1000 * 1000) + " Microseconds"
    