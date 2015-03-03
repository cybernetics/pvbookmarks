

.. index::
   pair: udev ; pcscd


.. _pcscd_uses_libudev_instead_of_libhal:

=========================================
pcscd now uses libudev instead of libhal
=========================================


.. seealso::

   - http://ludovicrousseau.blogspot.com/2011/02/pcscd-now-uses-libudev-instead-of.html
   - :ref:`libpcsclite`


.. contents::
   :depth: 3

Introduction
============

``pcsc-lite`` first started (in the previous century) when only serial readers
were in use.

The serial readers are configured using the /etc/reader.conf file.

The problem is that the configuration is static and can't be used with a USB reader.

History of USB plug-n-play mechanism
=====================================

To detect the insertion or removal of a USB reader different mechanisms have been
used in the last 10 years.

Linux
-----

hotplug_linux.c: introduced at least in (or before) version 1.0.2beta2 (20 Dec, 2001).

The problem is that the code is Linux specific.

libusb
------

**hotplug_libusb.c**
    introduced in version 1.2.0-rc1 (26 August, 2003).
    From the changelog:

    - src/hotplug_libusb.c: Add support of libusb. Allow to use USB readers on
      BSD or any plateform supported by libusb.
      Thanks to Toni Andjelkovic for the great job.


The problem of libusb is that pcscd is constantly polling the USB bus to detect
reader hotplug.

libhal
------

**hotplug_libhal.c**
   introduced in version 1.4.100 (23 March 2008).

   From the changelog:

   - add libhal support to avoid polling the USB bus.
     libusb is still supported but libhal is now the default

The problem is that `libhal has been deprecated`_ upstream in May 2008
(**2 months  after pcscd started using it !**).

Some distributions are actively migrating out of libhal.

See Debian bug 587979_ "pcscd: uses deprecated HAL" for example.
And the wiki page HALRemoval_.


.. _587979:  http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=587979
.. _HALRemoval:  https://wiki.debian.org/HALRemoval
.. _`libhal has been deprecated`: http://lists.freedesktop.org/archives/hal/2008-May/011560.html


.. _libudev_pcsc:

libudev
-------

**hotplug_libudev.c**
    introduced in version 1.6.8 (not yet released as of February 2011).

It looks like :ref:`libudev <udev>` is a good choice for the future.
I don't know if it is supported by other systems than GNU/Linux. I removed the
support of libhal but support of libusb is still present.


.. seealso::

   - :ref:`udev_versus_devfs`
   - http://en.wikipedia.org/wiki/Udev
   - http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html

Mac OS X
========

Mac OS X has its own hotplug mechanism in hotplug_macosx.c.
Apple maintains its own forked version of pcsc-lite. So I do not plan to change
anything Mac OS X specific in pcsc-lite.

Conclusion
==========


The hotplug mechanism is a fast moving target on GNU/Linux.
I hope libudev will last at least a few months before I have to move to something
else.
