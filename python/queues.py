import queue # Tell whish element will be free to be used by some thread

q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q.put(number) # Takes all the number and put into q
print(q.get())    # Print the next free for use element # Will print 10
print(q.get())    # Very userfull when I have a tone of methods tying to access the same elements list  # Will print 20

######################################################
qu = queue.LifoQueue() # Last in first out

numberslist = [1, 2, 3, 4, 5, 6, 7]

for x in numberslist:
    qu.put(x)
print(qu.get())  # It will return 7, the last element of the list qu

######################################################
qq = queue.PriorityQueue() # Takes the priority element

qq.put((2, "Hello world")) # Lowest number has the hightest priority
qq.put((10, 456))
qq.put((0, "zero"))
qq.put((20, 5))

while not qq.empty():
    print(qq.get())