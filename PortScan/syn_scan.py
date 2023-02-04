from scapy.layers.inet import TCP, IP
from scapy.sendrecv import sr1, send


def syn_scan(ip, port):
    try:
        ans = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=1, verbose=False)
        if ans is not None:
            if ans.getlayer(TCP).flags == 0x12:
                send(IP(dst=ip) / TCP(dport=port, flags='R'), verbose=False)
                print("%s port %s is open" % (ip, port))
            elif ans.getlayer(TCP).flags == 0x14:
                print("%s port %s is closed" % (ip, port))
            else:
                print("%s port %s is filtered" % (ip, port))
        elif ans is None:
            print("%s port %s is no response" % (ip, port))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dst_ip = input('ip:')
    dst_port = int(input('port:'))
    syn_scan(dst_ip, dst_port)
