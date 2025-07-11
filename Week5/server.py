import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost',12345))

server_socket.listen()

print("server is listening on port 12345")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

data = client_socket.recv(1024).decode()
print("Received:",data)

# response
client_socket.send("Hello from server!".encode())

server_socket.close()
client_socket.close()


