########### EVENT ###########
import threading
import time

event = threading.Event() # Create an event # We can trigger this event or we can wait for this event 

def myfunction():
    print("Waiting for event to trigger...\n")
    event.wait() # Event watting to be setted/trigger
    print("Performing action XYZ now...")


t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you want to trigger the event? (y/n) ")
if x == "y":
    event.set() # set means trigger the event


##### DEAMON THREAD ##### Nothing waits for deamon threads, cuz it is running in the background
# Deamon threads are waitting in the background script terminate, evendown it still running
# We use deamon threads for constantly redding information from files and web API. And soon 
# everything is done, we just terminate the script and terminate de deamon thread. 

# Here we'll have two threads. One will read the information from the text file,
# where the other tread will print that information out on the screen

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f: # Open a file as read only
            text = f.read() # Load file content into the variable
        time.sleep(3)

def printLoop():
    for x in range(10):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()