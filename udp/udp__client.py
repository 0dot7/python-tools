from _socket import *

client = socket(AF_INET, SOCK_DGRAM)

# 设置 IP及端口
host = '127.0.0.1'
port = 6666
server_addr = (host, port)

while True:
    data = input("请输入待传数据：")
    client.sendto(data.encode('utf-8'), server_addr)
    data, addr = client.recvfrom(1024)
    print('接收到 %s 的返回数据：%s' % (addr, data.decode('utf-8')))
