def fib(n):
    # Repraesentiert fn-1
    fi = 1
    # Repraesentiert fn-2
    fiPrev = 0
    # Pseudo Fibonacci Zahl 0
    if n == 0:
        return fiPrev
    # Berechnet fiNext aus fi & fiPrev
    for i in range(1, n):
        fiNext = fi + fiPrev
        fiPrev = fi
        fi = fiNext
        pass
    # Gibt die endgueltige Fibonacci Zahl zurueck
    return fi
    pass

# Output: 0
print(fib(0))
# Output: 1
print(fib(1))
# Output: 1
print(fib(2))
# Output: 2
print(fib(3))
# Output: 3
print(fib(4))
# Output: 5
print(fib(5))
# Output: 8
print(fib(6))
# Output: 13
print(fib(7))