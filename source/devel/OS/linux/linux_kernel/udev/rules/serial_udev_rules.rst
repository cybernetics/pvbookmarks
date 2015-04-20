

.. index::
   dialout
   group dialout
   dialout group (RS232)
   RS232
   serial cimmunication


.. _serial_udev_rules:

==================
Serial udev rules
==================


Create the udev rule file
=========================


Prerequisite
------------


You are a 'root' user.


::

    pvergain@houx: ls -l /dev/ttyACM0

::

    crw-rw---- 1 root dialout 166, 0 27 sept. 11:24 /dev/ttyACM0


Only the users who belong to the ``root`` or ``dialout`` groups can access to
the device.

So we have to add the users who will use ``serial device`` to this group::


    gpasswd -a $USERNAME dialout


Example::

    gpasswd -a pvergain dialout


Depending on your OS, you have to reboot (fedora 15 by example).


::

    dmesg


::

    [ 1414.179055] usb 6-2: new full speed USB device using ohci_hcd and address 2
    [ 1414.336096] usb 6-2: New USB device found, idVendor=0b81, idProduct=8004
    [ 1414.336107] usb 6-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [ 1414.336114] usb 6-2: Product: MEABOARD
    [ 1414.336119] usb 6-2: Manufacturer: id3 semiconductors
    [ 1414.336124] usb 6-2: SerialNumber: 00000000
    [ 1414.661889] cdc_acm 6-2:1.0: This device cannot do calls on its own. It is not a modem.
    [ 1414.662253] cdc_acm 6-2:1.0: ttyACM0: USB ACM device
    [ 1414.666412] usbcore: registered new interface driver cdc_acm
    [ 1414.666421] cdc_acm: v0.26:USB Abstract Control Model driver for USB modems and ISDN adapters



::

    > cd /etc/udev/rules.d
    > udevadm control --reload-rules
    > more 99-id3_serial.rules

::

    ATTRS{idVendor}=="0b81", ATTRS{idProduct}=="8004", SUBSYSTEMS=="tty",  \
    ATTRS{SerialNumber}=="00000000", SYMLINK += "cle_rfid"



Python reading test
===================

.. seealso::  :ref:`serial_python_communication`


::

    #!/usr/bin/python2

    import serial


    device_port = serial.Serial("/dev/serial/by-id/usb-id3_semiconductors_MEABOARD_00000000-if00", 115200, timeout=30)
    while 1:
        answer = device_port.read(6)
        print answer
    device_port.close()


Test result
-----------

::

    Msg000
    Msg001
    Msg002
    Msg003
    Msg004
    Msg005
    Msg006
    Msg007
    Msg008
    Msg009
    Msg010
    Msg011
    Msg012
    Msg013
    Msg014
    Msg015
    Msg016
    Msg017



