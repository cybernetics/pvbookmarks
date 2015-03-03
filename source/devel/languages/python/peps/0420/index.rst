
.. index::
   pair: Python PEP; 0420
   pair: Python; Implicit Namespace Packages

.. _python_pep_0420:

============================================================================
pep 0420 Implicit Namespace Packages
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0420/



Abstract
========

Namespace packages are a mechanism for splitting a single Python package across
multiple directories on disk. In current Python versions, an algorithm to compute
the packages __path__ must be formulated.

With the enhancement proposed here, the import machinery itself will construct
the list of directories that make up the package.

This PEP builds upon previous work, documented in PEP 382 and PEP 402.

Those PEPs have since been rejected in favor of this one.
An implementation of this PEP is at


.. _`PEP 382`: http://www.python.org/dev/peps/pep-0382
.. _`PEP 402`: http://www.python.org/dev/peps/pep-0402
