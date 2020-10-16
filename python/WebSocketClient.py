import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket = SOCK_STREAM
s.connect(("127.0.0.1", 55555))
message = s.recv(1024) # Receive the message
s.close() # Close connection

print(message.decode()) # Print decoded message
