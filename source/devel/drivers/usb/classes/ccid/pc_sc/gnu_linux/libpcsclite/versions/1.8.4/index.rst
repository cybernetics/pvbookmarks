
.. index::
   pair: libpcsclite ; version 1.8.4


.. _libpcsclite_1_8_4:

========================================
libpcsclite 1.8.4  (26/06/2012 19:03)
========================================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2012/06/new-version-of-pcsc-lite-184.html
   - https://alioth.debian.org/frs/shownotes.php?release_id=1811


.. contents::
   :depth: 3

Changelog  (26/06/2012 19:03)
=============================


- Add [ and ] in the list of accepted characters for a reader name
- truncates the reader name if it is too long instead of rejecting the
  reader
- The restriction to have to call SCardEstablishContext() in each thread
  has been removed. Threads could now share a PC/SC context.
- Fix compiler failure for static driver
- Update IFDHandler API Doxygen regarding the "libusb-1.0" naming scheme
- Some other minor improvements and bug corrections





