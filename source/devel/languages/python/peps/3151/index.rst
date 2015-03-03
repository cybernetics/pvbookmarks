

.. index::
   pair: python; exception
   pair: python peps; pep 3151


.. _python_pep_3151:

=====================================================
pep 3151 Reworking the OS and IO exception hierarchy
=====================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-3151/


Abstract
========

The standard exception hierarchy is an important part of the Python language.

It has two defining qualities: it is both generic and selective.

Generic in that  the same exception type can be raised - and handled - regardless
of the context  (for example, whether you are trying to add something to an
integer, to call a  string method, or to write an object on a socket, a TypeError
will be raised for  bad argument types).

Selective in that it allows the user to easily handle (silence, examine, process,
store or encapsulate...) specific kinds of error conditions while letting other
errors bubble up to higher calling contexts. For example, you can choose to
catch ZeroDivisionErrors without affecting the default handling of other
ArithmeticErrors (such as OverflowErrors).

This PEP proposes changes to a part of the exception hierarchy in order to better
embody the qualities mentioned above: the errors related to operating system calls
(OSError, IOError, mmap.error, select.error, and all their subclasses).








