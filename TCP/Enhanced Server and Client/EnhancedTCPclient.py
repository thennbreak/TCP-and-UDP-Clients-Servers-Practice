#!/usr/bin/python3
#Tyler Henn CSCI 379
from socket import *
import sys

serverName = (sys.argv[1] if len(sys.argv) > 1 else "localhost")
serverPort = int(sys.argv[2]) if len (sys.argv) > 1 else 12346
serverAddress = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)#creates the socket
clientSocket.connect(serverAddress)#connects to the server

message = input("Input message: ")
input = input("Input lower for lowercase response. Or input upper for uppercase response.  Or input reverse for reversed response: ")

clientSocket.send(input.encode())#encode converts message into bytes, similar to str()
clientSocket.send(message.encode())#encode converts message into bytes, similar to str()



modMessage = clientSocket.recv(2048).decode()#converts back to a string

printInfo = "From server {}: {}".format(serverName, modMessage)
print(printInfo)

thankyou = clientSocket.recv(2048).decode()#converts back to a string
print(thankyou)
