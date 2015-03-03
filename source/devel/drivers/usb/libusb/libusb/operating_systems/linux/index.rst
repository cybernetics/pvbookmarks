

.. index::
   pair: Libusb ; 1.0


.. _libusb_linux:

================
libusb 1.0 linux
================

.. contents::
   :depth: 3


C library for writing portable USB drivers in userspace.

Sources
=======


- http://git.libusb.org/
- http://git.libusb.org/?p=libusb.git;a=summary
- http://ldn.linuxfoundation.org/book/53-patch-preparation


http://libusb.sourceforge.net/api-1.0/
======================================

Introduction
------------

**libusb is an open source library that allows you to communicate with USB
devices from userspace.**

It's possible to write USB driver is userspace. See the :ref:`usb_driver_API_moves_to_EXPORT_SYMBOL_GPL`


This documentation is aimed at application developers wishing to communicate
with USB peripherals from their own software. After reviewing this
documentation, feedback and questions can be sent to the libusb-devel
mailing list.

This documentation assumes knowledge of how to operate USB devices from
a software standpoint (descriptors, configurations, interfaces, endpoints,
control/bulk/interrupt/isochronous transfers, etc).

.. seealso::

   - http://sourceforge.net/projects/libusb/files/libusb-1.0/
   - http://git.libusb.org/
   - http://git.libusb.org/?p=libusb.git;a=summary
   - http://ldn.linuxfoundation.org/book/53-patch-preparation
   - http://www.linux-mips.org/wiki/The_perfect_patch
   - http://userweb.kernel.org/~akpm/stuff/tpp.txt (inspiration for the above)
   - http://lkml.indiana.edu/hypermail/linux/kernel/0801.0/0373.html
   - http://lwn.net/Articles/160191/
   - http://www.usbmadesimple.co.uk/index.html


.. index::
   pair: isochronous; libusb


Library features
----------------

- All transfer types supported (control/bulk/interrupt/isochronous)
- 2 transfer interfaces:

    1. Synchronous (simple)
    2. Asynchronous (more complicated, but more powerful)

- Thread safe (although the asynchronous interface means that you usually won't need to thread)
- Lightweight with lean API
- Compatible with libusb-0.1 through the libusb-compat-0.1 translation layer


.. index::
   pair: USB ;  root permission

libusb and root permission (libusb and udev)
============================================

.. seealso::

   - http://code.google.com/p/picusb/wiki/libusb_and_udev


One issue about libusb under Linux and BSDs is how to run the program
without using the root privilege.

Under Linux, the standard solution is to use udev rules.

Here are some good references about udev:

- udev homepage http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
- Writing udev rules http://www.reactivated.net/udevrules.php
- Proper place to ask questions about udev rules http://vger.kernel.org/vger-lists.html#linux-hotplug
- http://www.gphoto.org/doc/manual/permissions-usb.html


libusb installation
===================

.. toctree::
   :maxdepth: 2

   install/index


Other libraries using libusb
=============================

.. toctree::
   :maxdepth: 2

   libfprint/index









