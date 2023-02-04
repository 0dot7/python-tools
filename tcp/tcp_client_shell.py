import time
from socket import *
import struct

# 设置服务端连接的IP和端口
host = '127.0.0.1'
port = 7777
server_addr = (host, port)

while True:
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(server_addr)
        print('%s|服务端%s连接成功' % (time.strftime('%Y-%m-%d %H:%M:%S'), server_addr))
        while True:
            try:
                cmd = input('>>').strip().encode('utf-8')
                client.send(cmd)
                head = client.recv(4)
                size = struct.unpack('i', head)[0]
                cur_size = 0
                result = b''
                while cur_size < size:
                    data = client.recv(1024)
                    cur_size += len(data)
                    result += data
                print(result.decode('gbk'))  # windows系统默认编码是gbk，解码肯定也要用gbk
            except ConnectionResetError:
                print('%s|服务端%s已中断' % (time.strftime('%Y-%m-%d %H:%M:%S'), server_addr))
                client.close()
                break
    except ConnectionRefusedError:
        print('无法连接到服务端')
        break
