import asyncio
import ipaddress
from kasa import Discover

for ip in ipaddress.IPv4Network("192.168.1.0/24"):
    device = asyncio.run(Discover.discover(target=str(ip), timeout=0.3))
    if device:
        print(f"ip: {ip} device: {device}")


# device = asyncio.run(Discover.discover(target="192.168.1.117"))
# print(f"ip: 192.168.1.117 device: {device}")
