
.. index::
   pair: python; Per user site-packages directory
   pair: python peps; pep 0370
   pair: pep; 0370

.. _python_pep_0370:

====================================================
pep 0370 Per user site-packages directory
====================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0370/




Abstract
========

This PEP proposes a new a per user site-packages directory to allow users the
local installation of Python packages in their home directory.


Rationale
==========

Current Python versions don't have a unified way to install packages into the
home directory of a user (except for Mac Framework builds). Users are either
forced to ask the system administrator to install or update a package for them
or to use one of the many workarounds like Virtual Python [1], Working Env [2]
or Virtual Env [3].

It's not the goal of the PEP to replace the tools or to implement isolated
installations of Python. It only implements the most common use case of an
additional site-packages directory for each user.

The feature can't be implemented using the environment variable PYTHONPATH.

The env var just inserts a new directory to the beginning of sys.path but it
doesn't parse the pth files in the directory.

A full blown site-packages path is required for several applications and
Python eggs.





