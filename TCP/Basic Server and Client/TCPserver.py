#!/usr/bin/python3
#Tyler Henn CSCI379
from socket import *

serverPort = 12002
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    capSentence = sentence.upper()
    connectionSocket.send(capSentence.encode())
    connectionSocket.close()
