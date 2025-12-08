import socket
s = socket.socket()
s.connect(("192.168.20.27", 1883))
s.send(b"hola")
s.close()