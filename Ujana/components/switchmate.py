import bluepy
import time

class Bright:

    handles = {
        'SysTime': 0x001F,
        'Timer1': 0x0021,
        'Timer2': 0x0023,
        'Timer3': 0x002E,
        'SwState': 0x0030,
        'Motion': 0x0032,
    }

    def __init__(self, mac_addr):
        self.mac = mac_addr

    def _connect(self):
        return bluepy.btle.Peripheral(self.mac, bluepy.btle.ADDR_TYPE_RANDOM, 0)

    def SetState(self, cmd):
        lightswitch = self._connect()
        if (cmd == "on"):
            lightswitch.writeCharacteristic(0x0030, b'\x01')
        else:
            lightswitch.writeCharacteristic(0x0030, b'\x00')

    def SetMotion(self, enable="yes", start="00:00", end="00:00", duration="00:01"):
        print(time.time())
