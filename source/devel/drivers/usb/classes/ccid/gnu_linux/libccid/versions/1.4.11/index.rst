

.. index::
   pair: Libccid; 1.4.11

.. _libccid_1.4.11:

============================================================
Changes for libccid 1.4.11  12 June 2013, Ludovic Rousseau
============================================================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2013/06/new-version-of-libccid-1411.html
   - https://plus.google.com/u/0/105951035108309096272/posts


Courriel
========

::

    Ludovic Rousseau <ludovic.rousseau@gmail.com>
    à:	 MUSCLE <muscle@lists.musclecard.com>
    date:	 12 juin 2013 14:32
    objet:	 [Muscle] New version of libccid: 1.4.11


I just released a version 1.4.11 of libccid the free software CCID
class smart card reader driver.

Changes
========

- Add support of
   . Gemalto IDBridge CT30
   . Gemalto IDBridge K30
   . SCM Microsystems Inc. SCL010 Contactless Reader
   . SCM Microsystems Inc. SDI011 Contactless Reader
   . THRC reader
- Better management of time extension requests
- parse: better support of devices with bInterfaceClass = 0xFF
- udev rule file: Remove setting group to pcscd, remove support of
  Linux kernel < 2.6.35 for auto power up management
- some minor bugs removed

