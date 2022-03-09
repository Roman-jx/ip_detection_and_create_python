from re import L;
import socket;
from threading import local;
hostname = socket.gethostname();
local_ip = socket.gethostbyname(hostname);
print(f"HOSTname: {hostname}\nIP address: {local_ip}");