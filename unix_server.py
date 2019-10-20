import socket 
s = socket.socket(socket.AF_UNIX)

s.bind('test.sock')

s.listen(5)

while True:
  clt, adr = s.accept()
  print('Connected')
  clt.send(bytes("Socket programming in python", "utf-8"))
