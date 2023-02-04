#!/usr/bin/python3
# 文件名：tcp_client.py

import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置 IP及端口
host = '127.0.0.1'
port = 9999

# 连接服务，指定IP和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)
print(msg.decode('utf-8'))

data = input('请输入待传数据：')
s.send(data.encode('utf-8'))

s.close()
