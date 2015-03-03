

.. index::
   pair: python ; cython


.. _cython:

=========
cython
=========

.. seealso::

   - http://cython.org/
   - http://docs.cython.org/src/quickstart/overview.html


.. image:: cython-logo-light.png


Cython is a programming language based on Python, with extra syntax
allowing for optional static type declarations. It aims to become a superset
of the Python_ language which gives it high-level, object-oriented,
functional, and dynamic programming.  The source code gets translated
into optimized C/C++ code and compiled as Python extension modules.
This allows for both very fast program execution and tight integration
with external C libraries, while keeping up the high programmer
productivity for which the Python language is well known.

The primary Python execution environment is commonly referred to as
CPython, as it is written in C.  Other major implementations use Java
(Jython Jython_), C# (IronPython IronPython_) and Python itself
(PyPy PyPy_).  Written in C, CPython has been conducive to wrapping
many external libraries that interface through the C language.  It
has, however, remained non trivial to write the necessary glue code in
C, especially for programmers who are more fluent in a high-level
language like Python than in a close-to-the-metal language like C.

Originally based on the well-known Pyrex Pyrex_, the Cython project has
approached this problem by means of a source code compiler that
translates Python code to equivalent C code.  This code is executed
within the CPython runtime environment, but at the speed of compiled C
and with the ability to call directly into C libraries.
At the same time, it keeps the original interface of the Python
source code, which makes it directly usable from Python code.  These
two-fold characteristics enable Cython's two major use cases:
extending the CPython interpreter with fast binary modules, and
interfacing Python code with external C libraries.

While Cython can compile (most) regular Python code, the generated C
code usually gains major (and sometime impressive) speed improvements
from optional static type declarations for both Python and C types.
These allow Cython to assign C semantics to parts of the code, and to
translate them into very efficient C code.  Type declarations can
therefore be used for two purposes: for moving code sections from
dynamic Python semantics into static-and-fast C semantics, but also
for directly manipulating types defined in external libraries.  Cython
thus merges the two worlds into a very broadly applicable programming
language.

.. _IronPython: http://www.codeplex.com/IronPython
.. _Jython: http://www.jython.org/
.. _PyPy: http://codespeak.net/pypy
.. _Pyrex: http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/
.. _Python:  http://python.org



Wrapping C++ Classes in Cython
==============================

.. seealso:: http://wiki.cython.org/WrappingCPlusPlus


This page aims to get you quickly up to speed so you can wrap C++ interfaces with
a minimum of pain and 'surprises'.

In the past, Pyrex (and later, Cython) only supported wrapping of C APIs, and
not C++. To wrap C++, one had to write a pure-C shim, containing functions
for constructors/destructors and method invocations. Object pointers were passed
around as opaque void pointers, and cast to/from object pointers as needed.

This approach did work, but it got awfully messy and error-prone when trying to
wrap APIs with large class hierarchies and lots of inheritance. Later versions
of Pyrex and Cython simplified this somewhat by allowing textual definitions
that would get generated literally into the output sources. This was still error
prone but was at least capable of interfacing with a lot of existing code through
a somewhat self-contained declaration.

Since then, a lot of work went into improving Cython and starting with
version 0.13, it offers heavily extended support for C++ code in 'real'
language syntax. The approach described in this document will help you wrap a
lot of C++ code with only little effort. Due to the vast landscape that C++
considers valid syntax, there are still some limitations, which we will discuss
at the end of the document.
