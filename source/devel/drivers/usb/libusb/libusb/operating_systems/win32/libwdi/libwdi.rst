.. module:: libwdi 
    :synopsis: libwdi
    :platform: windows XP, Vista, windows 7

.. index:: 
   libwdi
  
======
libwdi
======

.. seealso:: 

   - http://libusb.org/wiki/libwdi
   - http://git.libusb.org/?p=libusb-pbatard.git;a=shortlog;h=refs/heads/wdi
   


The aim of this project is to create a library that facilitates the foolproof 
installation of any USB driver required to use a libusb application on Windows. 

Features
========

- all required driver files are provided by the library - no need for 
  additional downloads
  
- automated inf generation

- compatible with 32 and 64 bit Windows platforms, starting with Windows XP, 
  with the possibility to either produce 2 separate libraries, for 32 or 64 bit, 
  or a single library that covers both 32 and 64 bit at the same time.
  
- can either be integrated in your libusb application, so that a single executable 
  application can be redistributed without the need for an additional installer, 
  or to create a separate installer application (the library itself does have 
  any libusb dependency) 

Status
======

As of 2010.03.29, libwdi is in functional beta. 

