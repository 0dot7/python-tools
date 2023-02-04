#!/usr/bin/python3
# 文件名：tcp_server.py

import socket

# 创建 socket 对象
server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置 IP及端口
host = '127.0.0.1'
port = 9999

# 绑定端口号
server_socket_tcp.bind((host, port))

# 设置最大连接数，超过后排队
server_socket_tcp.listen(5)

# 建立客户端连接
print("listening...")
client_socket, client_addr = server_socket_tcp.accept()

print("连接到客户端地址: %s" % str(client_addr))
msg_0 = "成功连接到服务器\r\n"
client_socket.send(msg_0.encode('utf-8'))

msg = client_socket.recv(1024)
print('接收数据：', msg.decode('utf-8'))

client_socket.close()
print("已断开连接\n")
