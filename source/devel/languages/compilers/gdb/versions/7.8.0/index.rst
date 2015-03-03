
.. index::
   pair: GDB ; 7.8.0


.. _gdb_7_8_0:

===================================================
GDB 7.8.0  (July 29th, 2014: GDB 7.8 Released!)
===================================================

.. seealso::

   - https://www.gnu.org/software/gdb/news/

.. contents::
   :depth: 3


News
=====

 Changes in this release include:

- Guile scripting support.
- Python scripting enhancements.
- New commands, options, convenience variables/options.
- Remote Protocol and GDBserver enhancements.
- New target configurations (PowerPC64 GNU/Linux little-endian).
- btrace enhancements.
- ISO C99 variable length automatic arrays support.
- The "compare-sections" command now works on all targets.
- The "target native" command now connects to the native target. 

See the NEWS file for a more complete and detailed list of what this release 
includes. 

June 11th, 2014: GDB 7.8 branch created
========================================

The GDB 7.8 branch (gdb-7.8-branch) has been created. To check out a copy of 
the branch use::

    git clone --branch gdb-7.8-branch ssh://sourceware.org/git/binutils-gdb.git
