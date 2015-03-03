
.. index::
   pair: libpcsclite ; version 1.8.10


.. _libpcsclite_1_8_10:

========================================
libpcsclite 1.8.10 (19/10/2013 16:41)
========================================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2013/10/new-version-of-pcsc-lite-1810.html
   - https://alioth.debian.org/frs/?group_id=30105&release_id=1907#pcsclite-_1.8.10-title-content


.. contents::
   :depth: 3

Changelog (19/10/2013 16:41)
=============================

This version is a bug fix for the version 1.8.9 I released 3 days ago.

When making the Debian package for pcsc-lite the lintian tool reported that a 
new symbol log_msg was exported by the client library libpcsclite.so.1. 

This symbol is NOT part of the WinSCard API and should not be exported. 

It was a bug and needed to be fixed soon to avoid problems in PC/SC applications 
(like symbol conflict).








