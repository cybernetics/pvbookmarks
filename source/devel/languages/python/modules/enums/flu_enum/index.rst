
.. index::
   pair: Python enums; flufl.enum


.. _python_fluflenums:

=======================
flufl.enum
=======================

.. seealso::

   - http://pythonhosted.org/flufl.enum/README.html


.. contents::
   :depth: 3


What is flufl.enum ?
=====================

It is an enumeration package with a simple syntax, and concise and specific
semantics.

flufl.enum is compatible with Python 2.7, 3.2, and 3.3.

It is proposed for inclusion in Python 3.4 by way of PEP 435.


An enumeration is a set of symbolic names bound to unique, constant integer
values.  Within an enumeration, the values can be compared by identity, and
the enumeration itself can be iterated over.  Enumeration items can be
converted to and from their integer equivalents, supporting use cases such as
storing enumeration values in a database.


Motivation
==========

The properties of an enumeration are useful for defining an immutable, related
set of constant values that have a defined sequence but no inherent semantic
meaning.  Classic examples are days of the week (Sunday through Saturday) and
school assessment grades ('A' through 'D', and 'F').  Other examples include
error status values and states within a defined process.

It is possible to simply define a sequence of values of some other basic type,
such as ``int`` or ``str``, to represent discrete arbitrary values.  However,
an enumeration ensures that such values are distinct from any others, and that
operations without meaning ("Wednesday times two") are not defined for these
values.


flufl.enum versions
====================

.. toctree::
   :maxdepth: 3

   versions/index


