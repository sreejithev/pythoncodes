from socket import *
s = socket (AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',8888))
s.send("hello,world")
data = s.recv(10000)
s.close()
