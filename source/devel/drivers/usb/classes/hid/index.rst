.. index::
   pair: USB ; HID
   ! HID

.. _usb_hid:

==================================
USB HID (Human Interface Device)
==================================


.. seealso::

   - http://en.wikipedia.org/wiki/USB_human_interface_device_class
   - http://www.usb.org/developers/hidpage/
   - http://www.usb.org/developers/devclass_docs/HID1_11.pdf
   - https://github.com/bfoz/libhid/
   - http://www.wooji-juice.com/free/pyhid/readme.html

   - :ref:`usb_hid_linux_2_6_31`

.. contents::
   :depth: 3

Device Class Definition HID
===========================

The Device Class Definition for HID 1.11 is intended to supplement the USB
Specification and provide HID manufacturers with the information necessary to
build USB-compatible devices.

It also specifies how the HID class driver should extract data from USB devices.

The primary and underlying goals of the HID class definition are to:

- be as compact as possible to save device data space
- allow the software application to skip unknown information
- be extensible and robust
- support nesting and collections
- be self-describing to allow generic software applications

Introduction
============

.. seealso::

   - http://www.frank-zhao.com/cache/hid_tutorial_1.php
   - http://www.usb.org/developers/devclass_docs/HID1_11.pdf


This document describes the Human Interface Device (HID) class for use with
Universal Serial Bus (USB). Concepts from the USB Specification are used but
not explained in this document


The HID class consists primarily of devices that are used by humans to control
the operation of computer systems. Typical examples of HID class devices
include:

- Keyboards and pointing devices—for example, standard mouse devices,
  trackballs, and joysticks.
- Front-panel controls—for example: knobs, switches, buttons, and sliders.
- Controls that might be found on devices such as telephones, VCR remote
  controls, games or simulation devices—for example: data gloves, throttles,
  steering wheels, and rudder pedals.
- Devices that may not require human interaction but provide data in a similar
  format to HID class devices—for example, bar-code readers, thermometers, or
  voltmeters.
- Many typical HID class devices include indicators, specialized displays, audio
  feedback, and force or tactile feedback. Therefore, the HID class definition
  includes support for various types of output directed to the end user


   - http://www.alanmacek.com/usb/
   - https://github.com/bfoz/libhid/


USB and Human Interface Devices (HID)
=====================================

Human Interface Devices (HID) are a class of USB devices that give structure to
the data that will transfered between the device and the host computer.
During the enumeration process, the device describes the information that
it can receive and send.  This allows a host computer to handle the data
being received from the USB device without requiring a specially
designed device driver.

.. index::
   HID class
   HID descriptor tool

HID class
---------

The HID class is supposed to include devices such as a mouse, joystick,
keyboard, etc. Because the host computer knows what the data means a
device driver is not necessary for HID devices, the operating system
can supply a generic HID driver. For instance, if you plug in a USB Mouse,
it will immediately work because the OS knows how to interpret
information received from a mouse.

Information on the HID class can be found at http://www.usb.org/developers/hidpage.
You can see examples of HID descriptors starting on page 89 of the HID 1.1
spec from http://usb.org.

A very useful tool for designing HID class devices is the HID Descriptor
Tool also available from http://usb.org. This tool allows you to put together
the HID description and run it through the HID parser.

Some other useful tools are available from Intel University Press.
They include 'USB Single Step', 'USBView', 'HIDView' and the
HID Descriptor Tool described above.

If you are using Visual C++, then the 'hview' sample program that
comes with the Windows DDK is good for examining the HID descriptor
and values. Unfortunately the program is more complicated than
it needs to be and is not a good example of using the USB functions.

Links
=====

TtyLinux
--------

- http://www.linux-magazine.com/Online/News/Ttylinux-9.1-Supports-USB-HID (Jan 11, 2010)

The very frugal ttylinux distro is available in version 9.1.

The newest aspect of ttylinux is that the kernel now supports
USB Human Interface Devices (HID), which primarily serve in
connecting USB keyboards. It also has a new init script and
config files for the cron daemon.

The resource-saving ttylinux is ready-made for i486 machines
with 24 MBytes RAM in Live memory. A hard drive installation
requires only 8 MBytes disk space and 16 MBytes RAM.
The Linux distro also supports Intel 64-bit CPUs.

Ttylinux 9.1 is available for download from the project
page as ISO images and source code archive.



HID Tutorials
==============

.. seealso::

   - http://www.frank-zhao.com/cache/hid_tutorial_1.php
   - http://www.tracesystemsinc.com/USB_Tutorials_web/USB/B1_USB_Classes/Books/A3_A_Closer_Look_at_HID_Class/sbook2.htm


http://www.tracesystemsinc.com/USB_Tutorials_web/USB/B1_USB_Classes/Books/A3_A_Closer_Look_at_HID_Class/sbook2.htm
------------------------------------------------------------------------------------------------------------------

HID devices can be used for all sorts of applications, like these:

- data acquisition devices
- test instruments
- data loggers
- devices to control hardware
- display devices,
- and of course keyboards, mice, and joysticks.



In fact, just about any kind of device that doesn't already fit into some other
existing USB class, and in which a 64,000 byte per second data rate is acceptable,
can usually be done better, faster, and more intelligently as a USB HID class device.

And it will never require a special device driver to be installed, either.


HID Libraries
=============

.. toctree::
   :maxdepth: 3

   libraries/index






