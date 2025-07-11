import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.61', 4444))
server_socket.listen(1)
print("Server is listening on port 4444")

client_socket, client_address = server_socket.accept()
print(client_address)

while True:
    command = input(">> ")
    if command == 'exit':
        client_socket.send(b'exit')
        break

    client_socket.send(command.encode())
    response = client_socket.recv(4096).decode()
    print(response)

client_socket.close()
server_socket.close()
