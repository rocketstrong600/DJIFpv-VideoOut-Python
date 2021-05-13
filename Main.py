import usb.core
import usb.util
import sys
#import ffmpeg
import atexit

GooglesDev = usb.core.find(idVendor=0x2ca3, idProduct=0x1f)
if GooglesDev is None:
    raise ValueError('Googles Not Connected')
print(GooglesDev)
GooglesDev.set_configuration(0x1)
cfg = GooglesDev.get_active_configuration()
intf = cfg[(0,0)]
epOUT = intf[0]
epIN = intf[1]
magic = bytes.fromhex('524d5654')
good = True
try:
    epOUT.write(magic)
except:
    good = False

while good:
    try:
        Data = epIN.read(512)
        sys.stdout.buffer.write(Data)
    except:
        pass
GooglesDev.reset()
usb.util.dispose_resources(GooglesDev)
