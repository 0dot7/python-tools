# coding:utf-8
import time
from socket import *

# 设置服务端连接的IP和端口
host = '127.0.0.1'
port = 7777
server_addr = (host, port)

count = 1
while True:
    if count > 10:
        time.sleep(1)
        print('%s|连接%s超时' % (time.strftime('%Y-%m-%d %H:%M:%S'), server_addr))
        break
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(server_addr)
        count = 1
        print('%s|服务端%s连接成功' % (time.strftime('%Y-%m-%d %H:%M:%S'), server_addr))
        while True:
            try:
                msg = input('请输入待传数据：')  # 接收用户输入
                if not msg:  # 如果输入为空，即直接回车结束输入
                    print('%s|服务端%s已中断' % (time.strftime('%Y-%m-%d %H:%M:%S'), server_addr))
                    client.close()
                    break
                client.send(msg.encode('utf-8'))
                data = client.recv(1024)
                print(data.decode('utf-8'))
                time.sleep(0.5)
            except ConnectionResetError:
                print('%s|服务端%s已中断' % (time.strftime('%Y-%m-%d %H:%M:%S'), server_addr))
                client.close()
                break
    except ConnectionRefusedError:
        print('无法连接到服务端')
        count += 1
