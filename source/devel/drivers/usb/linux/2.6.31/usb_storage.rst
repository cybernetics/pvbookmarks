.. module:: LinuxKernel2_6_31_USB_storage
    :synopsis: Sources for the 2.6.31 portux linux USB storage
    :platform: Linux kernel 2.6.31 (portux)
 
 
.. index::
   Matthew Dharm <mdharm-usb@one-eyed-alien.net>
   USB Mass Storage driver for Linux
   
============
usb_storage
============


::

    /* Driver for USB Mass Storage compliant devices
     *
     * Current development and maintenance by:
     *   (c) 1999-2003 Matthew Dharm (mdharm-usb@one-eyed-alien.net)
     *
     * Developed with the assistance of:
     *   (c) 2000 David L. Brown, Jr. (usb-storage@davidb.org)
     *   (c) 2003-2009 Alan Stern (stern@rowland.harvard.edu)
     *
     * Initial work by:
     *   (c) 1999 Michael Gee (michael@linuxspecific.com)
     *
     * usb_device_id support by Adam J. Richter (adam@yggdrasil.com):
     *   (c) 2000 Yggdrasil Computing, Inc.
     *
     * This driver is based on the 'USB Mass Storage Class' document. This
     * describes in detail the protocol used to communicate with such
     * devices.  Clearly, the designers had SCSI and ATAPI commands in
     * mind when they created this document.  The commands are all very
     * similar to commands in the SCSI-II and ATAPI specifications.
     *
     * It is important to note that in a number of cases this class
     * exhibits class-specific exemptions from the USB specification.
     * Notably the usage of NAK, STALL and ACK differs from the norm, in
     * that they are used to communicate wait, failed and OK on commands.
     *
     * Also, for certain devices, the interrupt endpoint is used to convey
     * status of a command.
     *
     * Please see http://www.one-eyed-alien.net/~mdharm/linux-usb for more
     * information about this driver.
     *
     * This program is free software; you can redistribute it and/or modify it
     * under the terms of the GNU General Public License as published by the
     * Free Software Foundation; either version 2, or (at your option) any
     * later version.
     *
     * This program is distributed in the hope that it will be useful, but
     * WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
     * General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License along
     * with this program; if not, write to the Free Software Foundation, Inc.,
     * 675 Mass Ave, Cambridge, MA 02139, USA.
     */

    #include <linux/sched.h>
    #include <linux/errno.h>
    #include <linux/freezer.h>
    #include <linux/module.h>
    #include <linux/init.h>
    #include <linux/slab.h>
    #include <linux/kthread.h>
    #include <linux/mutex.h>
    #include <linux/utsname.h>

    #include <scsi/scsi.h>
    #include <scsi/scsi_cmnd.h>
    #include <scsi/scsi_device.h>

    #include "usb.h"
    #include "scsiglue.h"
    #include "transport.h"
    #include "protocol.h"
    #include "debug.h"
    #include "initializers.h"

    #include "sierra_ms.h"
    #include "option_ms.h"

    /* Some informational data */
    MODULE_AUTHOR("Matthew Dharm <mdharm-usb@one-eyed-alien.net>");
    MODULE_DESCRIPTION("USB Mass Storage driver for Linux");
    MODULE_LICENSE("GPL");

    static unsigned int delay_use = 5;
    module_param(delay_use, uint, S_IRUGO | S_IWUSR);
    MODULE_PARM_DESC(delay_use, "seconds to delay before using a new device");

    static char quirks[128];
    module_param_string(quirks, quirks, sizeof(quirks), S_IRUGO | S_IWUSR);
    MODULE_PARM_DESC(quirks, "supplemental list of device IDs and their quirks");
    
        +---storage
        |       alauda.c
        |       cypress_atacb.c
        |       datafab.c
        |       debug.c
        |       debug.h
        |       freecom.c
        |       initializers.c
        |       initializers.h
        |       isd200.c
        |       jumpshot.c
        |       karma.c
        |       Kconfig
        |       libusual.c
        |       Makefile
        |       onetouch.c
        |       option_ms.c
        |       option_ms.h
        |       protocol.c
        |       protocol.h
        |       scsiglue.c
        |       scsiglue.h
        |       sddr09.c
        |       sddr55.c
        |       shuttle_usbat.c
        |       sierra_ms.c
        |       sierra_ms.h
        |       transport.c
        |       transport.h
        |       unusual_alauda.h
        |       unusual_cypress.h
        |       unusual_datafab.h
        |       unusual_devs.h
        |       unusual_freecom.h
        |       unusual_isd200.h
        |       unusual_jumpshot.h
        |       unusual_karma.h
        |       unusual_onetouch.h
        |       unusual_sddr09.h
        |       unusual_sddr55.h
        |       unusual_usbat.h
        |       usb.c
        |       usb.h
        |       usual-tables.c



 