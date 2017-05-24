from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',9000))
s.listen(5)
while 1:
	c,a = s.accept()
	print "received connection from", a
	c.send("hello %s\n" %a[0])
	c.close
