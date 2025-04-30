##########################################################################
""" 
TCPServer.py      

816019037 - Brandon Rampersad                         
           
"""

from socket import *

serverPort = 12031

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))

serverSocket.listen(1)


print ("The Capitalization Server running over TCP is ready to receive- ")

connectionSocket, addr = serverSocket.accept()

num=0

while num<4:
#receiving message from client
    message = connectionSocket.recv(1024)
    print ("Received From Client: ", message.decode())
#converting to capital	 
    capitalizedMessage = message.upper()
    connectionSocket.send(capitalizedMessage)
# output to console it was sent back to the client 
    print ("Sent back to Capitalised string to client")
    num+=1
    
# close the TCP connection; the welcoming socket continues
connectionSocket.close()    
	 

'''

'''
