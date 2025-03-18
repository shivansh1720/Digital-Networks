import socket
import threading
import sys

exit_event = threading.Event()

def receive_messages(sock):   #this the thread function for recieving messages
    global exit_event
    while not exit_event.is_set():
        try:
            sock.settimeout(1)  # Set a timeout to avoid blocking forever
            data, addr = sock.recvfrom(1024)
            message = data.decode()
            print(f"\nReceived from {addr}: {message}")
            if message.lower() in ["exit", "bye"]:  #This sets exit event is exit is recieved over any thread
                print("Received exit command. Closing chat.")
                exit_event.set()
                break
        except socket.timeout:
            continue  
        except OSError:
            break  

def send_messages(sock, target_ip, target_port):    #this the thread function for sending messages
    global exit_event
    while not exit_event.is_set():
        try:
            sock.settimeout(1)
            msg = input("You: ")
            if msg.lower() in ["exit", "bye"]:      #This sets exit event is exit is recieved over any thread
                exit_event.set()
                break
            sock.sendto(msg.encode(), (target_ip, target_port))
        except socket.timeout:
            continue
        except OSError:
            break  

def start_udp_chat(my_port, target_ip, target_port):
    global exit_event
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", my_port))
    
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    send_thread = threading.Thread(target=send_messages, args=(sock, target_ip, target_port))
    receive_thread.start()   #starts the receive thread
    send_thread.start()      #starts the send thread

    exit_event.wait() # This blocks following commands until exit is sent over any of the following commands
    sock.sendto("Goodbye".encode(), (target_ip, target_port))  # A goodbye message is sent to UDP monitor to demarcate closure of chat  
    sock.close()                               # Close the socket
    send_thread.join()                         # Send thread is exited
    receive_thread.join()                      # Receive thread is exited
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <your_PC_port> <target_IP> <target_port>")
    else:
        start_udp_chat(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
