

.. index::
   pair: Python ; Mypy


.. _mypy:

=========
mypy 
=========

.. seealso::

   - http://www.mypy-lang.org/


.. contents::
   :depth: 3

Introduction
============

The mypy programming language is an experimental Python variant that aims to 
combine the benefits of dynamic (or "duck") typing and static typing. 

Our goal is to have the expressive power and convenience of Python combined 
with compile-time type checking. 

The long-term goal is to also support efficient compilation to native code, 
without the need of a heavy-weight VM.

Mypy is still in development. 

The current prototype supports type checking and running programs using a 
standard Python VM, i.e. there is no performance boost yet (development roadmap). 

A significant subset of Python features is supported.


Why mypy ?
===========

Compile-time type checking
--------------------------

Static typing makes it easier to find bugs and with less debugging (and with 
less staring at long stack traces). 

Stress-free code maintenance
----------------------------

Type declarations act as machine-checked documentation. 

Static types can make your code easier to understand and modify, for yourself 
and other programmers. 

Grow your programs from dynamic to static typing
------------------------------------------------

You can develop programs with dynamic types and only add static typing after 
your code has matured. 
This way you do not have maintain type declarations in initial development 
when the code is still changing rapidly. 

Performance
------------

Static typing has the potential to enable high, scalable and predictable 
efficiency, without the slow warm-up seen in many JIT compilers. 

IDE goodness
------------

The type system makes it practical to add support for :ref:`Eclipse <eclipse>` /Visual Studio 
style IDE convenience for mypy programs, including precise and reliable code 
completion. 



 

