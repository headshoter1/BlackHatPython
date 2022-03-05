#!/usr/bin/env python3

"""
iface MAC

change MAC

"""
import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser
    parser.add_argument("-m", "--mac", required=True, help="New MAC-address")
    parser.add_argument("-i", "--iface", required=True, help="Your interface")
    parser.add_argument("-i", "--test", required=False, help="Test valuse")

def check_mac(mac_address):
    return re.match(r"^(([a-f0-9]{2})[-:]?){5}[a-f0-9]{2}", mac_address.lower())


def main():
    mac_adress = input("Enter new MAC:")
    iface = input("Enter iface:")
    if not check_mac(mac_adress):
        print("Wrong mac address")
        return
if __name__ == "__main__":
    main()