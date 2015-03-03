
.. index::
   pair: PEP; 0441

.. _python_pep_0441:

============================================================================
pep 0441 Improving Python ZIP Application Support
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0441/


.. contents::
   :depth: 3




Improving Python ZIP Application Support
=========================================

Python has had the ability to execute directories or ZIP-format archives as 
scripts since version 2.6.

When invoked with a zip file or directory as its first argument the interpreter 
adds that directory to sys.path and executes the __main__ module. 

These archives provide a great way to publish software that needs to be 
distributed as a single file script but is complex enough to need to be 
written as a collection of modules.

This feature is not as popular as it should be mainly because no one’s heard 
of it as it wasn’t promoted as part of Python 2.6, but also because Windows 
users don’t have a file extension (other than .py) to associate with the launcher.

This PEP proposes to fix these problems by re-publicising the feature, 
defining the .pyz and .pyzw extensions as “Python ZIP Applications” and 
“Windowed Python ZIP Applications”, and providing some simple tooling to 
manage the format.
