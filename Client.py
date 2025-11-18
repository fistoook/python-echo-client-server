import socket

class Client:
    def __init__(self, port):
        self.port = port
        self.client = socket.socket()
        self.client.connect(('127.0.0.1', self.port))
    
    def barkAtTheServer(self):
        self.client.send('bark!'.encode())
        echo = (self.client.recv(1024)).decode()
        print(f"Server sent a message: {echo}.\n")
    
    def sendMessageToServer(self, message):
        self.client.send(message.encode())
        echo = (self.client.recv(1024)).decode()
        print(f"Server sent a message: {echo}.\n")

    def exitServer(self):
        self.client.send('exit'.encode())