

.. index::
   pair: python ; str


.. _python_str:

====================
python str
====================

.. seealso::

    - http://docs.python.org/py3k/library/stdtypes.html#sequence-types-str-bytes-bytearray-list-tuple-range
    - http://docs.python.org/py3k/library/functions.html#str
    - :ref:`python_parse_module`



.. contents::
   depth: 3


What is a native string
=======================

.. seealso::

   - http://www.python.org/dev/peps/pep-3333/#a-note-on-string-types


If you don't know what a native string is, then you need to study more
to understand why Armin's PEP exists and why it is useful. I suggest
starting with PEP 3333 (the WSGI update to v1.0.1 that first clearly
defined the concept of a native string:
http://www.python.org/dev/peps/pep-3333/#a-note-on-string-types).

There are concrete, practical reasons why the lack of Unicode literals
in Python 3 makes porting harder than it needs to be. Are they
insurmountable? No, of course not - there are plenty of successful
ports already that demonstate porting it quite feasible with existing
tools. But the existing approaches require that, in order to be
forward compatible with Python 3, a program must be made *worse* in
Python 2 (i.e. harder to read and harder to write correctly for
someone that hasn't learned Python 3 yet). Restoring unicode literal
support in 3.3 is a pragmatic step that allows a lot of code to *just
work* on Python 3. Most 2.6+ code that still doesn't work on Python 3
even after this change will be made *better* (or at least not made
substantially worse) by the additional changes necessary for forward
compatibility.

Unicode literals are somewhat unique in their impact on porting
efforts, as they show up *everywhere* in Unicode correct code in
Python 2. The diffs that will be needed to correctly tag bytestrings
in such code under Python 2 are tiny compared to those that would be
needed to strip the u"" prefixes.

Regards,
Nick.


String literals
===============

.. seealso:: http://docs.python.org/py3k/reference/lexical_analysis.html#strings

String methods
==============

.. seealso:: http://docs.python.org/py3k/library/stdtypes.html#string-methods


String services
===============

.. seealso:: http://docs.python.org/py3k/library/strings.html


.. index::
   python (image processing buffer protocol)

Buffer protocol
===============

.. seealso:: http://docs.python.org/py3k/c-api/buffer.html#bufferobjects

Certain objects available in Python wrap access to an underlying memory array
or buffer. Such objects include the built-in bytes and bytearray, and
some extension types like array.array.

Third-party libraries may define their own types for special purposes, such as
image processing or numeric analysis.






