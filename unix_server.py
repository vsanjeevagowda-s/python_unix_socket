import socket 
import os
from subprocess import check_output
from shlex import split

with socket.socket(socket.AF_UNIX) as s:
    try:
      os.remove(os.path.dirname(__file__) +"/test.sock")
    except:
      print("An error occurred")
    s.bind("test.sock")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected')
        while True:
            data = conn.recv(1024)
            # conn.sendall(data)
            print('[ data ]', data)
            resp = check_output(split(data.decode("utf-8")))
            conn.sendall(resp)
            