import socket # Lower level of network connection

# UDP is faster than TCP # Using UDP you may loose some data
# TCP is more trustable but slower than UDP 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET     = Internet socket 
# SOCK_STREAM = TCP socket
# SOCK_DGRAM  = UDP socket

s.bind(("127.0.0.1", 55555))
s.listen() # Put socket in the listening mode

while True:
    client, address = s.accept() # accept() is the method you'll gonna use to client connects to the server
    print(f"connected to {address}")
    client.send("You are connected!".encode()) # Send an encoded message
    client.close() # We allways close after sendding the message, so we do not have a unlimited clients

