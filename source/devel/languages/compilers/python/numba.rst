
.. index::
   pair: Compiler ; numba


.. _numba:

==========================================
Numba (Python to C99/OpenCL/JS compiler )
==========================================

.. seealso::

   - http://www.llvmpy.org/
   - http://pypi.python.org/pypi/numba


Introduction
=============

numba is a NumPy aware dynamic compiler for Python.

It creates LLVM bit-code from Python syntax and then creates a wrapper around
that bitcode to call from Python.

Numba is an Open Source NumPy-aware optimizing compiler for Python
sponsored by Continuum Analytics, Inc.

It uses the remarkable LLVM compiler infrastructure to compile Python syntax to
machine code.

It is aware of NumPy arrays as typed memory regions and so can speed-up
code using NumPy arrays.  Other, less well-typed code will be translated
to Python C-API calls effectively removing the "interpreter" but not removing
the dynamic indirection.

Numba is also not a tracing jit.  It *compiles* your code before it gets
run either using run-time type information or type information you provide
in the decorator.

Numba is a mechanism for producing machine code from Python syntax and typed
data structures such as those that exist in NumPy.

Dependencies:

- LLVM 3.1
- llvm-py (from llvmpy/llvmpy fork)
- numpy
- Meta (from numba/Meta fork)
- Cython


Pycon 2013 Numba: A Dynamic Python compiler for Science
========================================================

.. seealso::

   - https://us.pycon.org/2013/schedule/presentation/130/










