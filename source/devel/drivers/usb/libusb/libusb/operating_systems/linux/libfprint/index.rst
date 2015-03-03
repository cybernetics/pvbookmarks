.. module:: libfprint
    :synopsis: The libfprint for GNU/linux
    :platform: GNU/Linux
  
  
.. index::
   fprint system
   http://www.reactivated.net/fprint/wiki/Main_Page
   
   
  
.. _libfprint_main:

=======================
libfprint linux library
=======================

.. image:: _static/fprint_logo_project.png



.. seealso:: 

   - http://www.reactivated.net/fprint/wiki/Main_Page
   - http://www.reactivated.net/fprint/api/

libfprint
=========

libfprint is the centre of our efforts. libfprint is the component which does 
the dirty work of talking to fingerprint reading devices, and processing 
fingerprint data.

If you're a user, you probably aren't interested in libfprint, instead you 
want  to find some software which uses libfprint (see the integration 
project).

If you're an application developer looking to add support for some kind 
of fingerprinting to your software, libfprint is exactly what you are 
looking for. It provides a simple API for you to enroll fingerprints and 
then identify users later on.


Download
========

- http://www.reactivated.net/fprint/wiki/Download
- http://cgit.freedesktop.org/libfprint/libfprint/

Clone
-----

- git://anongit.freedesktop.org/libfprint/libfprint
- ssh://git.freedesktop.org/git/libfprint/libfprint

Integration
===========

The integration project details our efforts to integrate libfprint with existing 
applications, so that users can use their fingerprint reading hardware.


fprint_demo
===========

fprint_demo is a simple GUI application used to demonstrate and test 
libfprint's capabilities.

fprint_demo homepage 
====================

fprintd is a daemon that provides fingerprint scanning functionality 
over D-Bus.


.. toctree::
   :maxdepth: 2

   libfprint
   libfprintd
   libfprint_demo
   libfprint_faq
   libfprint_src
   libfprint_news
   
   
   
   

