

.. index::
   pair: python; qualified name

.. _python_pep_3155:

==================================================
pep 3155 Qualified name for classes and functions
==================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-3155/


Python's introspection facilities have long had poor support for nested classes.

Given a class object, it is impossible to know whether it was defined inside
another class or at module top-level; and, if the former, it is also impossible
to know in which class it was defined. While use of nested classes is often
considered poor style, the only reason for them to have second class
introspection support is a lousy pun.







