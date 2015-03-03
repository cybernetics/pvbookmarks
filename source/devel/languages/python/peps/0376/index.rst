
.. index::
   pair: PEP; 0376

.. _python_pep_0376:

============================================================================
pep 0376 Database of Installed Python Distributions
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0376/
   - :ref:`python_pep_0427`


.. contents::
   :depth: 3



Abstract
========

The goal of this PEP is to provide a standard infrastructure to manage project
distributions installed on a system, so all tools that are installing or
removing projects are interoperable.

To achieve this goal, the PEP proposes a new format to describe installed
distributions on a system.

It also describes a reference implementation for the standard library.

In the past an attempt was made to create an installation database (see PEP 262 [3]).

Combined with PEP 345, the current proposal supersedes PEP 262.


Last-Modified:  2012-11-09 20:58:41 -0500 (Fri, 09 Nov 2012)
============================================================

