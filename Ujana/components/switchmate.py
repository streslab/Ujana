import bluepy
import datetime


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

    def SetMotion(self, enable="yes", start="00:00", end="00:00", duration="00:01"):
        lightswitch = self._connect()

        hexhour = datetime.datetime.now().hour.to_bytes(1, "big")
        hexmin = datetime.datetime.now().minute.to_bytes(1, "big")
        hexsec = datetime.datetime.now().second.to_bytes(1, "big")
        hexday = datetime.datetime.now().weekday().to_bytes(1, "big")

        writeval = hexhour + hexmin + hexsec + hexday

        print(str(writeval))

        lightswitch.writeCharacteristic(self.handles['SysTime'], writeval)
        lightswitch.writeCharacteristic(self.handles['Motion'], b'\x01\x00\x00\x00\x00\x01')

    def SetState(self, cmd):
        lightswitch = self._connect()
        if (cmd == "on"):
            lightswitch.writeCharacteristic(self.handles['SwState'], b'\x01')
        else:
            lightswitch.writeCharacteristic(self.handles['SwState'], b'\x00')
