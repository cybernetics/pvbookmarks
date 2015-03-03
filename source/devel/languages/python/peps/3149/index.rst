

.. index::
   pair: Python pep; 3149


.. _python_pep_3149:

==========================================================
PEP 3149 ABI version tagged .so files
==========================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-3149/

Abstract
========

PEP 3147 [1] described an extension to Python's import machinery that improved 
the sharing of Python source code, by allowing more than one byte compilation 
file (.pyc) to be co-located with each source file.

This PEP defines an adjunct feature which allows the co-location of extension 
module files (.so) in a similar manner. 

This optional, build-time feature will enable downstream distributions of 
Python to more easily provide more than one Python major version at a time.

