import socket
with socket.socket(socket.AF_UNIX) as s:
  s.connect('test.sock')
  s.sendall(b'free -m')
  data = s.recv(1024)
  print(data.decode("utf-8"))

# s.connect('test.sock')
# msg = s.recv(1024)

