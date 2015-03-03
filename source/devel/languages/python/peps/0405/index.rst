

.. index::
   pair: Python; Virtual Environments
   pair: Pep; 0405


.. _python_pep_0405:

=====================================================
pep 0405 Python Virtual Environments
=====================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0405/
   - :ref:`virtualenv`


.. contents::
   :depth: 3

Abstract
========


This PEP proposes to add to Python a mechanism for lightweight "virtual environments"
with their own site directories, optionally isolated from system site directories.

Each virtual environment has its own Python binary (allowing creation of
environments with various Python versions) and can have its own independent set
of installed Python packages in its site directories, but shares the standard
library with the base installed Python.








