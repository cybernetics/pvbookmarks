
.. index::
   smartcard sim


===========================
smartcard sim python module
===========================

.. seealso::

   - http://michau.benoit.free.fr/
   - http://michau.benoit.free.fr/codes/smartcard/
   - http://michau.benoit.free.fr/codes/smartcard/iso7816.py
   - https://code.google.com/p/pssi/source/browse/trunk/pssi/plugins/sim/structures.py
   - http://ludovic.rousseau.free.fr/softwares/pcsc-tools/smartcard_list.txt



Smartcards with electrical connectors are in general all compliant with the basis
standard ISO7816 - part 1-2-3-4.

ISO standards are not public, but you can have a good view on it here:

- http://www.cardwerk.com/smartcards/smartcard_standard_ISO7816.aspx

The principle is to communicate with the card over a serial link, sending APDU
commands,  and receiving replies with always SW codes and sometimes data.

All the SIM and USIM cards are based on these standards, and in addition, on
ETSI and 3GPP standards.

ETSI standards are not public.

3GPP standards are  (http://www.3gpp.org/specification-numbering).

SIM cards are easy to read as they are only mono-application: check 3GPP TS 11.11
or TS 51.011.

USIM cards are some more evolved as they are multi-applications / multi-channels
cards:  check ETSI TS 101.221 and 3GPP TS 31.101 and 31.102



.. _cardlib_for_smartcard:

cardlib for smartcard
=====================

.. seealso::

   - http://michau.benoit.free.fr/codes/smartcard/card/
   - http://ludovic.rousseau.free.fr/softwares/pcsc-tools/smartcard_list.txt


::

    |   smartcard_list.txt
    |
    \---card
            __init__.py
            utils.pyc
            SIM.py
            ICC.py
            __init__.pyc
            utils.py
            USIM.py
            ICC.pyc
            smartcard_list.txt
            FS.py


This is a new version, build from the older iso7816.py monolithic script, to
request mainly SIM and USIM cards.

It needs python 2.6 (may work on older version: not tested), a smartcard reader
(USB or RS-232), pcsc-lite driver and daemon and its python binding pyscard.

The library is now splitted in several files:

- utils.py: contains facilities for parsing TV, TLV, BER_TLV records and some
  other little functions used by others modules
- `ICC.py <http://michau.benoit.free.fr/codes/smartcard/card/ICC.py>`_ : contains the 2 main classes:

    - ISO7816: which implements a little part of the ISO standard
    - UICC: which implements part of the ETSI standard inheriting from the
      ISO7816 class

- SIM.py: contains the class SIM inheriting from ISO7816 class, implementing
  part of TS 51.011
- USIM.py: contains the class USIM inheriting from UICC class, implementing
  part of TS 31.102
- `FS.py <http://michau.benoit.free.fr/codes/smartcard/card/FS.py>`_ : dictionnaries refencing SIM and USIM files address as described in
  those 3GPP standards

All file addresses and data syntax are list of short integer (e.g. [0xAA, 0xBB,
0xCC, ...]), as used by pyscard.

Mistakes remains surely still in these scripts, so use it with care.

UICC and USIM classes do not implement logical channels.

ISO7816 and UICC security conditions parsing is really not well implemented.


Example sessions
================

::

    >>> from card.ICC import ISO7816
    >>> a = ISO7816()
    >>> a.ATR_scan()


Output:


::

    smartcard reader:  id3 Semiconductors CL1356A+ 0
    smart card ATR is: 3B 8F 80 01 80 4F 0C A0 00 00 03 06 03 00 00 00 00 00 00 6B
    ATR analysis:
    TD1: 80
    TD2: 1
    supported protocols {'T=0': True, 'T=1': True}
    T=0 supported True
    T=1 supported True
    checksum: 107
            clock rate conversion factor: 372
            bit rate adjustment factor: 1
            maximum programming current: 50
            programming voltage: 5
            guard time: None
    nb of interface bytes: 2
    nb of historical bytes: 15
    None

    historical bytes:  80 4F 0C A0 00 00 03 06 03 00 00 00 00 00 00
    checksum:  0x6B

    using pcsc_scan ATR list file: smartcard_list.txt
    smartcard ATR fingerprint:
    RFID - ISO 14443 Type A Part 3 (as per PCSC std part3)
    specialized Mifare Ultralight card

iso7816.py
==========

The old version replace by the carlib module.


:download:`Download iso7816.py <iso7816.py>`


.. literalinclude:: iso7816.py


.. index::
   cardlib for smartcard
