from scapy.layers.inet import IP, UDP, ICMP
from scapy.sendrecv import sr1


def udp_scan(ip, port, timeout=3):
    try:
        ans = sr1(IP(dst=ip) / UDP(dport=port), timeout=timeout, verbose=False)
        if ans is not None:
            if ans.haslayer(ICMP):
                icmp_fields = ans.getlayer(ICMP).fields
                if icmp_fields["type"] == 3 and icmp_fields["code"] == 3:
                    print("%s port %s is closed" % (ip, port))
                else:
                    print("%s port %s is filtered" % (ip, port))
            if ans.haslayer(UDP):
                print("%s port %s is open" % (ip, port))
        elif ans is None:
            print("%s port %s is no response" % (ip, port))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dst_ip = input('ip:')
    dst_port = int(input('port:'))
    udp_scan(dst_ip, dst_port)
