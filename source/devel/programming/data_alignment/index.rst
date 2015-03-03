

.. index::
   ! Data alignment


.. _data_alignment:

==================================
Data alignment
==================================


.. seealso::

   - http://en.wikipedia.org/wiki/Data_structure_alignment
   - :ref:`memories`


.. contents::
   :depth: 3

Introdution
===========

Data structure alignment is the way data is arranged and accessed in computer
memory.

It consists of two separate but related issues:

- data alignment
- and data structure padding.

When a modern computer reads from or writes to a memory address, it will do this
in word sized chunks (e.g. 4 byte chunks on a 32-bit system).

Data alignment means putting the data at a memory offset equal to some multiple
of the word size, which increases the system's performance due to the way the
CPU handles memory.

To align the data, it may be necessary to insert some meaningless bytes between
the end of the last data structure and the start of the next, which is data
structure padding.

Endianness
==========

.. toctree::
   :maxdepth: 3


   endianness/index


Mask computing
===============

.. toctree::
   :maxdepth: 3


   mask_computing/index


Bitwise IO
===============

.. toctree::
   :maxdepth: 3


   bitwise/index


