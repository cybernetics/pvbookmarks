
.. index::
   pair: libpcsclite ; version 1.8.2


.. _libpcsclite_1_8_2:

=================================
libpcsclite 1.8.2 (janvier 2012)
=================================

.. seealso::

   - http://ludovicrousseau.blogspot.com/2012/01/new-version-of-pcsc-lite-182.html


I just released a new version of pcsc-lite 1.8.2. No big changes expect for
``pcsc-spy`` I talked about in a previous article `PCSC API spy, third try`_.


.. _`PCSC API spy, third try`:  http://ludovicrousseau.blogspot.com/2011/11/pcsc-api-spy-third-try.html

Changelog 18 January 2012
==========================

- rename pcsc-spy.py to pcsc-spy and install it as a normal binary
  (in :file:`/usr/local/bin by default`)
- write a pcsc-spy.1 manpage
- fix a bug with a multi-slot reader
- Info.plist parser: avoid a buffer read overflow in management
- Some Doxygen improvements









