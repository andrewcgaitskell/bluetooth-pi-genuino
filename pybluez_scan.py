#!/usr/bin/env python3
"""PyBluez ble example scan.py"""

from gattlib import DiscoveryService

service = DiscoveryService()
devices = service.discover(2)

for address, name, rssi in devices.items():
    print("Name: {}, address: {}, rssi: {}".format(name, address, rssi))
