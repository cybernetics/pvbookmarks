
.. index::
   pair: Library ; Bionic
   pair: Libc   ; Bionic
   ! Bionic


.. _bionic:

============
bionic
============

.. seealso::

   - https://en.wikipedia.org/wiki/Bionic_%28software%29


The Bionic libc is a derivation of the BSD standard C library code that was
originally developed by Google for the Android embedded operating system.

Bionic has several major Linux-specific features and development continues
independent of other code bases. The publicly stated goals for Bionic are:

- BSD license: Android uses a Linux kernel which is under the GNU General Public
  License (GPL), but Google wished to isolate Android applications from the effects
  of the GPL.
- Small size: Bionic is much smaller than the GNU C Library (glibc) and somewhat
  smaller than uClibc.
- Speed: Bionic is designed for CPUs at relatively low clock frequencies.







