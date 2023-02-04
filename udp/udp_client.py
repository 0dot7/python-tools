#!/usr/bin/python3
# 文件名：udp_client.py

import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 设置连接服务器的 ip及端口
host = '127.0.0.1'
port = 8888
server_addr = (host, port)

# 连接服务，指定主机和端口
s.connect(server_addr)

# 传送数据
data = input("请输入待传数据：")
s.sendto(data.encode('utf-8'), server_addr)
