
=======
libccid
=======


.. contents::
   :depth: 3



Introduction
============


This package provides the source code for a generic USB CCID
(Chip/Smart Card Interface Devices) driver and  ICCD
(Integrated Circuit(s) Card Devices).

See the USB CCID and ICCD specifications from the USB working group.


.. seealso::

   - https://alioth.debian.org/frs/?group_id=30105&release_id=1377
   - http://pcsclite.alioth.debian.org/ccid.html
   - http://pcsclite.alioth.debian.org/


CCID driver
===========

- http://ludovicrousseau.blogspot.com/
- http://pcsclite.alioth.debian.org/

- `Project page <http://pcsclite.alioth.debian.org/ccid.html>`_:

      * `Sending usefull logs <http://pcsclite.alioth.debian.org/ccid.html#support>`_
      * `Checking for reader compliance <http://pcsclite.alioth.debian.org/ccid.html#CCID_compliant>`_
      * `Reader matrix <http://pcsclite.alioth.debian.org/section.html>`_

- `Download libccid <https://alioth.debian.org/project/showfiles.php?group_id=30105>`_
- Subversion repository:

      * `viewsvn <http://svn.debian.org/viewsvn/pcsclite/trunk/Drivers/ccid/>`_
      * `wsvn <http://svn.debian.org/wsvn/pcsclite/trunk/Drivers/ccid/>`_
      * svn co svn://svn.debian.org/pcsclite/trunk/Drivers/ccid


Main CCID/ICCD features supported
=================================

- Exchange levels:

    * short APDU
    * extended APDU (with some limitations)
    * TPDU
    * character

- multi-slot readers
- composite CCID device
- PC/SC v2 part 10 features:

    * GET_FEATURE_REQUEST
    * secure PIN verify (FEATURE_VERIFY_PIN_DIRECT)
    * modify PIN entry (FEATURE_MODIFY_PIN_DIRECT)
    * reader PIN properties (FEATURE_IFD_PIN_PROPERTIES)
    * Multifunctional Card Terminal reader direct (FEATURE_MCT_READER_DIRECT)
    * retrieve reader properties in TLV form (FEATURE_GET_TLV_PROPERTIES)

- Data rates list
- Localize LCD display messages (Gemalto GemPC PIN PAD, Covadis Véga-Alpha)
- Extended APDU (for T=1 cards only and if your reader is in TPDU mode
  or extended APDU mode)
- SCardGetAttrib() attributes
- ICCD versions A and B





