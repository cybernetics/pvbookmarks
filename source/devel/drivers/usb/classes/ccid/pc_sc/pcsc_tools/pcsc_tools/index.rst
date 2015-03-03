

.. index::
   pair: PC/SC; Pcsc-tools


.. _pcsc_tools:

==========
pcsc-tools
==========

.. seealso::

   - http://ludovic.rousseau.free.fr/softwares/pcsc-tools/index.html
   - http://ludovic.rousseau.free.fr/softwares/pcsc-tools/README
   - http://ludovic.rousseau.free.fr/softwares/pcsc-tools/smartcard_list.txt
   - :ref:`pcsc_tools_ref` 


Some tools to be used with smart cards and PC/SC
================================================

This archive contains some tools usefull for a PC/SC user.
PC/SC lite from MUSCLE.

The tools provided are:

pcsc_scan (Ludovic Rousseau <ludovic.rousseau@free.fr>)
=======================================================


regularly scans every PC/SC reader connected to the host
if a card is inserted or removed a "line" is printed

For example::

     PC/SC device scanner
     V 1.4.5 (c) 2001-2006, Ludovic Rousseau <ludovic.rousseau@free.fr>
     PC/SC lite version: 1.3.1
     0: GemPC410 0 0
     1: GemPC430 0 0

     Wed Aug 21 10:08:02 2002
      Reader 0 (GemPC410 0 0)
             Card state: Card removed,

     Wed Aug 21 10:08:09 2002
      Reader 0 (GemPC410 0 0)
             Card state: Card inserted,
             ATR: 3B 6D 00 FF 00 31 80 71 8E 64 48 D5 02 00 82 90 00

     ATR: 3B 6D 00 FF 00 31 80 71 8E 64 48 D5 02 00 82 90 00
     + TS = 3B --> Direct Convention
     + T0 = 6D, Y(1): 0110, K: 13 (historical bytes)
       TB(1) = 00 --> Programming Param P: 0, I: 0
       TC(1) = FF --> Extra guard time: 255
     + Historical bytes: 00 31 80 71 8E 64 48 D5 02 00 82 90 00
       Category indicator byte: 00 (compact TLV data object)
         Tag: 3, len: 1 (card service data byte)
           Card service data byte: 80
             - Application selection: by full DF name
             - EF.DIR and EF.ATR access services: by GET RECORD(s) command
             - Card with MF
         Tag: 7, len: 1 (card capabilities)
           Selection methods: 8E
             - DF selection by full DF name
             - Implicit DF selection
             - Short EF identifier supported
             - Record number supported
         Tag: 6, len: 4 (pre-issuing data)
           Data: 48 D5 02 00
         Mandatory status indicator (3 last bytes)
           LCS (life card cycle): 82 (Proprietary)
           SW: 9000 (Normal processing.)

     Possibly identified card:
     3B 6D 00 FF 00 31 80 71 8E 64 48 D5 02 00 82 90 00
             Blue for Business, American Express@Business

     Wed Aug 21 10:09:57 2002
      Reader 0 (GemPC410 0 0)
             Card state: Card removed,



pcsc-tools versions
===================

.. toctree::
   :maxdepth: 4

   versions/index

