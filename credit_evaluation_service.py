# credit_evaluation_service
import json
import socket
from threading import Thread

SIZE = 1024

class CreditEvaluationServer:
    def __init__(self, host='0.0.0.0', port=8081):
        self.host = host
        self.port = port
        self.address = (host, port)
        self._methods = {'fetch_credit_report': self.fetch_credit_report}

    def fetch_credit_report(self, user_id):
        # 模拟从数据库或第三方服务获取信用报告的过程
        print(f"Fetching credit report for user {user_id}")
        return {"status": "success", "report": f"Credit Report for {user_id}"}

    def __handle__(self, client, address):
        print(f'Credit Evaluation Service: Connection from {address}')
        while True:
            data = client.recv(SIZE)
            if not data:
                break
            functionName, args, kwargs = json.loads(data.decode())
            if functionName in self._methods:
                response = self._methods[functionName](*args, **kwargs)
                client.sendall(json.dumps(response).encode())
            else:
                client.sendall(json.dumps({'error': 'Method not found'}).encode())
        client.close()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.address)
            sock.listen()
            print(f'Credit Evaluation Service listening on {self.host}:{self.port}')
            while True:
                client, address = sock.accept()
                Thread(target=self.__handle__, args=(client, address)).start()

if __name__ == "__main__":
    server = CreditEvaluationServer()
    server.run()
