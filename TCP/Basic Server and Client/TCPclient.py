#!/usr/bin/python3
#Tyler Henn CSCI 379
from socket import *

serverName = "localhost"#IP
serverPort = 12002
serverAddress = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverAddress)

message = input("Input lowercase sentence: ")
clientSocket.send(message.encode())#encode converts message into bytes, similar to str()


modMessage = clientSocket.recv(2048).decode()#converts back to a string

printInfo = "From server {}: {}".format(serverName, modMessage)
print(printInfo)

clientSocket.close()
