from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1


def xmas_scan(ip, port):
    try:
        ans = sr1(IP(dst=ip) / TCP(dport=port, flags="FPU"), timeout=1, verbose=False)
        if ans is None:
            print("%s port %s is open | filtered" % (ip, port))
        elif ans is not None:
            if ans.getlayer(TCP).flags == 'RA':
                # ans.display()
                print("%s port %s is closed" % (ip, port))
            elif ans.getlayer(ICMP).type == 3 and ans.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
                print("%s port %s is filtered" % (ip, port))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dst_ip = input('ip:')
    dst_port = int(input('port:'))
    xmas_scan(dst_ip, dst_port)
