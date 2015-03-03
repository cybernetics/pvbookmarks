
.. index::
   pair: LLVM; python wrappers
   pair: LLVM; Bitey


.. _python_llvm_wrappers:

=====================
Python llvm wrappers
=====================

.. seealso::

   - http://www.llvmpy.org/

llvmpy is a Python wrapper around the llvm C++ library which allows simple access
to compiler tools.

It can be used for a lot of things, but here are some ideas:

- dynamically create LLVM IR for linking with LLVM IR produced by CLANG or dragonegg
- build machine code dynamically using LLVM execution engine
- use together with PLY or other tokenizer and parser to write a complete compiler
  in Python


Bitey - Bitcode Import Tool
===========================


.. seealso::

   - https://github.com/dabeaz/bitey/

Import LLVM bitcode directly into Python and use it as an extension module.





