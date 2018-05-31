import socket

s = socket.socket() # Create a socket object
port = 2000
s.bind(("localhost", port))

s.listen(5)
# Now, wait for client connection.
while True:
   # Establish connection with client.
   # It returns connection and address of client
   c, addr = s.accept()
   c.send("Hello".encode())
   c.close()
