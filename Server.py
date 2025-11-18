import socket
import time

class Server:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket()
        self.sock.bind(('0.0.0.0', self.port))
    
    def run(self):
        self.sock.listen(5)
        print('Running Server...')
        self.work()
      
    def work(self):
        while True:
            client, name = self.sock.accept()
            print(f"Client connected! Ip:{name[0]}, Port:{name[1]}")

            while True:
                data = (client.recv(1024)).decode()
                if data.lower() == 'exit':
                    print('\nConnection stopped.')
                    self.sock.close()
                    return
                else:
                    print(f"Client sent a message: {data}. echoing back...")
                    client.send(data.encode())