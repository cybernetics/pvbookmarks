

.. index::
   smartcard udev rules
   udev smartcard rules
   udevadm control --reload-rules

.. _smartcard_udev_rules:

======================================================
Smartcard udev rules to access to the smartcard reader
======================================================

.. seealso:: :ref:`udev_rules`


In our specific case, we want that any user in the `plugdev` group
can use the id3 smartcard reader.


Create the udev rule file
=========================


Prerequisite
------------

.. seealso:: :ref:`plugdev_group`

You are a 'root' user.


Any user in the ``plugdev`` group will be able to use the CL1356A+ smartcard reader
(VendorId=0x0b81, ProductId=0x0200).


::

    > cd /etc/udev/rules.d
    > udevadm control --reload-rules
    > more 99-id3.rules

::

    ATTRS{idVendor}=="0b81", ATTRS{idProduct}=="0200", SUBSYSTEMS=="usb",  \
    ACTION=="add", MODE="0666", GROUP="plugdev"



/etc/udev/rules.d directory
===========================


::


    drwxr-xr-x 3 root root 4096 2011-04-11 17:06 ./
    drwxr-xr-x 3 root root 4096 2011-01-10 15:35 ../
    -rw-r--r-- 1 root root  906 2011-01-10 16:03 70-persistent-cd.rules
    -rw-r--r-- 1 root root  595 2011-01-10 10:46 70-persistent-net.rules
    -rw-r--r-- 1 root root  115 2011-01-13 11:24 99-id3-fingerprint-reader.rules
    -rw-r--r-- 1 root root  114 2011-04-11 16:57 99-id3-smartcard-reader.rules
    -rw-r--r-- 1 root root 1157 2010-04-19 11:30 README


Test: pluging the CL1356A+ smartcard reader
===========================================

If you type::

    > lsusb

You can see the CL1356A+ reader which is not the case if the user is not
``root`` or is not in the ``plugdev`` group::

    Bus 006 Device 002: ID 0b81:0200 id3 Semiconductors CL1356T / CL1356A / CL1356T5 smartcard readers
    Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 002: ID 0bda:0111 Realtek Semiconductor Corp. Card Reader
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub




