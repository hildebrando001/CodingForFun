# The same method in the same memory space
import threading

def hello():
    for x in range(50):
        print("Hello")

t1 = threading.Thread(target=hello)
t1.start()

print("This text comes first")

t1.join() # Whaits until the thread finish to run next code lines

print("This text comes latter")
