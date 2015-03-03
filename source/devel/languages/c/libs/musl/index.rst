
.. index::
   pair: C ; musl
   pair: libC ; musl
   ! musl

.. _musl:

============
musl
============

.. seealso::

   - http://www.musl-libc.org/


.. contents::
   :depth: 3
   
   
.. figure:: musl2.png
   :align: center

Introduction
=============

Welcome to the home of musl, a new standard library to power a new generation 
of Linux-based devices. musl is lightweight, fast, simple, free, and strives to 
be correct in the sense of standards-conformance and safety.


Introduction to musl
=====================

.. seealso::

   - http://www.musl-libc.org/intro.html
   
   
Say it like	“mussel” or “muscle”
Provides the standard C/POSIX library and extensions
Licensed under	permissive MIT license

Use it on	Linux x86, x86_64, ARM, MIPS, Microblaze, PowerPC
Use it for	the next generation of Linux-based devices

musl provides consistent quality and implementation behavior from tiny embedded 
systems to full-fledged servers. 

Minimal machine-specific code means less chance of breakage on minority 
architectures and better success with “write once run everywhere” C development.

musl's efficiency is unparalleled in Linux libc implementations. 

Designed from the ground up for static linking, musl carefully avoids pulling 
in large amounts of code or data that the application will not use. 

Dynamic linking is also efficient; by integrating the entire standard library 
implementation, including threads, math, and even the dynamic linker itself into 
a single shared object, most of the startup time and memory overhead of dynamic 
linking have been eliminated.

musl features the first post-NPTL implementation of POSIX threads for Linux, and 
the first aimed at complete conformance and robustness. 

Thread cancellation has been re-designed to avoid serious race conditions in the 
original NPTL design. 
As for efficiency, the whole threads implementation weighs in at around 10-20k 
depending on target architecture and compiler settings.

Not only the threads implementation, but all code in musl has been designed for 
realtime-quality robustness. Low-memory or resource exhaustion conditions are 
never fatal. 

musl has no unnecessary dynamic allocation and no unrecoverable late failures. 

All error conditions can be detected and handled by applications; interfaces for 
which an application could not reasonably handle failure do not fail.

Using musl maximizes application deployability. Its permissive MIT license is 
compatible with all FOSS licenses, static-linking-friendly, and makes commercial 
use painless too. Binaries statically linked with musl have no external dependencies,
even for features like DNS lookups or character set conversions that are implemented 
with dynamic loading on glibc. An application can really be deployed as a single 
binary file and run on any machine with the appropriate instruction set architecture 
and Linux kernel or Linux syscall ABI emulation layer.

Finally, musl has simple source code and source tree layout, so it’s easy to 
customize or track down the cause of unexpected behavior or bugs, or simply 
learn how the library works.

Comparison of C/POSIX standard library implementations for Linux
================================================================

.. seealso::

   - http://www.etalabs.net/compare_libcs.html

musl source code
==================

.. seealso::

   - http://git.musl-libc.org/cgit/musl/tree
   
   







