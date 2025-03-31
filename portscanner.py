#!/usr/bin/python3
import socket
import sys


def scanHost(ip, startPort, endPort):
    print('[*] Starting TCP port scan on host %s' % ip)

    tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on host %s complete' % ip)


def scanRange(network, startPort, endPort):
    print('[*] Starting TCP port scan on network %s.0' % network)

    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on network %s.0 complete' % network)


def tcp_scan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()
                
        except Exception:
            pass


if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:
        print('Usage: python3 portscanner.py <IP address> <start port> <end port>')
        print('Example: python3 portscanner.py 192.168.1.10 1 65535\n')
        print('Usage: python3 portscanner.py <network> <start port> <end port> -n')
        print('Example: python3 portscanner.py 192.168.1 1 65535 -n')

    elif len(sys.argv) >= 4:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(network, startPort, endPort)

    if len(sys.argv) == 5:
        scanRange(network, startPort, endPort)
