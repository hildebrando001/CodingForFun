#Fibonacci with Generator

# def fib(num):
#     a,b = 0,1
#     for i in range(0, num):
#         a, b = b, a + b
#         yield (f"{a}")

# f = fib(4)       

# for i in f:
#     print(i)

############################
def gen(n):
    for i in range(n):
        yield i**2

g = gen(5)
for i in g:
    print(i)
############################
# def gene(n):
#     for i in range(n):
#         yield i**2

# g = gene(10000)
# print(next(g))
# print(next(g))
# print(next(g))
############################
import sys

def gen2(n):
    for i in range(n):
        yield i**2
g2 = gen2(10000)
x  = [i**2 for i in range(10000)]

print("*"*20)
print(f"Size of the list with generator: {sys.getsizeof(g2)}")
print(f"Size of the direct list:         {sys.getsizeof(x)}")

