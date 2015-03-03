
.. index::
   pair: PEP; 0426
   pair: Metadata ; Python Software

.. _python_pep_0426:

============================================================================
pep 0426 Metadata for Python Software Packages 2.0
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0426/
   - :ref:`python_pep_0440`





.. contents::
   :depth: 3

Last-Modified:  2013-06-20 22:42:23 +1000 (Thu, 20 Jun 2013)
=============================================================

Abstract
========

This PEP describes a mechanism for publishing and exchanging metadata 
related to Python distributions. 

It includes specifics of the field names, and their semantics and usage.

This document specifies version 2.0 of the metadata format. 
Version 1.0 is specified in PEP 241. 
Version 1.1 is specified in PEP 314. 
Version 1.2 is specified in PEP 345.
Version 2.0 of the metadata format migrates from a custom key-value 
format to a JSON-compatible in-memory representation.

This version also adds fields designed to make third-party packaging of 
Python software easier, defines a formal extension mechanism, and adds 
support for optional dependencies. 

Finally, this version addresses several issues with the previous iteration 
of the standard version identification scheme.


Vinay Sajip depmodel.py
========================


Simple RDBMS modelling of dependencies based on PEP 426. 

Needs SQLAlchemy 0.8. Now updated to reflect the latest schema from PEP 426.

.. seealso:: 

   - https://gist.github.com/vsajip/5929707
   
   
::


    > And it means that having multiple combinations of the same
    > extra/envs is disallowed so I'm going to have to collapse everything
    > back down since it's not stored that way at all?
    >

    I posted a working example [1] showing how there's no need to have the same
    structure at the RDBMS layer and the JSON layer. I asked for more
    information about modelling difficulties you said you had encountered, but
    didn't hear anything more about it. AFAICT the code you were talking about
    isn't public - at least, I couldn't see it in the branches on your GitHub repo.

    As my example shows, it's possible to have a sensible RDBMS structure which
    interoperates with multiple entries in "requires". If I've misunderstood
    something, please let me know what it is.

    Regards,

    Vinay Sajip
    
    [1] https://gist.github.com/vsajip/5929707
    
    
    
