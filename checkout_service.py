# checkout_service
import json
import socket

SIZE = 1024

class CheckoutClient:
    def __init__(self, host='localhost', port=8081):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.address)

    def fetch_credit_report(self, user_id):
        self.sock.sendall(json.dumps(('fetch_credit_report', [user_id], {})).encode())
        response = json.loads(self.sock.recv(SIZE).decode())
        return response

    def disconnect(self):
        self.sock.close()

if __name__ == "__main__":
    client = CheckoutClient()
    client.connect()
    user_id = "user123"
    print(f"Requesting credit report for {user_id}")
    response = client.fetch_credit_report(user_id)
    print(f"Received response: {response}")
    client.disconnect()
