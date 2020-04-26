import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(),1235))

str=""
while True:
	

	msg= s.recv(8)
	if len(msg)<=0:
		break
	str+=msg.decode("utf-8")
print(str)



