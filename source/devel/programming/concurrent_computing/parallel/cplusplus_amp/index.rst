

.. index::
   pair: C++ AMP ; Multiprocessing
   pair: Accelerated ; Massive Parallelism
   pair: Massive ; Parallelism
   ! AMP


.. _amp:

==============================================
C++ AMP (C++ Accelerated Massive Parallelism)
==============================================


.. seealso::

   - http://en.wikipedia.org/wiki/C%2B%2B_AMP
   - http://msdn.microsoft.com/en-us/library/vstudio/hh265136.aspx



.. contents::
   :depth: 3

Microsoft introduction
======================

.. seealso::

   - http://msdn.microsoft.com/en-us/library/vstudio/hh265136.aspx


C++ Accelerated Massive Parallelism (C++ AMP) accelerates execution of C++ code
by taking advantage of data-parallel hardware such as a graphics processing unit
(GPU) on a discrete graphics card.

By using C++ AMP, you can code multi-dimensional data algorithms so that execution
can be accelerated by using parallelism on heterogeneous hardware.

The C++ AMP programming model includes multidimensional arrays, indexing,
memory transfer, tiling, and a mathematical function library.

You can use C++ AMP language extensions to control how data is moved from the
CPU to the GPU and back, so that you can improve performance.


Wikipedia introduction
======================

.. seealso::

   - http://en.wikipedia.org/wiki/C%2B%2B_AMP


C++ Accelerated Massive Parallelism (C++ AMP) is a library implemented on
DirectX 11 and an open specification from Microsoft for implementing data
parallelism directly in C++.

It is intended to make programming GPUs easy for the developer by supporting a
range of expertise from none (in which case the system does its best) to being
more finely controllable, but still portable.

Code that cannot be run on GPUs will fall back onto one or more CPUs instead
and use SSE instructions.

The Microsoft implementation is included in Visual Studio 2012, including
debugger and profiler support. Support for other platforms and hardware may
become available from Microsoft or other compiler or hardware vendors.

The initial C++ AMP release from Microsoft requires at least Windows 7 or Windows
Server 2008 R2.

Microsoft added the restrict(amp) feature, which can be applied to any function
(including lambdas) to declare that the function can be executed on a C++
AMP accelerator. The restrict keyword instructs the compiler to statically check
that the function uses only those language features that are supported by most GPUs,
for example, void myFunc() restrict(amp) {…} Microsoft or other implementers of
the open C++ AMP spec could add other restrict specifiers for other purposes,
including for purposes that are unrelated to C++ AMP.

Beyond the new language feature, the rest of C++ AMP is available through the
<amp.h> header file in the concurrency namespace.

The key C++ AMP classes are: array (container for data on an accelerator),
array_view (wrapper for data), index (N-dimensional point), extent (N-dimensional size),
accelerator (computational resource, such as a GPU, on which to allocate memory
and execute), and accelerator_view (view of an accelerator).

There is also a global function, parallel_for_each, which you use to write a
C++ AMP parallel loop.

Book on C++ AMP
===============

.. seealso::

   - http://www.gregcons.com/cppamp/


Articles
========

Programmez ! , Janvier 2013
---------------------------

:titre: Prise en mains de C++ AMP.





