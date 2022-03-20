import scapy.all as scapy
import argparse
from scapy.layers.l2 import ARP, Ether


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", required=True)
    return parser.parse_args()


def scan_range(ip_range):
    p = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    ans, _ = scapy.srp(p, timeout=3)
    res = []
    for s, r in ans:
        res.append(f"IP:{r.psrc} MAC:{r.hwsrc}")
    return res



if __name__ == "__main__":
    options = args()
    devices = scan_range(options.range)
    for d in devices:
        print(d)
