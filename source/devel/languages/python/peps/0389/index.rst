

.. _python_pep_0389:

====================================================
pep 0389 argparse - New Command Line Parsing Module
====================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0389/
   - :ref:`python_argparse`
   - :ref:`python_plac_parser`


Acceptance
==========

This PEP was approved by Guido on python-dev on February 21, 2010.

Abstract
========

This PEP proposes inclusion of the ``argparse`` module in the Python standard
library in Python 2.7 and 3.2.


Motivation
==========

The argparse module is a command line parsing library which provides more
functionality than the existing command line parsing modules in the standard
library, getopt and optparse. It includes support for positional arguments
(not just options), subcommands, required options, options syntaxes like "/f"
and "+rgb", zero-or-more and one-or-more style arguments, and many other features
the other two lack.

The argparse module is also already a popular third-party replacement for these
modules. It is used in projects like IPython (the Scipy Python shell) , is
included in Debian testing and unstable, and since 2007 has had various
requests for its inclusion in the standard library .

This popularity suggests it may be a valuable addition to the Python libraries.








