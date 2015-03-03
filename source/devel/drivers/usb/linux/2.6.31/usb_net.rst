.. module:: LinuxKernel2_6_31_USB_net
    :synopsis: Sources for the 2.6.31 portux linux USB net
    :platform: Linux kernel 2.6.31 (portux)
 
.. index::
   usbnet
   
   
=======
usbnet
=======

::


    /*
     * USB Network driver infrastructure
     * Copyright (C) 2000-2005 by David Brownell
     * Copyright (C) 2003-2005 David Hollis <dhollis@davehollis.com>
     *
     * This program is free software; you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation; either version 2 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program; if not, write to the Free Software
     * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
     */

    /*
     * This is a generic "USB networking" framework that works with several
     * kinds of full and high speed networking devices:  host-to-host cables,
     * smart usb peripherals, and actual Ethernet adapters.
     *
     * These devices usually differ in terms of control protocols (if they
     * even have one!) and sometimes they define new framing to wrap or batch
     * Ethernet packets.  Otherwise, they talk to USB pretty much the same,
     * so interface (un)binding, endpoint I/O queues, fault handling, and other
     * issues can usefully be addressed by this framework.
     */
    // #define	DEBUG			// error path messages, extra info
    // #define	VERBOSE			// more; success messages

    #include <linux/module.h>
    #include <linux/init.h>
    #include <linux/netdevice.h>
    #include <linux/etherdevice.h>
    #include <linux/ctype.h>
    #include <linux/ethtool.h>
    #include <linux/workqueue.h>
    #include <linux/mii.h>
    #include <linux/usb.h>
    #include <linux/usb/usbnet.h>
    #define DRIVER_VERSION		"22-Aug-2005"

    /*-------------------------------------------------------------------------*/

    /*
     * Nineteen USB 1.1 max size bulk transactions per frame (ms), max.
     * Several dozen bytes of IPv4 data can fit in two such transactions.
     * One maximum size Ethernet packet takes twenty four of them.
     * For high speed, each frame comfortably fits almost 36 max size
     * Ethernet packets (so queues should be bigger).
     *
     * REVISIT qlens should be members of 'struct usbnet'; the goal is to
     * let the USB host controller be busy for 5msec or more before an irq
     * is required, under load.  Jumbograms change the equation.
     */
    #define RX_MAX_QUEUE_MEMORY (60 * 1518)
    #define	RX_QLEN(dev) (((dev)->udev->speed == USB_SPEED_HIGH) ? \
                (RX_MAX_QUEUE_MEMORY/(dev)->rx_urb_size) : 4)
    #define	TX_QLEN(dev) (((dev)->udev->speed == USB_SPEED_HIGH) ? \
                (RX_MAX_QUEUE_MEMORY/(dev)->hard_mtu) : 4)

    // reawaken network queue this soon after stopping; else watchdog barks
    #define TX_TIMEOUT_JIFFIES	(5*HZ)

    // throttle rx/tx briefly after some faults, so khubd might disconnect()
    // us (it polls at HZ/4 usually) before we report too many false errors.
    #define THROTTLE_JIFFIES	(HZ/8)

    // between wakeups
    #define UNLINK_TIMEOUT_MS	3

    /*-------------------------------------------------------------------------*/
    // randomly generated ethernet address
    static u8	node_id [ETH_ALEN];

    static const char driver_name [] = "usbnet";
    
    +---net
    |   \---usb
    |           asix.c
    |           catc.c
    |           cdc-phonet.c
    |           cdc_eem.c
    |           cdc_ether.c
    |           cdc_subset.c
    |           dm9601.c
    |           gl620a.c
    |           hso.c
    |           int51x1.c
    |           kaweth.c
    |           Kconfig
    |           Makefile
    |           mcs7830.c
    |           net1080.c
    |           pegasus.c
    |           pegasus.h
    |           plusb.c
    |           rndis_host.c
    |           rtl8150.c
    |           smsc95xx.c
    |           smsc95xx.h
    |           usbnet.c
    |           zaurus.c