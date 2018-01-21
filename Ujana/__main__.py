import bluepy

nearby_devices = bluepy.btle.Scanner().scan()

#nearby_devices = bluetooth.discover_devices(device_id=0)

for bdaddr in nearby_devices:
    print(bdaddr.getScanData())