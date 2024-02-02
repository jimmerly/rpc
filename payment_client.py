import json
import socket

SIZE = 1024

class RPCClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.address = (host, port)

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.address)

    def disconnect(self):
        self.sock.close()

    def __getattr__(self, name):
        def method(*args, **kwargs):
            self.sock.sendall(json.dumps((name, args, kwargs)).encode())
            response = json.loads(self.sock.recv(SIZE).decode())
            if "error" in response:
                raise Exception(response["error"])
            return response
        return method

if __name__ == "__main__":
    client = RPCClient()
    client.connect()

    # Simulate a payment process
    try:
        response = client.process_payment("user123", 100)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")

    client.disconnect()
