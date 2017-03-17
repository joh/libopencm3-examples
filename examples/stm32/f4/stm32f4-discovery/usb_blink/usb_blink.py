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

# dev.set_configuration()

def bulk():
    print("bulk")

    data = [1,2,3,4]
    n = dev.write(0x01, data)
    print("wrote {} bytes: {}".format(n, data))

    data = dev.read(0x81, 4)
    print("read {} bytes: {}".format(len(data), data))

def ctrl_on():
    print("ctrl_on")
    bmRequestType = usb.util.build_request_type(
            usb.util.CTRL_OUT,
            usb.util.CTRL_TYPE_VENDOR,
            usb.util.CTRL_RECIPIENT_ENDPOINT)
    dev.ctrl_transfer(bmRequestType, 0x11)

def ctrl_off():
    print("ctrl_off")
    bmRequestType = usb.util.build_request_type(
            usb.util.CTRL_OUT,
            usb.util.CTRL_TYPE_VENDOR,
            usb.util.CTRL_RECIPIENT_ENDPOINT)
    dev.ctrl_transfer(bmRequestType, 0x12)

def ctrl_data():
    print("ctrl_data")
    bmRequestType = usb.util.build_request_type(
            usb.util.CTRL_OUT,
            usb.util.CTRL_TYPE_VENDOR,
            usb.util.CTRL_RECIPIENT_ENDPOINT)

    # Write data to device buf
    data = array.array('B', [1, 2, 3, 4, 5, 6])
    n = dev.ctrl_transfer(bmRequestType, 0x13, data_or_wLength=data)

    print("wrote {} bytes: {}".format(n, data))

    # Read data back from device buf
    bmRequestType = usb.util.build_request_type(
            usb.util.CTRL_IN,
            usb.util.CTRL_TYPE_VENDOR,
            usb.util.CTRL_RECIPIENT_ENDPOINT)

    # Write data to device buf
    data = dev.ctrl_transfer(bmRequestType, 0x93, data_or_wLength=6)

    print("read {} bytes: {}".format(len(data), data))


if __name__ == '__main__':
    cmd = "bulk"
    if len(sys.argv) > 1:
        cmd = sys.argv[1]

    if cmd == "bulk":
        bulk()
    elif cmd == "ctrl_on":
        ctrl_on()
    elif cmd == "ctrl_off":
        ctrl_off()
    elif cmd == "ctrl_data":
        ctrl_data()
    else:
        print("Invalid command: {}".format(cmd))
