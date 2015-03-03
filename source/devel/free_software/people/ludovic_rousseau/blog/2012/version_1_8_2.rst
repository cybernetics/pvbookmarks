
.. index::
   pair: Ludovic Rousseau; 2012
   pair: PC/SC ; Spy tool


.. _blog_ludovic_rousseau_1.8.2:

=================================================
New version of pcsc-lite: 1.8.2 (18 January 2012)
=================================================

.. seealso::

   - http://ludovicrousseau.blogspot.com/2012/01/new-version-of-pcsc-lite-182.html
   - https://alioth.debian.org/frs/?group_id=30105&release_id=1765#pcsclite-_1.8.2-title-content
   - http://anonscm.debian.org/viewvc/pcsclite/trunk/PCSC/
   - :ref:`libpcsclite`


.. contents::
   :depth: 3


Introduction
============

I just released a new version of pcsc-lite 1.8.2.

No big changes expect for ``pcsc-spy`` I talked about in a previous article
`PCSC API spy, third try`_


.. _`PCSC API spy, third try`:  http://ludovicrousseau.blogspot.com/2011/11/pcsc-api-spy-third-try.html

Changelog 18 January 2012
==========================

- rename pcsc-spy.py to pcsc-spy and install it as a normal binary
  (in :file:`/usr/local/bin by default`)
- write a pcsc-spy.1 manpage
- fix a bug with a multi-slot reader
- Info.plist parser: avoid a buffer read overflow in management
- Some Doxygen improvements






