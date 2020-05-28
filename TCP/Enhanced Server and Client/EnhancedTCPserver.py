#!/usr/bin/python3
#Tyler Henn CSCI379
from socket import *
import sys

def get_Host_name_IP():
    try:
        host_name = gethostname()
        host_ip = gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")
get_Host_name_IP()

serverSocket = socket()#creates the socket
print("Socket created successfully")

serverPort = 12345

serverSocket.bind(('', serverPort))#connects to the port
print("The socket binded to %s" %(serverPort))

serverSocket.listen(5)#listens for incoming clients

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Got connection from", addr)

    input = connectionSocket.recv(1024).decode()#converts back to a string
    message = connectionSocket.recv(1024).decode()#converts back to a string
    capSentence = message.upper()#changes the message to uppercase letters
    lowerSentence = message.lower()#changes the message to lowercase letters
    sen_rev = " ".join(message.split()[::-1])#reverses the message of longer then 2 words.
    thank = "Thank you for connecting."

    if input == "upper":
        connectionSocket.send(capSentence.encode())#encode converts message into bytes, similar to str()
    elif input == "lower":
        connectionSocket.send(lowerSentence.encode())#encode converts message into bytes, similar to str()
    elif input == "reverse":
        connectionSocket.send(sen_rev.encode())#encode converts message into bytes, similar to str()

    connectionSocket.send(thank.encode())#encode converts message into bytes, similar to str()
    connectionSocket.close()
