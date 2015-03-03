

.. index::
   pair: Boost versions; 1.56


.. _boost_cplusplus_1.56:

=============================================
Boost C++ 1.56 (August 7th, 2014 16:08 GMT)
=============================================


.. seealso:: 

   - http://www.boost.org/users/history/version_1_56_0.html



Modularization
===============

Boost version control has migrated to a system using git submodules. 

This shouldn't make too much of a difference to users, although the directory 
structure is now a bit different.

Parts of some libraries have been moved into different modules, and several 
new modules have been extracted from existing code. 

All header paths should remain the same. The new modules are:

- Assert: Customizable assert macros. Maintained by Peter Dimov.
- Core: Core utilities used by other libraries, with minimal dependencies. 
  Maintained by Peter Dimov, Glen Fernandes and Andrey Semashev.
- Lexical_Cast: General literal text conversions, such as an int represented a 
  string, or vice-versa, from Kevlin Henney.
- Throw_Exception: A common infrastructure for throwing exceptions from Boost 
  libraries, from Emil Dotchevski.
- Winapi: Windows API declarations without <windows.h>, for internal Boost use.



New Libraries
=============

- Align: Memory alignment functions, allocators, and adaptors, from Glen Fernandes.
- Type_Index: Runtime/Compile time copyable type info, from Antony Polukhin.



