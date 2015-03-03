
.. index::
   pair: GDB ; 7.7.0


.. _gdb_7_7_0:

===================================================
GDB 7.7.0 (February 6th, 2014: GDB 7.7 Released!)
===================================================

.. seealso::

   - https://www.gnu.org/software/gdb/news/
   
   
.. contents::
   :depth: 3


News
=====


- Enhanced Python scripting support.
- Some C++ improvements.
- New commands, options, convenience variables/options.
- Several GDB/MI new commands and enhancements.
- Remote Protocol and GDBserver enhancements.
- New target configurations (Nios II, TI MSP430).
- GDB Windows x64 unwinding data support.
- SystemTap SDT probes support on AArch64 GNU/Linux.
- CTF (Common Trace Format) support.
- New scripts gcore and gdb-add-index.sh.
- Improved arm*-linux record/replay support.
- Removed support for a.out NetBSD and OpenBSD obsolete configurations. ELF 
  variants of these configurations are kept supported.
- The "set|show remotebaud" commands are deprecated in favor of "show|show 
  serial baud". 

See the NEWS file for a more complete and detailed list of what this release includes. 

January 8th, 2014: GDB 7.7 branch created
==========================================

The GDB 7.7 branch (gdb-7.7-branch) has been created. To check out a copy of 
the branch use::

    git clone --branch gdb-7.7-branch ssh://sourceware.org/git/binutils-gdb.git

