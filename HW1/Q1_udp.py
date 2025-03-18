import socket
import threading

def start_udp_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
    
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        server_socket.sendto(data.upper(), addr)

def start_udp_client(server_host='127.0.0.1', server_port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        msg = input("Enter message: ")
        client_socket.sendto(msg.encode(), (server_host, server_port))
        data, _ = client_socket.recvfrom(1024)
        print(f"Received: {data.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <mode>")
        print("Modes: server, client")
    elif sys.argv[1] == "server":
        start_udp_server()
    elif sys.argv[1] == "client":
        start_udp_client()
    else:
        print("Invalid mode!")
