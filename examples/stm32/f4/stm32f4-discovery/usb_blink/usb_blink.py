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

cmd = 0x1
dev.write(cmd, "1")

