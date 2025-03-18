import socket
import threading

#Function to start TCP server
def start_tcp_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"TCP Server listening on {host}:{port}")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data.upper())   #Sends back recieved Data after converting to uppercase
    
    conn.close()
    server_socket.close()

def start_tcp_client(server_host='127.0.0.1', server_port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    while True:    #causes it to run in infinite loop
        msg = input("Enter message: ")
        client_socket.sendall(msg.encode())
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <mode>")
        print("Modes: server, client")
    elif sys.argv[1] == "server":
        start_tcp_server()
    elif sys.argv[1] == "client":
        start_tcp_client()
    else:
        print("Invalid mode!")
