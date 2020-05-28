#Tyler Henn CSCI 379
from socket import *

serverName = '192.168.0.68'
serverPort = 12000
serverAddress = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect(serverAddress)

message = input("Input lowercase sentence: ")
clientSocket.send(message.encode())

modMessage = clientSocket.recv(2048).decode()

printInfo = "From server {}: {}".format(serverName, modMessage)
print(printInfo)

clientSocket.close()
