
.. index::
   pair: gdb ; 7.5.0


.. _gdb_7_5_0:

====================================================
GDB 7.5.0  (August 17th, 2012: GDB 7.5 Released!)
====================================================


.. seealso::

   - https://www.gnu.org/software/gdb/news/

.. contents::
   :depth: 3


Introduction
============


Release 7.5 of GDB, the GNU Debugger, is now available via anonymous
FTP.  GDB is a source-level debugger for Ada, C, C++, Objective-C,
Pascal and many other languages.  GDB can target (i.e., debug programs
running on) more than a dozen different processor architectures, and GDB
itself can run on most popular GNU/Linux, Unix and Microsoft Windows
variants.

You can download GDB from the GNU FTP server in the directory:

        ftp://ftp.gnu.org/gnu/gdb

The vital stats::

  Size  md5sum                            Name
  21MB  24a6779a9fe0260667710de1b082ef61  gdb-7.5.tar.bz2
  28MB  c9f5ed81008194f8f667f131234f3ef0  gdb-7.5.tar.gz


News
=====


- Go language support.
- New targets (x32 ABI, microMIPS, Renesas RL78, HP OpenVMS ia64).
- More Python scripting improvements.
- SDT (Static Defined Tracing) probes support with SystemTap probes.
- GDBserver improvements (stdio connections, target-side evaluation of 
  breakpoint conditions, remote protocol improvements).
- Other miscellaneous improvements (ability to stop when a shared library is 
  loaded/unloaded, dynamic printf, etc).
- Reverse debugging on ARM.
- The binary "gdbtui" has been abandoned and can no longer be built. 
  Use "gdb -tui" instead. 


