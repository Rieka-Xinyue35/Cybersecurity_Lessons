import socket

target_ip_address = '192.168.1.61'
list_of_ports =  [123,445,80,8080,25]
print("Scanning open ports...")

for port in list_of_ports:
    scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner_socket.settimeout(1)
    scanned_port = scanner_socket.connect_ex((target_ip_address,port))
    if scanned_port == 0:
         print(f"Port {port} is Opened")
    else:
        print(f"Port {port} is Closed")

    scanner_socket.close()
