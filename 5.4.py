import socket

s= socket.socket()

port= 8888

s.bind(('', port))

s.listen(5)

print("\nWaiting for connection...")

while True:
	c, addr= s.accept()
	print("\nAccepted a connection from IP: "+ str(addr))

	c.send(b'\nServer: Hi! This is the server to store your file.')

	filename= c.recv(1024).decode("utf-8")
	file= open(filename, "wb")

	print("\nTransferring ", filename)

	File= c.recv(99999)

	while File:
		file.write(File)

	file.close()
	message= "\nFile has been stored succesfully"
	c.send(b'message')
	print(message)

	c.close()
	print("\nClosed the connection")

	break
