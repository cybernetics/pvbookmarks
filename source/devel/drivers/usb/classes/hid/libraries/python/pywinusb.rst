

.. index::
   pair: HID; pywinusb


.. _pywinusb:

=====================
pywinusb
=====================


.. seealso::

   - http://pypi.python.org/pypi/pywinusb/
   - https://github.com/rene-aguirre/pywinusb


.. contents::
   :depth: 3

Introduction
============

This project aims to be a simple USB/HID user application space (hence no system
drivers needed) 100% python package (without C extensions). Initially targeting
simple HID devices management.

The vision for this project is to be something similar to PySerial or PyParallel
but for USB/HID hardware enthusiasts.


Advantages
==========


- All python code, using ctypes
- Top level handling of HID events (usage events calling hook function handlers)



