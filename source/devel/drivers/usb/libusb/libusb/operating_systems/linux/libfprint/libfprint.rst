.. module:: libfprint
    :synopsis: The libfprint for GNU/linux
    :platform: GNU/Linux
  
  
.. index::
   libfprint linux
   http://www.reactivated.net/fprint/wiki/Libfprint
   http://www.reactivated.net/fprint/api/
   http://www.reactivated.net/fprint/wiki/Driver_quality
   http://www.reactivated.net/fprint/wiki/Libfprint:Supported_devices
   LGPL-2.1
   libfprint LGPL

.. image:: _static/fprint_logo_project.png


.. _libfprint:

=======================
libfprint linux library
=======================

.. seealso:: 

   - http://sourceforge.net/projects/fprint/files/
   - http://www.reactivated.net/fprint/api/
   - http://www.reactivated.net/fprint/wiki/Libfprint
   - http://www.reactivated.net/fprint/wiki/Main_Page
   - http://www.reactivated.net/fprint/wiki/Libfprint:Supported_devices
   - http://www.reactivated.net/fprint/wiki/Driver_quality
   

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


.. index::
   Fingerprint driver quality
   
   
Fingerprint driver quality
==========================

.. seealso:: http://www.reactivated.net/fprint/wiki/Driver_quality


libfprint includes a number of drivers which are all compiled and included 
by default. This will not change, because we want to promote further 
development of all drivers and ensure they continue to compile OK (even 
the ones that are not so high quality).

However, if you're distributing libfprint, you may want to selectively 
disable the drivers which are known not to work so well. This page will 
guide you on those decisions.

In the context of this page, we refer to "quality" from a user perspective 
how well does the driver accept fingers that match, and reject ones that 
don't? It does not necessary relate to the code quality of that driver, 
which may be different!

The quality of most drivers could be improved by the methods described 
at Imaging performance. 
   
   

