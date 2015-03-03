.. module:: USB-ip
    :synopsis: USB ip


.. index::
   USB IP
   
======
USB IP
======  

usbip
=====

http://usbip.sourceforge.net/

The USB/IP Project aims to develop a general USB device sharing system 
over IP network. To share USB devices between computers with their full 
functionality, USB/IP encapsulates "USB I/O messages" into TCP/IP 
payloads and transmits them between computers. Original USB device drivers 
and applications can be also used for remote USB devices without any 
modification of them. A computer can use remote USB devices as if 
they were directly attached; for example, we can ...

* USB storage devices: fdisk, mkfs, mount/umount, file operations, play a DVD 
  movie and record a DVD-R media.
* USB keyboards and USB mice: use with linux console and X Window System.
* USB webcams and USB speakers: view webcam, capture image data and play some music.
* USB printers, USB scanners, USB serial converters and USB Ethernet interfaces: ok, use fine. 

It is currently implemented as Linux device drivers and available under the 
open source license GPL. Its I/O performance is enough practical in local 
area network for all types of devices, including isochronous devices, without 
any modification of Linux-original USB device drivers. 


.. index::
   http://code.google.com/p/ctypesgen/
   http://code.google.com/p/pyusbip/

pyusbip
=======


This project provides a Python wrapper for the USB/IP shared library. 
The wrapper was generated using ctypesgen (http://code.google.com/p/ctypesgen/). 
The goal this project is to maintain these wrappers and provide GUI (pygtk) 
tools for server-side and client-side USB/IP userland operations.

This project is still in its larval stage :)


http://code.google.com/p/pyusbip/

http://sourceforge.net/mailarchive/forum.php?thread_name=20091006201933.GD4731%40novell.com&forum_name=usbip-devel

Hi all,

Just an FYI if anyone is interested. I generated some Python
wrappers for the usb/ip shared libraries. This is a new realm for
me, so I don't even know how useful the wrappers are in their
current state. However, I created them several weeks ago and
haven't used them since, so I wanted to let everyone know there
there is at least something available. My end goal was to get some
nice pygtk userland tools developed.

Here's the link:

http://code.google.com/p/pyusbip/

If anyone decides to do any work in this realm, please let me know.
I'd be happy to participate.

Thanks,
Brian 