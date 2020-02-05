import time

# Globaler Cache fuer bereits
# berechnete Fibonacci Zahlen
cache = {0: 0}

def fib(n, fromCache=True):
    # Prueft ob bereits im Cache vorhanden
    if fromCache and n in cache:
        return cache[n]
    fi = 1
    fiPrev = 0
    if n == 0:
        return fiPrev
    # Iteratives Berechnen um nicht an
    # die maximale Rekursionstiefe
    # zu kommen
    for i in range(1, n):
        fiNext = fiPrev + fi
        fiPrev = fi
        fi = fiNext
    # Neuen Wert in den Cache
    cache[n] = fi
    return fi

def time_fib(n, periods=10000):
    start = time.time()
    for i in range(0, periods):
        fib(n, fromCache=False)
    end = time.time()
    return str(n) +"th: " + str((end - start) / periods * 1000 * 1000) + " Microseconds"
