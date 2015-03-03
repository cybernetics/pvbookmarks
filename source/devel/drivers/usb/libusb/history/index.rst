
.. index::
   pair: libusb ; History


.. _libusb_history:

==============================================
libusb history fork (June 2012 -> June 2013)
==============================================

.. contents::
   :depth: 2


Historique
===========

libusb forks (Thursday, June 14, 2012)
---------------------------------------


.. seealso::

   - http://ludovicrousseau.blogspot.fr/2012/06/libusb-109-released-and-libusbx.html
   - http://libusbx.sourceforge.net/

The other good news is that this libusb-1.0.9 release is linked to the released
of a fork of libusb called libusbx.

libusbx is the source code of libusb but with active maintainers. libusbx has
already made 4 releases in 3 months (1.0.9, 1.0.10, 1.0.11 and 1.0.12).

Many Linux distributions have already switched to libusbx or are planning to 
do so.



libusb merge (Tuesday, June 10, 2013) libusbx -> libusb
--------------------------------------------------------

::

    Nathan Hjelm <hjelmn@me.com> via lists.sourceforge.net 
    à:	 libusb-devel@lists.sourceforge.net,
    libusbx-devel@lists.sourceforge.net
    date:	 10 juin 2013 18:42
    objet:	 [Libusbx-devel] libusb and libusbx merging


Peter's time has gotten to be very limited so I have opted to take over 
maintenance of libusb. 

I have been in contact with the libusbx team to and invited them to rejoin 
libusb as maintainers and they have accepted. 

The plan is for us to work together in a 1.0.16 release of libusbx. 

This release will be the combination of the libusbx codebase and my efforts 
on libusb 1.0.16 and will be the final release of libusbx. 

After 1.0.16 is out we plan to rename the libusbx github group to libusb 
and wind down the libusbx sourceforge project. 

From that point on the official libusb repository will be at github
(this includes libusb-compat-0.1).

More details will be available (some things may change) as we get closer 
to finally merging the two projects.



Ancien fork libusbx (june 2012 -> june 2014)
============================================

.. toctree::
   :maxdepth: 3
   
   libusbx/index
   news/index   
   
   
