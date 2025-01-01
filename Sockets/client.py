import socket

c = socket.socket()

print("Client Socket Created")

c.connect(('localhost',9999))

name = input("ENter your name")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())