import socket
import json


class ClientHttp:
    def __init__(self):
        self.client = None
        self.target_host = "127.0.0.1"
        self.target_port = 5000

    def run(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        self.client.connect((self.target_host, self.target_port))

    def get_user(self, user):
        request = f'GET {user} HTTP/1.1\r\nHost:{self.target_host}\r\n\r\n'
        self.client.send(request.encode())

        total_data = []

        while True:
            res = self.client.recv(4096)
            if res:
                total_data.append(res.decode())
            else:
                break

        result = ''.join(total_data)
        data = result.split()
        return {
            'code': data[1],
            'user': json.loads(data[-1])
        }

# if __name__ == '__main__':
#     client = ClientHttp()
#     client.run()
#     data = client.get_user('/user/1')
#     print(data[0][9:12])
#     print(data[-1])
#     print()
