.. module:: LinuxKernel2_6_31_USBSrc
    :synopsis: Sources for the 2.6.31 portux linux USB drivers
    :platform: Linux kernel 2.6.31 (portux)
 

..  _linux_2_6_31_drivers_usb_sources:
  
========================
Linux 2.6.31 USB sources
========================

.. index::
   usb-skeleton
   USB host
   UHCI
   OHCI
   EHCI  
   USB host UHCI OHCI EHCI

::


    |   +---usb
    |   |   |   Kconfig
    |   |   |   Makefile
    |   |   |   README
    |   |   |   usb-skeleton.c
    |   |   |   
    |   |   +---atm
    |   |   |       cxacru.c
    |   |   |       Kconfig
    |   |   |       Makefile
    |   |   |       speedtch.c
    |   |   |       ueagle-atm.c
    |   |   |       usbatm.c
    |   |   |       usbatm.h
    |   |   |       xusbatm.c
    |   |   |       
    |   |   +---c67x00
    |   |   |       c67x00-drv.c
    |   |   |       c67x00-hcd.c
    |   |   |       c67x00-hcd.h
    |   |   |       c67x00-ll-hpi.c
    |   |   |       c67x00-sched.c
    |   |   |       c67x00.h
    |   |   |       Makefile
    |   |   |       
    |   |   +---class
    |   |   |       cdc-acm.c
    |   |   |       cdc-acm.h
    |   |   |       cdc-wdm.c
    |   |   |       Kconfig
    |   |   |       Makefile
    |   |   |       usblp.c
    |   |   |       usbtmc.c
    |   |   |       
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
    |   |   |       
    |   |   +---gadget
    |   |   |       amd5536udc.c
    |   |   |       amd5536udc.h
    |   |   |       at91_udc.c
    |   |   |       at91_udc.h
    |   |   |       atmel_usba_udc.c
    |   |   |       atmel_usba_udc.h
    |   |   |       audio.c
    |   |   |       cdc2.c
    |   |   |       ci13xxx_udc.c
    |   |   |       ci13xxx_udc.h
    |   |   |       composite.c
    |   |   |       config.c
    |   |   |       dummy_hcd.c
    |   |   |       epautoconf.c
    |   |   |       ether.c
    |   |   |       file_storage.c
    |   |   |       fsl_mx3_udc.c
    |   |   |       fsl_qe_udc.c
    |   |   |       fsl_qe_udc.h
    |   |   |       fsl_udc_core.c
    |   |   |       fsl_usb2_udc.h
    |   |   |       f_acm.c
    |   |   |       f_audio.c
    |   |   |       f_ecm.c
    |   |   |       f_loopback.c
    |   |   |       f_obex.c
    |   |   |       f_phonet.c
    |   |   |       f_rndis.c
    |   |   |       f_serial.c
    |   |   |       f_sourcesink.c
    |   |   |       f_subset.c
    |   |   |       gadget_chips.h
    |   |   |       gmidi.c
    |   |   |       goku_udc.c
    |   |   |       goku_udc.h
    |   |   |       g_zero.h
    |   |   |       imx_udc.c
    |   |   |       imx_udc.h
    |   |   |       inode.c
    |   |   |       Kconfig
    |   |   |       langwell_udc.c
    |   |   |       langwell_udc.h
    |   |   |       lh7a40x_udc.c
    |   |   |       lh7a40x_udc.h
    |   |   |       m66592-udc.c
    |   |   |       m66592-udc.h
    |   |   |       Makefile
    |   |   |       ndis.h
    |   |   |       net2280.c
    |   |   |       net2280.h
    |   |   |       omap_udc.c
    |   |   |       omap_udc.h
    |   |   |       printer.c
    |   |   |       pxa25x_udc.c
    |   |   |       pxa25x_udc.h
    |   |   |       pxa27x_udc.c
    |   |   |       pxa27x_udc.h
    |   |   |       rndis.c
    |   |   |       rndis.h
    |   |   |       s3c-hsotg.c
    |   |   |       s3c2410_udc.c
    |   |   |       s3c2410_udc.h
    |   |   |       serial.c
    |   |   |       usbstring.c
    |   |   |       u_audio.c
    |   |   |       u_audio.h
    |   |   |       u_ether.c
    |   |   |       u_ether.h
    |   |   |       u_phonet.h
    |   |   |       u_serial.c
    |   |   |       u_serial.h
    |   |   |       zero.c
    |   |   |  
    |   |   +---host
    |   |   |   |   ehci-au1xxx.c
    |   |   |   |   ehci-dbg.c
    |   |   |   |   ehci-fsl.c
    |   |   |   |   ehci-fsl.h
    |   |   |   |   ehci-hcd.c
    |   |   |   |   ehci-hub.c
    |   |   |   |   ehci-ixp4xx.c
    |   |   |   |   ehci-mem.c
    |   |   |   |   ehci-orion.c
    |   |   |   |   ehci-pci.c
    |   |   |   |   ehci-ppc-of.c
    |   |   |   |   ehci-ps3.c
    |   |   |   |   ehci-q.c
    |   |   |   |   ehci-sched.c
    |   |   |   |   ehci.h
    |   |   |   |   fhci-dbg.c
    |   |   |   |   fhci-hcd.c
    |   |   |   |   fhci-hub.c
    |   |   |   |   fhci-mem.c
    |   |   |   |   fhci-q.c
    |   |   |   |   fhci-sched.c
    |   |   |   |   fhci-tds.c
    |   |   |   |   fhci.h
    |   |   |   |   hwa-hc.c
    |   |   |   |   isp116x-hcd.c
    |   |   |   |   isp116x.h
    |   |   |   |   isp1760-hcd.c
    |   |   |   |   isp1760-hcd.h
    |   |   |   |   isp1760-if.c
    |   |   |   |   Kconfig
    |   |   |   |   Makefile
    |   |   |   |   ohci-at91.c
    |   |   |   |   ohci-au1xxx.c
    |   |   |   |   ohci-dbg.c
    |   |   |   |   ohci-ep93xx.c
    |   |   |   |   ohci-hcd.c
    |   |   |   |   ohci-hub.c
    |   |   |   |   ohci-lh7a404.c
    |   |   |   |   ohci-mem.c
    |   |   |   |   ohci-omap.c
    |   |   |   |   ohci-pci.c
    |   |   |   |   ohci-pnx4008.c
    |   |   |   |   ohci-pnx8550.c
    |   |   |   |   ohci-ppc-of.c
    |   |   |   |   ohci-ppc-soc.c
    |   |   |   |   ohci-ps3.c
    |   |   |   |   ohci-pxa27x.c
    |   |   |   |   ohci-q.c
    |   |   |   |   ohci-s3c2410.c
    |   |   |   |   ohci-sa1111.c
    |   |   |   |   ohci-sh.c
    |   |   |   |   ohci-sm501.c
    |   |   |   |   ohci-ssb.c
    |   |   |   |   ohci-tmio.c
    |   |   |   |   ohci.h
    |   |   |   |   oxu210hp-hcd.c
    |   |   |   |   oxu210hp.h
    |   |   |   |   pci-quirks.c
    |   |   |   |   pci-quirks.h
    |   |   |   |   r8a66597-hcd.c
    |   |   |   |   r8a66597.h
    |   |   |   |   sl811-hcd.c
    |   |   |   |   sl811.h
    |   |   |   |   sl811_cs.c
    |   |   |   |   u132-hcd.c
    |   |   |   |   uhci-debug.c
    |   |   |   |   uhci-hcd.c
    |   |   |   |   uhci-hcd.h
    |   |   |   |   uhci-hub.c
    |   |   |   |   uhci-q.c
    |   |   |   |   xhci-dbg.c
    |   |   |   |   xhci-ext-caps.h
    |   |   |   |   xhci-hcd.c
    |   |   |   |   xhci-hub.c
    |   |   |   |   xhci-mem.c
    |   |   |   |   xhci-pci.c
    |   |   |   |   xhci-ring.c
    |   |   |   |   xhci.h
    |   |   |   |   
    |   |   |   \---whci
    |   |   |           asl.c
    |   |   |           debug.c
    |   |   |           hcd.c
    |   |   |           hw.c
    |   |   |           init.c
    |   |   |           int.c
    |   |   |           Kbuild
    |   |   |           pzl.c
    |   |   |           qset.c
    |   |   |           whcd.h
    |   |   |           whci-hc.h
    |   |   |           wusb.c
    |   |   |           
    |   |   +---image
    |   |   |       Kconfig
    |   |   |       Makefile
    |   |   |       mdc800.c
    |   |   |       microtek.c
    |   |   |       microtek.h
    |   |   |       
    |   |   +---misc
    |   |   |   |   adutux.c
    |   |   |   |   appledisplay.c
    |   |   |   |   berry_charge.c
    |   |   |   |   cypress_cy7c63.c
    |   |   |   |   cytherm.c
    |   |   |   |   emi26.c
    |   |   |   |   emi62.c
    |   |   |   |   ftdi-elan.c
    |   |   |   |   idmouse.c
    |   |   |   |   iowarrior.c
    |   |   |   |   isight_firmware.c
    |   |   |   |   Kconfig
    |   |   |   |   ldusb.c
    |   |   |   |   legousbtower.c
    |   |   |   |   Makefile
    |   |   |   |   rio500.c
    |   |   |   |   rio500_usb.h
    |   |   |   |   trancevibrator.c
    |   |   |   |   usblcd.c
    |   |   |   |   usbled.c
    |   |   |   |   usbsevseg.c
    |   |   |   |   usbtest.c
    |   |   |   |   usb_u132.h
    |   |   |   |   uss720.c
    |   |   |   |   vstusb.c
    |   |   |   |   
    |   |   |   \---sisusbvga
    |   |   |           Kconfig
    |   |   |           Makefile
    |   |   |           sisusb.c
    |   |   |           sisusb.h
    |   |   |           sisusb_con.c
    |   |   |           sisusb_init.c
    |   |   |           sisusb_init.h
    |   |   |           sisusb_struct.h
    
    
    
