
.. index::
   pair: PEP; 0439
   pair: Enums; PEP 439

.. _python_pep_0439:

============================================================================
pep 0439 Inclusion of pip bootstrap in Python installation (rejected)
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0439/
   - :ref:`bootstrap`

.. contents::
   :depth: 3


Abstract
========

Inclusion of pip bootstrap in Python installation
    
This PEP proposes the inclusion of a pip boostrap executable in the Python 
installation to simplify the use of 3rd-party modules by Python users.

This PEP does not propose to include the pip implementation in the Python 
standard library. 

Nor does it propose to implement any package management or installation mechanisms 
beyond those provided by :ref:`PEP 427 ("The Wheel Binary Package Format 1.0") <python_pep_427>`
and TODO distlib PEP.
        
    
   
