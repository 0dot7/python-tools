import ipaddress
import queue
from random import randint

from scapy.all import *
from scapy.layers.inet import IP, ICMP
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def scan_once(ip_dst):
    # 构建ping包（复杂版）
    ip_id = randint(1, 65535)
    icmp_id = randint(1, 65535)
    icmp_seq = randint(1, 65535)
    packet1 = IP(dst=ip_dst, ttl=64, id=ip_id) / ICMP(id=icmp_id, seq=icmp_seq) / b'rootkit'
    result = sr1(packet1, timeout=1, verbose=False)
    if result:
        print(str(ip_dst) + ' is alive')
    else:
        print(str(ip_dst) + ' is down')
    pass


def scan_ping(ip_dst):
    ans, unans = sr(IP(dst=ip_dst) / ICMP(), timeout=1, verbose=False)
    ans.summary(lambda s, r: r.sprintf("%IP.src% is alive"))


def scan_subnet(ip_dst):
    network = list(ipaddress.ip_interface(ip_dst).network)
    tasks = []
    q = queue.Queue()
    for ip in network:
        tasks.append(threading.Thread(target=scan_ping, args=(str(ip),)))
    for i in tasks:
        q.put(i)
    while not q.empty():
        q.get().start()
    for i in tasks:
        i.join()
    print("Finished")
    pass


if __name__ == '__main__':
    choice = '1'
    while choice:
        choice = input("选择进行单台主机探测或子网扫描探测（1：单台主机探测 2：子网扫描探测 0：提出）：")
        if choice == '1':
            ip1 = input("输入ip：")
            scan_once(ip1)
        elif choice == '2':
            ip2 = input("输入子网ip：")
            scan_subnet(ip2)
        else:
            break
