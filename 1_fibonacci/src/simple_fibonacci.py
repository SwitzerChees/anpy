def fib(n, fiPrev = 0, fi = 1):
    if fiPrev == 0:
        if n > 0:
            n -= 1
        else:
            return fiPrev
    if n == 0:
        return fi
    return fib(n - 1, fi, fi + fiPrev)
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