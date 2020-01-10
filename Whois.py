#!/usr/share/python
#Criado Por DKVIZOWNA
#Github:Github.com/dkvizowna
# Data:07/11/2020

import socket,sys
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.160.2.3",43))
s.send(sys.argv[1]+'\r\n')
chegou = s.recv(1024)
print chegou