import socket
from contextlib import closing
from tqdm import tqdm
   
def is_port_open(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return sock.connect_ex((host, port)) == 0
ports = []
for i in tqdm(range(65535)):
   if is_port_open('192.168.0.105', i):
      ports.append(i)