#!/usr/bin/python3
# 文件名：udp_server.py

import socket

# 创建 socket 对象
server_socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 设置 IP及端口
host = '127.0.0.1'
port = 8888
server_addr = (host, port)

# 绑定端口号
server_socket_udp.bind(server_addr)

# 等待客户端连接
print("listening...")
client_socket, addr = server_socket_udp.recvfrom(1024)

print('来自客户端地址：%s' % str(server_addr))
print('接收数据：%s\n ' % client_socket.decode('utf-8'))
server_socket_udp.close()
