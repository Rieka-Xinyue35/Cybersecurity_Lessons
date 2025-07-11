import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('192.168.1.130',12345))

while True:
	message = input("You: ")
	client_socket.send(message.encode())
	if message.lower() == 'bye':
		break
	response = client_socket.recv(1024).decode()
	print("Server: ", response)

client_socket.close()
