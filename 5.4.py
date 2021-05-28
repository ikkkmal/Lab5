import socket

s= socket.socket()

port= 8888

s.connect(('192.168.56.101', port))

print(s.recv(1024).decode("utf-8"))

filename= input('\nFile to store in server: ')
s.send(filename.encode())

file= open(filename, "rb")

File= file.read(99999)

while File:
	print("\nMessage from the server: ", s.recv(1024).decode("utf-8"))

	s.send(File)

	print("\n", filename+ " has been stored in the server.")

s.close()
