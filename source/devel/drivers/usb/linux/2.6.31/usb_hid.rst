

.. index::
   pair: USB ; HID


.. _usb_hid_linux_2_6_31:

=====================
USB HID Linux 2.6.31
=====================


.. seealso::

   - :ref:`usb_hid`


::

    /*
     *  USB HID support for Linux
     *
     *  Copyright (c) 1999 Andreas Gal
     *  Copyright (c) 2000-2005 Vojtech Pavlik <vojtech@suse.cz>
     *  Copyright (c) 2005 Michael Haboustak <mike-@cinci.rr.com> for Concept2, Inc
     *  Copyright (c) 2006-2008 Jiri Kosina
     *  Copyright (c) 2007-2008 Oliver Neukum
     */

    /*
     * This program is free software; you can redistribute it and/or modify it
     * under the terms of the GNU General Public License as published by the Free
     * Software Foundation; either version 2 of the License, or (at your option)
     * any later version.
     */

    #include <linux/module.h>
    #include <linux/slab.h>
    #include <linux/init.h>
    #include <linux/kernel.h>
    #include <linux/list.h>
    #include <linux/mm.h>
    #include <linux/mutex.h>
    #include <linux/spinlock.h>
    #include <asm/unaligned.h>
    #include <asm/byteorder.h>
    #include <linux/input.h>
    #include <linux/wait.h>
    #include <linux/workqueue.h>

    #include <linux/usb.h>

    #include <linux/hid.h>
    #include <linux/hiddev.h>
    #include <linux/hid-debug.h>
    #include <linux/hidraw.h>
    #include "usbhid.h"

    /*
     * Version Information
     */

    #define DRIVER_VERSION "v2.6"
    #define DRIVER_AUTHOR "Andreas Gal, Vojtech Pavlik, Jiri Kosina"
    #define DRIVER_DESC "USB HID core driver"
    #define DRIVER_LICENSE "GPL"

    +---hid
    |   |   hid-a4tech.c
    |   |   hid-apple.c
    |   |   hid-belkin.c
    |   |   hid-cherry.c
    |   |   hid-chicony.c
    |   |   hid-core.c
    |   |   hid-cypress.c
    |   |   hid-debug.c
    |   |   hid-drff.c
    |   |   hid-ezkey.c
    |   |   hid-gaff.c
    |   |   hid-gyration.c
    |   |   hid-ids.h
    |   |   hid-input.c
    |   |   hid-kensington.c
    |   |   hid-kye.c
    |   |   hid-lg.c
    |   |   hid-lg.h
    |   |   hid-lg2ff.c
    |   |   hid-lgff.c
    |   |   hid-microsoft.c
    |   |   hid-monterey.c
    |   |   hid-ntrig.c
    |   |   hid-petalynx.c
    |   |   hid-pl.c
    |   |   hid-samsung.c
    |   |   hid-sjoy.c
    |   |   hid-sony.c
    |   |   hid-sunplus.c
    |   |   hid-tmff.c
    |   |   hid-topseed.c
    |   |   hid-wacom.c
    |   |   hid-zpff.c
    |   |   hidraw.c
    |   |   Kconfig
    |   |   Makefile
    |   |
    |   \---usbhid
    |           hid-core.c
    |           hid-pidff.c
    |           hid-quirks.c
    |           hiddev.c
    |           Kconfig
    |           Makefile
    |           usbhid.h
    |           usbkbd.c
    |           usbmouse.c
