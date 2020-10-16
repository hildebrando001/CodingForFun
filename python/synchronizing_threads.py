import threading
import time
"""
x = 8192
lock = threading.Lock() # Make it possible to lock a resource

def double():
    global x, lock # The variable only can be locked once
    lock.acquire() # Acquire this lock, if it is not already locked
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(0.5)
    print("Reached the maximum!")
    lock.release() # When the maximum value is reached, it releases the lock


def halve():
    global x, lock # Will lock the thread until reach the 
    lock.acquire() 
    while x > 1:
        x /= 2
        print(x)
        time.sleep(0.5)
    print("Reached the minimum!")
    lock.release()

# One thread will be deviding the number by two, the other one again doubleing it.
# Só this is an endless loop... if there is not a lock
t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)
t1.start()
t2.start()

"""

#################### SEMAPHORE ####################
# Do not lock the resource completely, but limit the access to resource
semaphore = threading.BoundedSemaphore(value=5) # Specify the maximum allowed value. "five access in this case"

def access(thread_number):
    print(f"{thread_number} is trying to access!")
    semaphore.acquire()
    print(f"{thread_number} was granted access!")
    time.sleep(10)
    print(f"{thread_number} is now releasing")
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)