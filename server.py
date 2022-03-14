# # first of all import the socket library
# import socket            
 
# # next create a socket object
# s = socket.socket()        
# print ("Socket successfully created")
 
# # reserve a port on your computer in our
# # case it is 12345 but it can be anything
# port = 12345               
 
# # Next bind to the port
# # we have not typed any ip in the ip field
# # instead we have inputted an empty string
# # this makes the server listen to requests
# # coming from other computers on the network
# s.bind(('', port))        
# print ("socket binded to %s" %(port))
 
# # put the socket into listening mode
# s.listen(5)    
# print ("socket is listening")           
 
# # a forever loop until we interrupt it or
# # an error occurs
# while True:
 
# # Establish connection with client.
#   c, addr = s.accept()    
#   print ('Got connection from', addr )
 
#   # send a thank you message to the client. encoding to send byte type.
#   c.send('Thank you for connecting'.encode())
 
#   # Close the connection with the client
#   c.close()
   
#   # Breaking once connection closed
#   break
#-------------------------------------------------------------------------------------------------


# from socket import *
# serverPort = 12000
# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind(('',serverPort))
# serverSocket.listen(1)
# print('The server is ready to receive')
# while 1:
#     connectionSocket, addr = serverSocket.accept()
#     sentence = connectionSocket.recv(1024)
#     Sentence = sentence.decode('UTF-8')
#     capitalizedSentence = sentence.upper()
#     connectionSocket.send(capitalizedSentence)
    
# connectionSocket.close()
send2 = ""
send1 = ""
send3 = ""
dest=0
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def getSolutionFor2(self, dist,src):
        global send2
        global send3
        send2 = "Vertex          Distance from Source\n"
        for node in range(self.V):
            if(src==node):
                send3="source - "+str(node)+" destinnation - "+str(dest)+"\nMininmum distance - "+str(dist[dest])
            send2 = send2 + str(node) + "          " + str(dist[node]) + "\n"
            print(send2)

        # for node in range(self.V):
        #     send1=send1+str(node)
        #     for ver in range(self.V):
        #         send1=send1+str(dist[ver])
        #     send1=send1+"\n"           
    
        
 
    def minDistance(self, dist, sptSet):
 
        min = 1e7

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.getSolutionFor2(dist,src)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    # print(sentence,sentence[-2])
    l = sentence.split()
    l = [int(i) for i in l]
    print(int(l[-1]))
    if(int(l[-1])==1):
        g.dijkstra(0)
        sentence = bytes(send1, 'utf-8')
        connectionSocket.send(sentence)  #To be worked upon
    elif(int(l[-1])==2):
        g.dijkstra(l[0])
        send2 = bytes(send2, 'utf-8')
        connectionSocket.send(send2)
    elif(int(l[-1])==3):
        dest = l[1]
        g.dijkstra(l[0])
        sentence = bytes(send3, 'utf-8')
        connectionSocket.send(sentence)  #done
    else:
        sentence = bytes("Invalid input", 'utf-8')
        connectionSocket.send(sentence)
    
    
connectionSocket.close()