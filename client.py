# # Import socket module
# import socket            
 
# # Create a socket object
# s = socket.socket()        
 
# # Define the port on which you want to connect
# port = 12345               
 
# # connect to the server on local computer
# s.connect(('127.0.0.1', port))
 
# # receive data from the server and decoding to get the string.
# print (s.recv(1024).decode())
# # close the connection
# s.close()    
#----------------------------------------------------------------------------------------------------
from socket import *
serverName = 'localhost' 
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('choose what to do: \n Enter 1 to get data \n Enter 2 get the time taken to travel to all places from source \n Enter 3 to get minimum time to go form source to destinaion\n Enter here: ')


if(sentence == '2'):
    source = input("Enter the source: ")
    sentence = source+" "+sentence
    print(sentence)
elif(sentence == '3'):
    source = input("Enter the source")
    dest = input("Enter the dest")
    sentence = source+" "+dest+" "+sentence
sentence = bytes(sentence, 'utf-8')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
modifiedSentence = str(modifiedSentence)
l = modifiedSentence.split("\\n")
#print(l)
for i in l:
    print(i)

#print('From Server: ',str(modifiedSentence))
clientSocket.close()