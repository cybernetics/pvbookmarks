

.. index::
   ! ord


.. _ord:

==================================
ord
==================================


.. seealso::

   - :ref:`convert_between_binary_and_ascii`


.. contents::
   :depth: 3



Python code
===========

.. seealso::

   - http://docs.python.org/library/functions.html#ord


Given a string of length one, return an integer representing the Unicode code
point of the character when the argument is a unicode object, or the value of
the byte when the argument is an 8-bit string.

For example, ord('a') returns the integer 97, ord(u'\u2020') returns 8224.

This is the inverse of chr() for 8-bit strings and of unichr() for unicode objects.

If a unicode argument is given and Python was built with UCS2 Unicode, then
the character’s code point must be in the range [0..65535] inclusive; otherwise
the string length is two, and a TypeError will be raised.
