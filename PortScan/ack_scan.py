from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1


def ack_scan(ip, port):
    try:
        ans = sr1(IP(dst=ip) / TCP(dport=port, flags="A"), timeout=1, verbose=False)
        if ans is None:
            print("%s port %s is filtered and FireWall is up" % (ip, port))
        elif ans is not None:
            if ans.haslayer(TCP) and ans.getlayer(TCP).flags == 'RA':
                print("%s port %s is unfiltered and FireWall is down" % (ip, port))
            elif ans.haslayer(ICMP) and ans.getlayer(ICMP).type == 3 and ans.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
                print("%s port %s is filtered and FireWall is up" % (ip, port))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dst_ip = input('ip:')
    dst_port = int(input('port:'))
    ack_scan(dst_ip, dst_port)