# coding:utf-8
import socketserver
import time

# 设置服务端 IP和端口
host = '127.0.0.1'
port = 7777
addr = (host, port)


class MyTcpHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print("%s|连接到客户端:%s" % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address))
        while True:
            try:
                data = self.request.recv(1024)
                print('%s|接收来自 %s 的数据：%s'
                      % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address, data.decode('utf-8')))
                msg = '已接收到数据:[%s]' % data.decode('utf-8')
                self.request.send(msg.encode('utf-8'))
            except ConnectionResetError:
                print('%s|客户端%s已断开连接' % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address))
                break
            except ConnectionAbortedError:
                print('%s|客户端%s已断开连接' % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address))
                break


if __name__ == '__main__':
    tcpSerSock = socketserver.TCPServer(addr, MyTcpHandler)
    print("listening...")
    tcpSerSock.serve_forever()  # 服务端一直开启
