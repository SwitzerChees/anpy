def fib(n, fiPrev = 0, fi = 1):
    # Abbruchbedingung
    if n <= 1:
        # Prueft ob 0te oder 1te Fibonacci Folge gefordert
        return fiPrev if fiPrev == 0 and n == 0 else fi
    # Rekursiver Aufruf
    return fib(n - 1, fi, fi + fiPrev)