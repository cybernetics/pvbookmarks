
.. index::
   pair: PEP; 0427
   ! Wheel

.. _python_pep_0427:
.. _python_pep_427:

============================================================================
pep 0427 The Wheel Binary Package Format
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0427/
   - http://wheel.readthedocs.org
   - :ref:`wheel_format`


.. contents::
   :depth: 3


Abstract
========

This PEP describes a built-package format for Python called ``wheel``.

A wheel is a ZIP-format archive with a specially formatted file name and
the .whl extension.

It contains a single distribution nearly as it would be installed according
to :ref:`PEP 376 <python_pep_0376>` with a particular installation scheme.


**A wheel file may be installed by simply unpacking into site-packages with the
standard 'unzip' tool, while preserving enough information to spread its
contents out onto their final paths at any later time**.




Source implementation
=====================

.. toctree::
   :maxdepth: 3

   wheel
