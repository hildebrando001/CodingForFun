n = 7

fact = 1
while n > 0:
    fact = fact * n
    n -= 1
print(fact)
######################

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number
print(factorial(7))
######################

def fib(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
    return a
print(fib(10))
######################

def fibonacci(n): # Recursion are slower than regular functions
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(10))