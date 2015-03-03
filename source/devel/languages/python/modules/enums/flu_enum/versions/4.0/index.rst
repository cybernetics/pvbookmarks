

==============================
flufl.enum  4.0 (2013-04-05)
==============================


.. seealso::

   - http://pythonhosted.org/flufl.enum/NEWS.html#id1
   - :ref:`python_pep_0435`



.. contents::
   :depth: 3

Announce
========


I am happy to announce flufl.enum version 4.0.

What is flufl.enum ?
---------------------

It is an enumeration package with a simple syntax, and concise and specific
semantics.

flufl.enum is compatible with Python 2.7, 3.2, and 3.3.

It is proposed for inclusion in Python 3.4 by way of :ref:`PEP 435 <python_pep_0435>`.

My thanks to Eli Bendersky for his help with both the code and in authoring
the PEP, as well as everyone who participated in discussions on python-dev,
python-ideas, and at the PyCon 2013 language summit.

Changes since 3.2
=================

 - Added the IntEnum variant.  When you create an enumeration with this base
   class, the resulting enum values *are* ints and can be used anywhere a
   Python int can be used, including in the C API.  (LP: #1132976)

 - make() is deprecated.  You can now just call Enum() or IntEnum() to
   programmatically create enumerations.  (LP: #1162375).  These constructors
   now also accept a space-separated string of attribute names which are
   auto-split and auto-numbered.  They also accept a dictionary mapping names
   to values.

 - IntEnums values support __index__() for slicing (LP: #1132972), as well
   as__int__() for coercion to a concrete integer.

 - EnumValue.__int__() is deprecated; use IntEnumValue (via IntEnum) instead.

 - EnumValues now have a .value attribute to access the actual, underlying
   value. (LP: #1132859)

 - Previously deprecated attributes .enumclass and .enumname have been
   removed, as well as the module function make_enum().  (LP: #1132951)

 - Minor API changes: the repr of enum values say "value=" instead of "int=",
   and multiple enum values in a single enum definition now raises ValueError
   instead of TypeError.

 - Single argument Enum() calling as a synonym for getitem is deprecated.

 - Other bugs fixed: LP: #1026403, LP: #1132830, LP: #1124596

Full documentation is available here:

- http://pythonhosted.org/flufl.enum/README.html

The project home is at:

- https://launchpad.net/flufl.enum

You can report bugs at:

- https://bugs.launchpad.net/flufl.enum

Download the package from the Cheeseshop:

- https://pypi.python.org/pypi/flufl.enum

or from the Launchpad project page above.

Read PEP 435:

- http://www.python.org/dev/peps/pep-0435/

::

    Enjoy,
    -Barry
