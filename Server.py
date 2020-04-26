import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((socket.gethostname(), 1235))
#AF_INET corrosponds to IPv4
#SOCK_STREAM
#(A Streaming socket



#Choose a relatively lower no but not too low as sockets like 
#	80 and 22 are reserved for tcp and ssh

s.listen(5)
#if multiple sockets try to send data then it'll for a queue of 5
while True:
 	clientsocket, address= s.accept() #client socket is just another socket object
 				# like s above. Address represt the IP address of the client

 	print(f"Establised the connection with ",{address})

 	clientsocket.send(bytes("Hello There !", "utf-8"))
 	clientsocket.close()