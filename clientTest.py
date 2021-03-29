#Jason Shamayev
#1001627879

import socket
import time


HEADER = 64
PORT = 8080
SERVER = 'localhost'
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT = "!DISCONNECT"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDRESS) #connect host and port to socket
send_time = time.time()

def send(msg):  #sends messages and calculates the RTT for each message
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    clientSocket.send(send_length)
    clientSocket.send(message)
    recv_time = time.time()
    RTT = recv_time - send_time
    print(clientSocket.recv(2048).decode(FORMAT))
    print("RTT:",RTT)

send("Hello")
send("Sup?")
send(DISCONNECT)
cmd = "GET http://127.0.0.1/JasonServer.html HTTP/1.0\r\n\r\n".encode()
clientSocket.send(cmd)
clientSocket.close()
