


.. index::
   python hash (pycrc)

===========================
Python crc module
===========================

.. seealso::

   - http://www.tty1.net/pycrc/index_en.html
   - http://www.tty1.net/pycrc/faq_en.html


pycrc is a free, easy to use Cyclic Redundancy Check (CRC) calculator and source
code generator.


Description
===========

pycrc provides CRC reference implementations in Python and a source code
generator for C. The used CRC variant can be chosen from a fast but space-consuming
implementation to slower but smaller versions especially suitable for embedded
applications. The models can be freely chosen, but a comprehensive collection
of CRC models is available by name. The following functions are implemented:

- calculate the checksum of a string or a file.
- generate the source files for a "C" implementation.

The following variants of the CRC algorithm are supported:

- bit-by-bit: the basic algorithm which operates individually on every bit of
  the augmented message (i.e. the input data with width 0-bits attached to the
  end). This algorithm is the easiest one to understand, because it's a direct
  implementation of the basic polynomial division, but it is also the slowest
  among all possible variants.
- bit-by-bit-fast: a variation of the simple bit-by-bit algorithm, which doesn't
  need the augmented message. This algorithm might be a good choice for embedded
  platforms, where code space is a major concern.
- table-driven: the standard table driven algorithm. This is the fastest variant,
  because it operates on bytes as opposed to bits, and uses a look-up table of
  256 elements, which might not be feasible for small embedded systems, though.
  Anyway, the number of elements in the look-up table can be reduced by means of
  the --table_idx_with command line switch. By using 4 bits (16 elements in the
  look-up table) the code is still very fast (roughly half the speed of a 8-bit
  table-driven code) but much more compact.

pycrc is released under the terms of the MIT licence.



