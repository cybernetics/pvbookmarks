
.. index::
   pair: libpcsclite ; version 1.8.6


.. _libpcsclite_1_8_6:

========================================
libpcsclite 1.8.6 (30 August 2012)
========================================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2012/08/new-version-of-pcsc-lite-185.html
   - https://alioth.debian.org/frs/shownotes.php?release_id=1823


.. contents::
   :depth: 3

Changelog 
============

- Fix a problem when only serial drivers are used (no hotplug/USB driver)
- increase log buffer size from 160 to 2048. Some "long" log lines where truncated.
- Fix redirection of stdin, stdout and stderr to /dev/null when pcscd is 
  started as a daemon (default)
- Some other minor improvements and bug corrections



