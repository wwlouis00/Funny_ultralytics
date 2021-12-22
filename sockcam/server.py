#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
HOST = '127.0.0.1'
PORT = 8888

s.listen(5)

while True:
          try:
                    clientsocket, address = s.accept()
          except print(0):
              pass
          
          print(f"Connect from  {address} has been established!")
          clientsocket.send(bytes("Welcome to the server!","utf-8"))
