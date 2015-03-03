
.. index::
   pair: PEP; 0345

.. _python_pep_0345:

============================================================================
pep 0345 Metadata for Python Software Packages 1.2
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0345/
   - :ref:`python_pep_0426`


.. contents::
   :depth: 3

Last-Modified:	2013-06-20 19:24:19 +1000 (Thu, 20 Jun 2013)
=============================================================

Abstract
========

This PEP describes a mechanism for adding metadata to Python distributions. 

It includes specifics of the field names, and their semantics and usage.

This document specifies version 1.2 of the metadata format. 

Version 1.0 is specified in PEP 241. 
Version 1.1 is specified in PEP 314.
Version 1.2 of the metadata format adds a number of optional fields 
designed to make third-party packaging of Python Software easier. 

These fields are "Requires-Python", "Requires-External", "Requires-Dist", 
"Provides-Dist", and "Obsoletes-Dist". 

This version also changes the "Platform" field. Three new fields were 
also added: "Maintainer", "Maintainer-email" and "Project-URL".
