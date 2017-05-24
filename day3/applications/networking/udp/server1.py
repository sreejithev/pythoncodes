from socket import *
server_socket = socket(AF_INET,SOCK_DGRAM)
server_socket.bind(('localhost',15000))
data_len = 1000
s = server_socket.recvfrom(data_len)
print s



