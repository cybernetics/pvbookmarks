


.. index::
   pair: pcsc-tools ;  versions



.. _pcsc_tools_versions:

=====================
pcsc-tools versions
=====================

.. seealso:: http://ludovic.rousseau.free.fr/softwares/pcsc-tools/index.html



.. toctree::
   :maxdepth: 4

   1.4.18/index


1.4.17 - 18 August 2010, Ludovic ROUSSEAU
=========================================

- 153 new ATRs
- Allow to build with pcsc-lite >= 1.6.2

1.4.16 - 12 January 2010, Ludovic ROUSSEAU
==========================================

- 153 new ATR
- pcsc_scan.c: check for PnP support at run time instead of using a #define
- ATR_analysis: use curl instead of wget on Darwin
- gscriptor: ReaderConfig(): escape metacharacters []() in
  the reader name when using reader name as a pattern matching

1.4.15 - 9 January 2009, Ludovic ROUSSEAU
=========================================

- 68 new ATR
- ATR_analysis:

 * truncate the ATR if extra bytes are present (like on Leopard with
   an ATR padded with 0 up to 33 bytes)
 * add value for Di=7 (7816-3:2006 page 19)
 * check if Fi is RFU when calculating baud rate
 * display the max frequency associated with Fi

- pcsc_scan.c: use "\\?PnP?\Notification" mechanism when possible

1.4.14 - 11 May 2008, Ludovic ROUSSEAU
======================================

- 24 new ATR
- gscriptor, scriptor: use SCARD_SHARE_SHARED instead of SCARD_SHARE_EXCLUSIVE
  to not lock the card
- ATR_analysis: add support for ATR with : as byte separator (ATR reported by
  "opensc-tool --atr" for example)

1.4.13 - 23 March 2008, Ludovic ROUSSEAU
========================================

- 29 new ATR
- pcsc_scan: avoid a bug when the last reader is removed

