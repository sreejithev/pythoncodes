from socket import *
client_socket = socket(AF_INET,SOCK_DGRAM)
data ="hello"
addr = ('localhost',15000)
client_socket.sendto(data,addr)


