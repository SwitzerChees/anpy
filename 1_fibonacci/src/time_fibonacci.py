from naive_fibonacci import fib as fib
from advanced_fibonacci import fib as fib_iter
import time

# Gib die durchschnittliche Laufzeit
# in Mikrosekunden für die
# rekursive Implementation zurück
def time_fib(n, periods = 10000):
    start = time.time()
    for i in range(0, periods):
        fib(n)
    end = time.time()
    return (end - start) / periods * 1000 * 1000

# Gib die durchschnittliche Laufzeit
# in Mikrosekunden für die
# iterative Implementation zurück
def time_fib_iter(n, periods=10000):
    start = time.time()
    for i in range(0, periods):
        fib_iter(n, fromCache=False)
    end = time.time()
    return (end - start) / periods * 1000 * 1000

    