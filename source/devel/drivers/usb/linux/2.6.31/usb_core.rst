.. module:: LinuxKernel2_6_31_USB_core
    :synopsis: Sources for the 2.6.31 portux linux USB core
    :platform: Linux kernel 2.6.31 (portux)
 

=======
usbcore
=======


This is for the core USB host code, including the usbfs files and the 
hub class driver ("khubd").

::

    /*
     * drivers/usb/core/usb.c
     *
     * (C) Copyright Linus Torvalds 1999
     * (C) Copyright Johannes Erdfelt 1999-2001
     * (C) Copyright Andreas Gal 1999
     * (C) Copyright Gregory P. Smith 1999
     * (C) Copyright Deti Fliegl 1999 (new USB architecture)
     * (C) Copyright Randy Dunlap 2000
     * (C) Copyright David Brownell 2000-2004
     * (C) Copyright Yggdrasil Computing, Inc. 2000
     *     (usb_device_id matching changes by Adam J. Richter)
     * (C) Copyright Greg Kroah-Hartman 2002-2003
     *
     * NOTE! This is not actually a driver at all, rather this is
     * just a collection of helper routines that implement the
     * generic USB things that the real drivers can use..
     *
     * Think of this as a "USB library" rather than anything else.
     * It should be considered a slave, with no callbacks. Callbacks
     * are evil.
     */

    #include <linux/module.h>
    #include <linux/moduleparam.h>
    #include <linux/string.h>
    #include <linux/bitops.h>
    #include <linux/slab.h>
    #include <linux/interrupt.h>  /* for in_interrupt() */
    #include <linux/kmod.h>
    #include <linux/init.h>
    #include <linux/spinlock.h>
    #include <linux/errno.h>
    #include <linux/usb.h>
    #include <linux/mutex.h>
    #include <linux/workqueue.h>
    #include <linux/debugfs.h>

    #include <asm/io.h>
    #include <linux/scatterlist.h>
    #include <linux/mm.h>
    #include <linux/dma-mapping.h>

    #include "hcd.h"
    #include "usb.h"


    const char *usbcore_name = "usbcore";

        |   |   +---core
        |   |   |       buffer.c
        |   |   |       config.c
        |   |   |       devices.c
        |   |   |       devio.c
        |   |   |       driver.c
        |   |   |       endpoint.c
        |   |   |       file.c
        |   |   |       generic.c
        |   |   |       hcd-pci.c
        |   |   |       hcd.c
        |   |   |       hcd.h
        |   |   |       hub.c
        |   |   |       hub.h
        |   |   |       inode.c
        |   |   |       Kconfig
        |   |   |       Makefile
        |   |   |       message.c
        |   |   |       notify.c
        |   |   |       otg_whitelist.h
        |   |   |       quirks.c
        |   |   |       sysfs.c
        |   |   |       urb.c
        |   |   |       usb.c
        |   |   |       usb.h




 