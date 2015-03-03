
.. index::
   pair: GCC; 4.9.0


.. _gcc_4.9.0:

=============================
GCC 4.9.0 (22 avril 2014)
=============================


.. seealso::

   - http://gcc.gnu.org/gcc-4.9/changes.html


.. contents::
   :depth: 3


Announce
=========

One year and one month passed from the time when the last major version
of the GNU Compiler Collection has been announced, so it is the time again
to announce a new major GCC release, 4.9.0.

GCC 4.9.0 is a major release containing substantial new
functionality not available in GCC 4.8.x or previous GCC releases.

The Local Register Allocator, introduced in GCC 4.8.0 for ia32 and
x86-64 targets only, is now used also on the Aarch64, ARM, S/390
and ARC targets by default and on PowerPC and RX targets optionally.

There have been substantial improvements to C++ devirtualization
and various scalability bottlenecks in the interprocedural optimizations
and LTO have been fixed.

Support for various C++14 additions have been added to the C++ Front End,
on the standard C++ library side the most important addition is
support for the C++11 <regex>.

GCC 4.9.0 supports the OpenMP 4.0 standard for C and C++, and a partial
implementation of the Cilk Plus extension for data and task parallelism.

Various kinds of undefined behaviors in programs can be now diagnosed at
runtime through Undefined Behavior Sanitizer.

Support for the new little-endian powerpc64le-linux platform has been added,
which defaults to the new PowerPC ELFV2 ABI.
On x86-64 and ia32, support for the AVX-512 instruction set has been
implemented.



See http://gcc.gnu.org/gcc-4.9/changes.html for more information about changes 
in GCC 4.9.
