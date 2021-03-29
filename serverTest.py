#Jason Shamayev
#1001627879

import socket
import threading
from urllib import request
import time
from socket import *
import os

HEADER = 64
PORT = 8080
SERVER = 'localhost'
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT = "!DISCONNECT"

serverSocket = socket(AF_INET, SOCK_STREAM)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        message_length = conn.recv(HEADER).decode(FORMAT) #receives message from client and decodes it
        if message_length:
            try:
                message_length = int(message_length)
                message = conn.recv(message_length).decode(FORMAT) #gets and decodes the message using message length

                if message == DISCONNECT:
                    connected = False
            
                print(f"[{addr}] {message}")
                conn.send("Message received".encode(FORMAT))
                conn.send(message.encode(FORMAT))
            except ValueError:
                pass 

    conn.close()


def start():
    serverSocket.bind(ADDRESS)
    serverSocket.listen(5)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = serverSocket.accept()

        #get client request
        request = conn.recv(1024).decode(FORMAT)
        print(request)

       
        #get content of file
        f = open('Computer Networks/JasonServer.html') #opens file
        content = f.read()
        f.close()
        #send HTTP response
        response = ('HTTP/1.0 200 OK\n\n' + content) #sends HTTP response valid
        conn.sendall(response.encode(FORMAT))

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
        
    conn.close()



print("[STARTING SERVER] server is starting...")
print('Access http://localhost:8080')
start()
serverSocket.close()