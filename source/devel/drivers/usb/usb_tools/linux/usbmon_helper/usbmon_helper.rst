.. index::
   pair: USB ; usbmon_helper.py
   ! USBMon helper

.. _usbmon_helper:

=============
usbmon_helper
=============

Thibaut Colar:

- http://wiki.colar.net/
- http://bitbucket.org/tcolar/berry4all/src/tip/src/usmon_helper.py
- http://www.mjmwired.net/kernel/Documentation/usb/usbmon.txt


.. contents::
   :depth: 3

Introduction
============


::

    #!/usr/bin/python
    '''
    Thibaut Colar
    http://wiki.colar.net/
    Quick (&dirty) script that takes in an usbmon log (USB sniffer)
    and dumps out an easier to read html file.

    This is used to debug/rev. engineer USB protocols under linux/unix.
    What it adds to a usbmon log:
    - colors so it's easier to scan through
    - timestamps shown as time offsets - easier to see where we are at
    - data packets shown in ascii as well as hex (ascii helps seing commands)
    etc...

    Example of use::

    Doing an USBMon trace
    =====================

        # mount -t debugfs none_debugs /sys/kernel/debug

    if not in kernel::

        # sudo modprobe usbmon

    cat /sys/kernel/debug/usbmon/4u > /tmp/usb.log
    ==============================================

    If you want to scan a specific device, find it's device number (sudo lsusb)::

        $ cat /sys/kernel/debug/usbmon/4u > /tmp/usb.log

    run some usb transactions of some kind :-) when done kill the
    'cat' command (^c)

    Converting to HTML
    ==================

    # python usbmon_helper.py /tmp/usb.log > /tmp/usb.html
    Open /tmp/usb.html in browser and enjoy !

    USBMon Doc:
    http://www.mjmwired.net/kernel/Documentation/usb/usbmon.txt
    '''


usbmon
======

See :ref:`the documentation about usbmon <usbmon>`.

File outputput example
======================

::

    Time: Time offset from first packet (MM:SS.mmmm)
    Type: S: submission, C: control, E: Error
    Address: Address (URB type and direction, Bus number, Device address, Endpoint nb)
       - URB type and direction:
        Ci Co Control input and output
        Zi Zo Insochronous input and output
        Ii Io Interrupt input and output
        Bi Bo Bulk input and output
    Status: Status Code returned
