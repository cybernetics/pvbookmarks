
.. index::
   pair: udev ; fingerprint rules



.. _fingerprint_udev_rules:

======================
fingerprint udev rules
======================

.. seealso:: :ref:`udev_rules`


In our specific case, we want that any user in the `plugdev` group
can use the id3 certis2 fingerprint reader.



Create the udev rule
====================

Any user in the ``plugdev`` group will be able to use the Certis2.


::

    > cd /etc/udev/rules.d
    > udevadm control --reload-rules
    > more 99-id3-fingerprint-reader.rules

::

    ATTRS{idVendor}=="0b81", ATTRS{idProduct}=="0103", SUBSYSTEMS=="usb", \
    ACTION=="add", MODE="0666", GROUP="plugdev"


Test
=====

If you type::

    > lsusb

You can see the Certis2 reader which is not the case if the user is not
``root`` or is not in the ``plugdev`` group::

    Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 011: ID 0b81:0103 id3 Semiconductors Certis V2 fingerprint reader
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 003: ID 0bda:0111 Realtek Semiconductor Corp. Card Reader
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub




