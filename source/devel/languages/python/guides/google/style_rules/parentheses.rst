
.. index::
   pair: python; parentheses

.. _python_parentheses:

==========================
Use parentheses sparingly
==========================

Do not use them in return statements or conditional statements unless using
parentheses for implied line continuation. (See above.)

It is however fine to use parentheses around tuples.

Yes::

     if foo:
         bar()
     while x:
         x = bar()
     if x and y:
         bar()
     if not x:
         bar()
     return foo
     for (x, y) in dict.items(): ...

No::

     if (x):
         bar()
     if not(x):
         bar()
     return (foo)
