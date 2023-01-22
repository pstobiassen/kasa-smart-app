import asyncio
import ipaddress
from kasa import Discover

devices = []


def DiscoverDevices():
    for ip in ipaddress.IPv4Network("192.168.1.0/24"):
        asyncio.run(
            Discover.discover(
                target=str(ip), timeout=0.5, on_discovered=get_device_info
            )
        )
    return devices


async def get_device_info(dev):
    devices.append({"host": dev.host, "alias": dev.alias})
    print(f"Discovered {dev}")


# my_devices = DiscoverDevices()

# print(f"my devices: {my_devices}")

# device = asyncio.run(Discover.discover(target="192.168.1.117"))
# print(f"ip: 192.168.1.117 device: {device}")
