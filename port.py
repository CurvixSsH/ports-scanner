import argparse
import socket
import socks
import threading
from queue import Queue
import time
import pyfiglet
import signal
import sys

def signal_handler(sig, frame):
    print('Stopping the program...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def print_banner():
    title = pyfiglet.figlet_format("Port Scanner", font="standard")
    banner_width = max(len(line) for line in title.split('\n')) + 4
    color_switch = True
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")
    for line in title.split('\n'):
        if color_switch:
            print("\033[1;34m" + "|" + " " + line.ljust(banner_width - 4) + " " + "|\033[0m")
            color_switch = False
        else:
            print("\033[1;37m" + "|" + " " + line.ljust(banner_width - 4) + " " + "|\033[0m")
            color_switch = True
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")
    print("\033[1;34m" + "|" + "{:^{}}".format("\033[1;34mBy\033[0m \033[1;37mCurvixSsH", banner_width - 2) + "|\033[0m")
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")

def parse_args():
    parser = argparse.ArgumentParser(description="""Examples:
                                     

    \033[33mpython port.py google.com\033[0m (default) [ports 1-65535 / 850 threads / 0.5s / Ping] -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
    
    
    \033[33mpython port.py google.com -p 1-6890,8080,57345 -t 800 -to 1 -pn -px [protocol://]host[:port]\033[0m
    """)
    parser.add_argument("target", help="IP or hostname", nargs='?')
    parser.add_argument("-p", "--ports", type=str, default="1-65535", help="Range of ports to scan (default: 1-65535). Example: \033[33m-p 1-500,8080,62544\033[0m")
    parser.add_argument("-t", "--threads", type=int, default=850, help="Number of threads to use (default: 850)")
    parser.add_argument("-to", "--timeout", type=float, default=0.5, help="Connection timeout in seconds (default: 0.5)")
    parser.add_argument("-pn", "--no_ping", action="store_true", help="Skip host discovery")
    parser.add_argument("-px", "--proxy", type=str, help=" \033[32mHTTP\033[0m, \033[32mHTTPS\033[0m, \033[32mSOCKS4\033[0m, or \033[32mSOCKS5\033[0m proxy (format: [\033[33mprotocol://]host[:port\033[0m]). Example: http://195.181.152.71:3128. To get a list of available proxies, visit https://hidemy.name/es/proxy-list/")
    args = parser.parse_args()
    return args

def set_port_range(ports):
    port_range = []
    for port in ports.split(','):
        if '-' in port:
            start, end = map(int, port.split('-'))
            port_range.extend(range(start, end+1))
        else:
            port_range.append(int(port))
    return port_range

def set_ping(args):
    if args.no_ping:
        ping = False
    else:
        ping = True
    return ping

def set_proxy(proxy):
    if proxy is not None:
        protocol, host = proxy.split('://')
        host, port = host.split(':')
        if protocol == 'http':
            socks.set_default_proxy(socks.HTTP, host, int(port))
        elif protocol == 'https':
            socks.set_default_proxy(socks.HTTPS, host, int(port))
        elif protocol == 'socks4':
            socks.set_default_proxy(socks.SOCKS4, host, int(port))
        elif protocol == 'socks5':
            socks.set_default_proxy(socks.SOCKS5, host, int(port))
        socket.socket = socks.socksocket

def scan_port(port, timeout, pn=False):
    if target is None:
        return None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        if pn:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((target, port))
        s.close()
        return port
    except socket.error as e:
        s.close()
        return None

def print_result(results):
    port_services = {}
    with open('port_services.txt', 'r') as f:
        for line in f:
            port, service = line.strip().split(': ')
            port_services[int(port)] = service

    banner_width = 40
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")
    open_ports = []
    for result in results:
        if result is not None:
            port = result
            open_ports.append(port)
    if len(open_ports) == 0:
        print("\033[1;37m|  No Open Ports Found  |\033[0m")
    else:
        print(f"      \033[1;37m|  Found \033[1;31m{len(open_ports)}\033[1;37m open ports  |\033[0m")
    print("\033[1;34m|{:^38}|\033[0m".format("RESULTS"))
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")
    open_ports.sort()
    for port in open_ports:
        service = port_services.get(port, '-')
        print(f"\033[1;32m| \033[1;32mPort \033[1;37m{port}\033[1;37m/TCP \033[1;32mis \033[1;37mOpen \033[1;32m|\033[0m")
        print(f"\033[1;34m|   Service: \033[1;31m{service} |\033[0m")
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")


        
def worker(timeout):
    while True:
        port = q.get()
        result = scan_port(port, timeout, pn=pn)
        if result:
            results.append(result)
        q.task_done()

print_banner()

args = parse_args()
target = args.target
ping = set_ping(args)
port_range = set_port_range(args.ports)
pn = args.no_ping
num_threads = args.threads
timeout = args.timeout

print(f"\nScanning TCP ports of {target} ...\n")

q = Queue()
results = []

start_time = time.time()

for i in range(num_threads):
    t = threading.Thread(target=worker, args=(timeout,))
    t.daemon = True
    t.start()

for port in port_range:
    q.put(port)

q.join()

elapsed_time = time.time() - start_time

print("\n" + "-"*60)
print(f"\nScan completed in {elapsed_time:.2f} seconds\n")
print_result(results)

