#!/usr/bin/python
import socket
import sys
import os

args = sys.argv
mySocket = socket.socket()
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
myHost = '0.0.0.0'#socket.gethostbyname(socket.gethostname())
myPort = args[1]

serverSocket = socket.socket()
serverHost = "192.168.56.101"
serverPort = args[2]

print "Starting proxy -- listening on "+myHost+":"+myPort+" for "+serverHost+":"+serverPort
mySocket.bind((myHost, int(myPort)))

mySocket.listen(5)
while True:	
	c, addr = mySocket.accept()
	print "Connection from ",addr
	serverSocket.connect((serverHost, int(serverPort)))
	while True:
		#Start talking to server
		msg_back = serverSocket.recv(1024)
		c.send(msg_back)
		msg_to = c.recv(1024)
		print str(addr[0])+":"+str(addr[1])+" sent \""+msg_to+"\""
		serverSocket.send(msg_to)
	c.close
