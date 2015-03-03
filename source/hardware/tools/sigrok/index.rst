

.. index::
   ! Sigrok

.. _sigrok:

======================
Sigrok
======================


.. seealso::

   - http://sigrok.org/wiki/Main_Page
   
 
.. contents::
   :depth: 3 

Introduction
============= 
 
The sigrok project aims at creating a portable, cross-platform, 
Free/Libre/Open-Source signal analysis software suite that supports 
various device types, such as logic analyzers, MSOs, oscilloscopes, 
multimeters, LCR meters, sound level meters, thermometers, hygrometers, 
anemometers, light meters, dataloggers, function generators, 
spectrum analyzers, power supplies, GPIB interfaces, and more.

It is licensed under the terms of the GNU GPL. Design goals and features include:

- Broad hardware support. Supports many different logic analyzers, 
  oscilloscopes, multimeters, data loggers etc. from various vendors.
- Cross-platform. Works on Linux, Mac OS X, Windows, FreeBSD, OpenBSD, 
  NetBSD (and on x86, ARM, Sparc, PowerPC, ...).
- Scriptable protocol decoding. Extendable with stackable protocol 
  decoders written in Python 3.
- File format support. Supports various input/output file formats 
  (binary, ASCII, hex, CSV, gnuplot, VCD, ...).
- Reusable code. Consists of the libsigrok and libsigrokdecode shared 
  libraries which can be used by various frontends/GUIs.
  

On debian
=========

.. seealso::

   - http://packages.qa.debian.org/s/sigrok.html


sigrok GUI
==========

.. seealso::

   - :ref:`sigrok_application`

.. seealso:: http://sigrok.org/wiki/GUI

  
Sigrok projects
================

.. toctree::
   :maxdepth: 3
   
   projects/index
   
      



   
   
   
