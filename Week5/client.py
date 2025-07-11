import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('192.168.1.61',4444))

while True:
	command = input("You: ")
	client_socket.send(command.encode())
	if command.lower() == 'bye':
		break
	response = client_socket.recv(4096).decode()
	print("Server: ", response)

client_socket.close()
