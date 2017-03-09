#!/usr/bin/env python
import usb.core
import usb.util
import sys
import random
import struct
import array
import numpy as np
from itertools import cycle
import time

# find our device
dev = usb.core.find(idVendor=0x0483, idProduct=0x5740)

# was it found?
if dev is None:
    print("Couldn't find device")
    sys.exit(2)

dev.set_configuration()

i = 0

while True:
    buf = array.array('B', range(i, i+4))
    bytes_written = dev.write(0x1, buf)

    print("wrote {} bytes: {}".format(bytes_written, buf))

    buf = dev.read(0x81, bytes_written)

    print("read {} bytes: {}".format(len(buf), buf))

    # time.sleep(1)

    i += 1
