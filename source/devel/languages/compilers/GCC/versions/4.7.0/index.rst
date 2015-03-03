
.. index::
   pair: GCC; 4.7.0


.. _gcc_4.7.0:

=============================
GCC 4.7.0 (22 mars 2012)
=============================


.. seealso::

   - http://gcc.gnu.org/gcc-4.7/changes.html
   - https://linuxfr.org/news/sortie-de-la-version-4-7-du-compilateur-gcc


.. contents::
   :depth: 3


Introduction
============

::

    From: Richard Guenther <rguenther@suse.de>
    Date: 2012/3/22
    Subject: GCC 4.7.0 Released
    To: gcc-announce@gcc.gnu.org


Today the GCC development team celebrates the 25th anniversary of the GNU
Compiler Collection.

When Richard Stallman announced the first public release of GCC in
1987, few could have imagined the broad impact that it has had.  It
has prototyped many language features that later were adopted as part
of their respective standards -- everything from "long long" type to
transactional memory. It deployed an architecture-neutral automatic
vectorization facility, OpenMP, and Polyhedral loop nest optimization.

It has provided the toolchain infrastructure for the GNU/Linux
ecosystem used everywhere from Google and Facebook to financial
markets and stock exchanges.  We salute and thank the hundreds
of developers who have contributed over the years to make
GCC one of the most long-lasting and successful free software projects
in the history of this industry.

As a special present we have prepared the release of GCC 4.7.0 which
continues the series of free software high-quality industry-standard
compilers.

GCC 4.7.0 is a major release, containing substantial new
functionality not available in GCC 4.6.x or previous GCC releases.

GCC 4.7 features support for software transactional memory on
selected architectures.  The C++ compiler supports a bigger
subset of the new ISO C++11 standard such as support for atomics
and the C++11 memory model, non-static data member initializers,
user-defined literals, alias-declarations, delegating constructors,
explicit override and extended friend syntax.  The C compiler adds support
for more features from the new ISO C11 standard.  GCC now supports
version 3.1 of the OpenMP specification for C, C++ and Fortran.

The link-time optimization (LTO) framework has seen improvements
with regards to scalability, stability and resource needs.  Inlining
and interprocedural constant propagation have been improved.

GCC 4.7 now supports various new GNU extensions to the DWARF debugging
information format, like entry value and call site information, a typed
DWARF stack and a more compact macro representation.

Extending the widest support for hardware architectures in the
industry, GCC 4.7 gains support for Adapteva's Epiphany processor,
National Semiconductor's CR16, and TI's C6X as well as Tilera's
TILE-Gx and TILEPro families of processors.  The x86
family support has been extended by the Intel Haswell and AMD Piledriver
architectures.  ARM has gained support for the Cortex-A7 family.

See
