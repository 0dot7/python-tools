from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1


def window_scan(ip, port):
    try:
        ans = sr1(IP(dst=ip) / TCP(dport=port, flags="A"), timeout=1, verbose=False)
        if ans is None:
            print("%s port %s is closed | filtered" % (ip, port))
        elif ans is not None and ans.haslayer(TCP):
            if ans.getlayer(TCP).window == 0:
                print("%s port %s is closed" % (ip, port))
            elif ans.getlayer(TCP).window > 0:
                print("%s port %s is open" % (ip, port))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dst_ip = input('ip:')
    dst_port = int(input('port:'))
    window_scan(dst_ip, dst_port)