import socket
s = socket.socket(socket.AF_UNIX)

s.connect('test.sock')
msg = s.recv(1024)
print(msg.decode("utf-8"))
