import json
import socket
from threading import Thread

SIZE = 1024

class RPCServer:
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self.address = (host, port)
        self._methods = {}

    def registerMethod(self, function):
        self._methods[function.__name__] = function

    def __handle__(self, client, address):
        print(f'Managing requests from {address}.')
        while True:
            try:
                data = client.recv(SIZE)
                if not data:
                    break
                functionName, args, kwargs = json.loads(data.decode())
                if functionName in self._methods:
                    response = self._methods[functionName](*args, **kwargs)
                    client.sendall(json.dumps(response).encode())
                else:
                    raise Exception('Method not found')
            except Exception as e:
                client.sendall(json.dumps({'error': str(e)}).encode())
                break
        print(f'Completed request from {address}.')
        client.close()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.address)
            sock.listen()
            print(f'Server running on {self.address}')
            while True:
                client, address = sock.accept()
                Thread(target=self.__handle__, args=(client, address)).start()

# Example usage
if __name__ == "__main__":
    server = RPCServer()

    def process_payment(user_id, amount):
        print(f"Processing payment for user {user_id} of amount {amount}")
        return {"status": "success", "user_id": user_id, "amount": amount}

    server.registerMethod(process_payment)
    server.run()
