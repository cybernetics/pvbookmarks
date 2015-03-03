
.. index::
   pair: C ; uClibc
   ! uClibc

.. _uclibc:

============
uClibc
============

.. seealso::

   - http://www.uclibc.org


Introduction
=============

A C library for embedded Linux

uClibc (aka µClibc/pronounced yew-see-lib-see) is a C library for developing
embedded Linux systems.

It is much smaller than the GNU C Library, but nearly all applications supported
by glibc also work perfectly with uClibc. Porting applications from glibc to uClibc
typically involves just recompiling the source code.

uClibc even supports shared libraries and threading. It currently runs on standard
Linux and MMU-less (also known as µClinux) systems with support for alpha, amd64,
ARM, Blackfin, cris, h8300, hppa, i386, i960, ia64, m68k, mips/mipsel, PowerPC,
SH, SPARC, and v850 processors.

If you are building an embedded Linux system and you find that glibc is eating
up too much space, you may want to consider using uClibc.

If you are building a huge fileserver with 12 Terabytes of storage, then using
glibc may make more sense. Unless, for example, that 12 Terabytes will be
Network Attached Storage and you plan to burn Linux into the system's firmware...


uClibc source code
==================

We allow anonymous (read-only) Git access to everyone.

To grab a copy of the latest version of uClibc using anonymous git access::

    git clone git://uclibc.org/uClibc.git






