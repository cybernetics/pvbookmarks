
.. index::
   pair: Libusb ; 1.0
   ! Libusb


.. _Libusb:
.. _Libusb_1.0:

===========
Libusb
===========


.. seealso::

   - http://libusb.info/


.. contents::
   :depth: 3


Introduction
=============

**Libusb is a library for USB device access from Linux userspace.**

libusb is a C library that provides generic access to USB devices. 

It is intended to be used by developers to facilitate the production of applications 
that communicate with USB hardware.

It is portable: Using a single cross-platform API, it provides access to USB 
devices on Linux, OS X, Windows and OpenBSD.

It is user-mode: No special privilege or elevation is required for the 
application to communicate with a device.

It is version-agnostic: All versions of the USB protocol, from 1.0 to 3.0 
(latest), are supported.


.. seealso:: :ref:`pyusb_module`


Warning
========


.. warning:: libusbx was a fork of libusb, a library that provides generic 
   access to USB devices.

   As of 2014.01.26, this project has been fully merged back into libusb and is 
   being discontinued.

   Since there will be no further releases of libusbx, you are strongly 
   encouraged to switch to using libusb. 


What platforms are currently supported ?
=========================================

Linux, OS X, Windows, Windows CE, Android, OpenBSD/NetBSD.


Libusb source code
==================

.. seealso::

   - https://github.com/libusb/libusb


Libusb tutorials
=================


.. toctree::
   :maxdepth: 2


   libusb_tutorials

Libusb people
==============


.. toctree::
   :maxdepth: 2


   people/index


Libusb on OS
==============


.. toctree::
   :maxdepth: 2


   operating_systems/index



Libusb versions
===============

.. toctree::
   :maxdepth: 2

   versions/index

