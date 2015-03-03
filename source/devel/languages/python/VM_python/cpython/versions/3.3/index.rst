

.. index::
   pair: python ; 3.3


.. _cpython_3_3:

================
cpython 3.3
================

.. seealso::

   - http://www.python.org/download/releases/3.3.0/
   - http://docs.python.org/3.3/whatsnew/3.3.html


.. contents::
   :depth: 3

What's new
==========


Python 3.3 includes a range of improvements of the 3.x series, as well
as easier porting between 2.x and 3.x.  Major new features and changes
in the 3.3 release series are:

* PEP 380, syntax for delegating to a subgenerator ("yield from")
* PEP 393, flexible string representation (doing away with the
  distinction between "wide" and "narrow" Unicode builds)
* A C implementation of the "decimal" module, with up to 80x speedup
  for decimal-heavy applications
* The import system (__import__) is based on importlib by default
* The new "packaging" module (also known as distutils2, and released
  standalone under this name), implementing the new packaging formats
  and deprecating "distutils"
* The new "lzma" module with LZMA/XZ support
* PEP 405, virtual environment support in core
* PEP 420, namespace package support
* PEP 3151, reworking the OS and IO exception hierarchy
* PEP 3155, qualified name for classes and functions
* PEP 409, suppressing exception context
* PEP 414, explicit Unicode literals to help with porting
* PEP 418, extended platform-independent clocks in the "time" module
* PEP 412, a new key-sharing dictionary implementation that
  significantly saves memory for object-oriented code
* The new "faulthandler" module that helps diagnosing crashes
* The new "unittest.mock" module
* The new "ipaddress" module
* A "collections.ChainMap" class for linking mappings to a single unit
* Wrappers for many more POSIX functions in the "os" and "signal"
  modules, as well as other useful functions such as "sendfile()"
* Hash randomization, introduced in earlier bugfix releases, is now
  switched on by default





