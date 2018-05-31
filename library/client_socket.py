import socket

c = socket.socket()
c.connect(("localhost",2000))
data = c.recv(100)
print(data.decode())