To understand all the Linux-USB framework
=========================================

To understand all the Linux-USB framework, you'll use these resources:

* This source code.  This is necessarily an evolving work, and
  includes kerneldoc that should help you get a current overview.
  ("make pdfdocs", and then look at "usb.pdf" for host side and
  "gadget.pdf" for peripheral side.)  Also, Documentation/usb has
  more information.

* The USB 2.0 specification (from http://www.usb.org), with supplements
  such as those for USB OTG and the various device classes.
  The USB specification has a good overview chapter, and USB
  peripherals conform to the widely known "Chapter 9".

* Chip specifications for USB controllers.  
  Examples include:
  
  - host controllers (on PCs, servers, and more)
  - peripheral controllers (in devices with Linux firmware, like printers or
    cell phones); 
  - and hard-wired peripherals like Ethernet adapters.

* Specifications for other protocols implemented by USB peripheral
  functions.  Some are vendor-specific; others are vendor-neutral
  but just standardized outside of the www.usb.org team.

Here is a list of what each subdirectory here is, and what is contained in
them:

core
----

This is for the core USB host code, including the usbfs files and the 
hub class driver ("khubd").

host
----

This is for USB host controller drivers.  This
includes:

* UHCI, 
* OHCI, 
* EHCI, 
* and others that might be used with more specialized "embedded" systems.

gadget
------

This is for USB peripheral controller drivers and the various gadget drivers 
which talk to them.


image
-----

This is for still image drivers, like scanners or digital cameras.
  
input
-----

This is for any driver that uses the input subsystem, like keyboard, mice, 
touchscreens, tablets, etc.
  
.. index::
   v4l video for linux
   
media
-----

This is for multimedia drivers, like video cameras, radios, and any other 
drivers that talk to the v4l subsystem.


net/usb 
-------

This is for network drivers.


serial
------  

This is for USB to serial drivers.


storage
-------

This is for USB mass-storage drivers.

class
-----

This is for all USB device drivers that do not fit into any of the above 
categories, and work for a range of USB Class specified devices. 
  
misc
----

This is for all USB device drivers that do not fit into any of the above 
categories.

  
Linux-USB sub-directories
=========================

.. toctree::
   :maxdepth: 2
    
   usb_core
   usb_storage
   usb_net
   usb_hid
   usb_image
   
   
   
   
   
    
    
