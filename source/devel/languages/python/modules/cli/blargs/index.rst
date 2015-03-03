

.. index::
   pair: cli ; blargs

.. _python_blargs:

=======================
Python blargs module
=======================

.. seealso::

   - http://readthedocs.org/docs/blargs/en/latest/
   - https://bitbucket.org/gyllstromk/blargs
   - http://pypi.python.org/pypi/blargs


blargs provides easy command line parsing, as an alternative to argparse and
optparse from Python's standard library. The main distinctions are:

  * Cleaner, more minimal, and possibly more `pythonic` syntax.
  * Support for arbitrarily complex dependency relationships. For example,
    argument A might require arguments B and C, while conflicting with D; or
    requiring argument E in the case that A is less than 10 or B is equal
    to the string 'wonderful!'.

  * Emphasis on `ease of use` over `configurability`.

Blargs has been tested on Python2.6 to Python3.2 and PyPy.







