
.. index::
   pair: hidapi; HID


.. hidapi:

===========
hidapi
===========

.. seealso::

   - http://www.signal11.us/oss/hidapi/
   - https://github.com/signal11/hidapi

.. contents::
   :depth: 3



Introduction
==============

HIDAPI is a multi-platform library which allows an application to interface with
USB and Bluetooth HID-Class devices on Windows, Linux, and Mac OS X.

While it can be used to communicate with standard HID devices like keyboards,
mice, and Joysticks, it is most useful when used with custom (Vendor-Defined)
HID devices.
Many devices do this in order to not require a custom driver to be written for
each platform.

HIDAPI is easy to integrate with the client application, just requiring a single
source file to be dropped into the application. On Windows, HIDAPI can optionally
be built into a DLL.

