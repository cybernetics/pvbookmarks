.. module:: libfprint
    :synopsis: The libfprint for GNU/linux
    :platform: GNU/Linux
  
  
.. index::
   libfprint linux
   http://www.reactivated.net/fprint/wiki/Libfprint
   LGPL-2.1
   libfprint LGPL


   
=======================
libfprint linux library
=======================

.. seealso:: http://www.reactivated.net/fprint/wiki/Libfprint

libfprint is an open source software library designed to make it easy for 
application developers to add support for consumer fingerprint readers to 
their software.


Features
=========

- Written in C
- Licensed as LGPL-2.1
- Depends on libusb for USB communication and glib
- Primarily developed for linux, but should be fairly portable
- Offers a single API to application developers to access the entire 
  range of supported devices
- Supports imaging - downloading live fingerprint scans from the device
- Includes image processing/matching code
- Supports enrollment/verification - enrolling a print from a known user, 
  and then later comparing a live scan to the enrolled print 




