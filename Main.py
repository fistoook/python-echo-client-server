import threading
from Server import Server
from Client import Client
import time

def main():
    server = Server(12345)

    # Run server in a background thread
    t = threading.Thread(target=server.run, daemon=True)
    t.start()

    # Give server time to start
    time.sleep(1)

    # Now create a client in same file
    client = Client(12345)
    client.sendMessageToServer("hello")
    time.sleep(1)
    client.sendMessageToServer("how are you?")
    time.sleep(1)
    client.barkAtTheServer()
    time.sleep(1)
    client.exitServer()

if __name__ == "__main__":
    main()