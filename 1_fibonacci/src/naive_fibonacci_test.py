from naive_fibonacci import * 

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
# RuntimeError: maximum recursion depth exceeded in cmp
print(fib(999))