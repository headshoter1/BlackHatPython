import socket
import os

# узел для прослушивания
HOST = '10.10.10.131'

def main():
    # создаем сырой сокет и привязываем к общедоступному интерфейсу
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    # делаем так, чтобы захватывался IP-заголовок
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # читаем один пакет
    print(sniffer.recvfrom(65565))
    # если мы в Windows, выключаем неизбирательный режим
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()