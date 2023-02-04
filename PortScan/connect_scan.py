import socket


def connect_scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("%s port %s is open" % (ip, port))
            sock.close()
        else:
            print("%s port %s is down" % (ip, port))
            sock.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dst_ip = input('ip:')
    dst_port = int(input('port:'))
    connect_scan(dst_ip, dst_port)
