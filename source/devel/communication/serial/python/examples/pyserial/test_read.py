#!/usr/bin/python2
"""

::

    python test_read_2.py

::

    Msg086
    Msg087
    Msg088
    Msg089
    Msg090
    Msg091
    Msg092
    Msg093
    Msg094
    Msg095

"""

import serial


device_port = serial.Serial("/dev/serial/by-id/usb-id3_semiconductors_MEABOARD_00000000-if00", 115200, timeout=30)
while 1:
    answer = device_port.read(6)
    print answer
device_port.close()
