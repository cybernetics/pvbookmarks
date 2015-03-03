

.. index::
   pair: Bitwise ; Python


.. _python_bitwise_io:

==================================
Python Bitwise IO
==================================


.. seealso::

   - http://rosettacode.org/wiki/Bitwise_IO#Python
   - :ref:`python_language`


.. contents::
   :depth: 3


Code Python
===========

The module file :download:`bitio.py`.


.. literalinclude:: bitio.py
   :linenos:


Exemple d'appel Python
======================

Usage example to "crunch" an 8-bit byte ASCII stream discarding the most
significative "unused" bit...

.. code-block:: python

    #! /usr/bin/env python
    import sys
    import bitio

    o = bitio.BitWriter(sys.stdout)
    c = sys.stdin.read(1)
    while len(c) > 0:
        o.writebits(ord(c), 7)
        c = sys.stdin.read(1)

    ... and to "decrunch" the same stream:

    #! /usr/bin/env python
    import sys
    import bitio

    r = bitio.BitReader(sys.stdin)
    while True:
        x = r.readbits(7)
        if ( r.read == 0 ):
            break
        sys.stdout.write(chr(x))
