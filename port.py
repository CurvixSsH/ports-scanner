import argparse
import socket
import threading
from queue import Queue
import time
import pyfiglet

def print_banner():
    title = pyfiglet.figlet_format("Port Scanner", font="standard")
    banner_width = len(title.split('\n')[0])
    color_switch = True
    for line in title.split('\n'):
        if color_switch:
            print("\033[1;34m" + "|" + line.center(banner_width) + "|\033[0m")
            color_switch = False
        else:
            print("\033[1;37m" + "|" + line.center(banner_width) + "|\033[0m")
            color_switch = True
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")
    print("\033[1;34m{:^{}}\033[0m".format("\033[1;34mBy\033[0m \033[1;37mCurvixSsH", banner_width))
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")



def parse_args():
    parser = argparse.ArgumentParser(description="Port Scanner by CurvixSsH")
    parser.add_argument("target", help="IP address or hostname to scan")
    parser.add_argument("-pn", "--no_ping", action="store_true", help="Skip host discovery")
    args = parser.parse_args()
    return args


def set_port_range():
    port_range = range(1, 65536)
    return port_range


def set_ping(args):
    if args.no_ping:
        ping = False
    else:
        ping = True
    return ping


print_banner()

args = parse_args()
target = args.target
ping = set_ping(args)
port_range = set_port_range()
pn = args.no_ping
num_threads = 850

print(f"\nEscaneando puertos TCP de {target} ...\n")

def scan_port(port, pn=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        if pn:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((target, port))
        print(f"\033[1;34m[\033[1;32m+\033[1;34m] \033[1;37mPort \033[1;32m{port}\033[1;37m/TCP \033[1;32mEsta \033[1;37mAbierto\033[0m")
        s.close()
        return port
    except:
        s.close()
        return None

def print_result(results):
    banner_width = 40
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")
    print("\033[1;34m|{:^38}|\033[0m".format("RESULTADOS"))
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")
    open_ports = []
    for result in results:
        if result is not None:
            port = result
            print(f"\033[1;32m| \033[1;32mPort \033[1;37m{port}\033[1;37m/TCP \033[1;32mEsta \033[1;37mAbierto \033[1;32m|\033[0m")
            open_ports.append(port)
    if len(open_ports) == 0:
        print("\033[1;31m|  No Se Encontraron Puertos Abiertos |\033[0m")
    print("\033[1;34m" + "+" + "-"*(banner_width-2) + "+\033[0m")


def worker():
    while True:
        port = q.get()
        result = scan_port(port, pn=pn)
        if result:
            results.append(result)
        q.task_done()

q = Queue()
results = []

start_time = time.time()

for i in range(num_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

for port in port_range:
    q.put(port)

q.join()

elapsed_time = time.time() - start_time

print("\n" + "-"*60)
print(f"\nEscaneo completo en {elapsed_time:.2f} segundos\n")
print_result(results)
