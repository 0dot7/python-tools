import socketserver
import time

# 设置 IP及端口
host = '127.0.0.1'
port = 6666
server_addr = (host, port)


class MyUdpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print('%s|接收来自 %s 的数据：%s'
              % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address, data.decode('utf-8')))
        socket.sendto(data.upper(), self.client_address)


if __name__ == '__main__':
    server = socketserver.ThreadingUDPServer(server_addr, MyUdpHandler)
    print("listening...")
    server.serve_forever()
