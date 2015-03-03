
.. index::
   pair: libpcsclite ; version 1.8.3


.. _libpcsclite_1_8_3:

========================================
libpcsclite 1.8.3 (30/03/2012 12:14))
========================================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2012/03/new-version-of-pcsc-lite-183.html
   - https://alioth.debian.org/frs/shownotes.php?release_id=1773


.. contents::
   :depth: 3

Changelog 
=============================


- ignore directories and hidden (.*) files when parsing a configuration directory 
  (like /etc/reader.conf.d/)
- add Mac OS X for PC/SC spy tool
- fix a bug in PC/SC spy tool when loading of the real library fails
- add:
      - PCSCv2_PART10_PROPERTY_dwMaxAPDUDataSize, 
      - PCSCv2_PART10_PROPERTY_wIdVendor 
      - and PCSCv2_PART10_PROPERTY_wIdProduct from PC/SC v2 part 10 release 2.02.09 (not yet published)
      
- Some other minor improvements and bug corrections





