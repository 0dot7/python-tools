import socketserver
import struct
import subprocess
import time

# 设置服务端 IP和端口
host = '127.0.0.1'
port = 7777
addr = (host, port)


class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print('%s|客户端%s已连接' % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address))
            try:
                cmd = self.request.recv(1024).decode('utf-8')
                print('执行命令：', cmd)
                res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout = res.stdout.read()
                stderr = res.stderr.read()
                head = struct.pack('i', len(stdout + stderr))
                self.request.send(head)
                self.request.send(stdout)
                self.request.send(stderr)
            except ConnectionResetError:
                print('%s|客户端%s已断开连接' % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address))
                self.request.close()
                print("listening...")
                break
            except ConnectionAbortedError:
                print('%s|客户端%s已断开连接' % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_address))
                self.request.close()
                print("listening...")
                break


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(addr, MyTcpHandler)
    print("listening...")
    server.serve_forever()
