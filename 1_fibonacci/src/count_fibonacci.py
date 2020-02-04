from naive_fibonacci import * 

def count_rec(fiCheck):
    n = 1
    while True:
        fi = fib(n-1)
        if fi > fiCheck:
            return "Error: No Fibonacci number"
        elif fi == fiCheck:
            return n
        n += 1
        pass