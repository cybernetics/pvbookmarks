.. module:: libUSB-winusb 
    :synopsis: libUSB-winusb annexes 
    :platform: windows XP, Vista, windows 7

.. index:: 
   libusb
   http://libusb.org/wiki/windows_backend 
   http://mcuee.blogspot.com   

======
libusb
======


.. seealso::  

   - https://lists.sourceforge.net/lists/listinfo/libusb-win32-devel
   - http://libusb.org/wiki/windows_backend
   - http://code.google.com/p/libusb-winusb-wip/

About
=====

The aim of this project is to bring a Windows backend to the mainline 
libusb 1.0 branch, so that libusb 1.0 can easily be used on Windows 
platforms. 

Status
======

The Windows backend is now in pre-release stages. As of 2010.02.17, 
it include all of the main libusb v1.0 features, for both HID and 
WinUSB devices, apart from isochronous transfers (which is a limitation 
from the WinUSB Microsoft API).
It currently supports all Windows platforms from Windows XP, including 
64 bit versions of Windows (Windows 2003 is untested). 


The benefits of this WinUSB backend is that it will work for 64bit Windows
like Vista and Windows 7. The WinUSB backend will not support isochronous
transfer. So it is not a complement replacement of libusb-win32 yet.

   
libusb-winusb
=============

libusb-winusb will be integrated to the main libusb-1.0
-------------------------------------------------------

libusb-winusb will be integrated to the main libusb-1.0 tree (using git). Once
it is mature, I think it will be very good replacement for libusb-win32. More
backend will probably be added, like the HID backend (HID support) and the
libusb-win32 device driver backend (isochronous support, Windows 2k support).

Please try this branch if you are interested.

Xiaofan http://mcuee.blogspot.com
 

.. index::
   signtool
   



   
   

     
   

   

   