
.. index::
   pair: Library ; Glibc
   ! Glibc
   ! GNU C Library


.. _glibc:

==========================
The GNU C Library (glibc)
==========================

.. seealso::

   - https://www.gnu.org/software/libc/libc.html
   - http://sourceware.org/glibc/wiki/HomePage
   - http://sourceware.org/glibc/wiki/GlibcGit#Fetching_The_Repository
   - http://sourceware.org/git/?p=glibc.git


.. contents::
   :depth: 3


Overview
=========

Any Unix-like operating system needs a C library: the library which defines the
``system calls`` and other basic facilities such as open, malloc, printf, exit...

The GNU C Library is used as the C library in the GNU systems and most systems
with the Linux kernel.


Project Goals
=============

The GNU C Library is primarily designed to be a portable and high performance
C library. It follows all relevant standards including ISO C11 and POSIX.1-2008.

It is also internationalized and has one of the most complete internationalization
interfaces known.


glibc documentation
====================

.. seealso::

   - https://www.gnu.org/software/libc/documentation.html
   - http://sourceware.org/glibc/wiki/HomePage


glibc source code
==================

.. seealso::

   - http://sourceware.org/git/?p=glibc.git

::

    git clone git://sourceware.org/git/glibc.git


