import bluepy

lightswitch = bluepy.btle.Peripheral("AA:BB:CC:DD:EE:FF", bluepy.btle.ADDR_TYPE_RANDOM,0)
print("Connected..")

while(1):
    cmd = input("> ")
    if(cmd == "on"):
        lightswitch.writeCharacteristic(0x0030, b'\x01')
    else:
        lightswitch.writeCharacteristic(0x0030, b'\x00')
