##https://github.com/citruz/beacontools/blob/master/examples/scanner_ibeacon_example.py
import time

from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> " % (bt_addr, rssi))

# scan for all iBeacon advertisements from beacons with certain properties:
# - uuid
# - major
# - minor
# at least one must be specified.
scanner = BeaconScanner(callback, 
    device_filter=IBeaconFilter(uuid="8a5e7768-4f64-11eb-ae93-0242ac130002")
)
scanner.start()
time.sleep(5)
scanner.stop()

# scan for all iBeacon advertisements regardless from which beacon
scanner = BeaconScanner(callback,
    packet_filter=IBeaconAdvertisement
)
scanner.start()
time.sleep(5)
scanner.stop()