

.. index::
   pair: Pyston ; Python implementation
   ! Pyston


.. _pyston:

=========
Pyston 
=========

.. seealso:: 

   - https://github.com/dropbox/pyston
   - :ref:`pyston_12_avril_2014`
   - https://tech.dropbox.com/2014/04/introducing-pyston-an-upcoming-jit-based-python-implementation/
   
.. contents::
   :depth: 3

Description
============

.. seealso::

   - https://tech.dropbox.com/2014/04/introducing-pyston-an-upcoming-jit-based-python-implementation/

An open-source Python implementation using JIT techniques.

Pyston is a new, under-development Python implementation built using LLVM and 
modern JIT techniques with the goal of achieving good performance.

Current state
=============

Pyston "works", though doesn't support very much of the Python language, and 
currently is not very useful for end-users.

Currently, Pyston targets Python 2.7, only runs on x86_64 platforms, and only 
has been tested on Ubuntu.  
Support for more platforms -- along with Python 3 compatibility -- is planned 
for the future, but this is the initial target due to the fact that Dropbox is 
on this setup internally.

Benchmarks are not currently that meaningful since the supported set of benchmarks 
is too small to be representative; with that caveat, Pyston seems to have better 
performance than CPython but lags behind PyPy.

Roadmap
========

Pyston is still an early-stage project so it is hard to project with much 
certainty, but here's what we're planning at the moment:

Current focus: more language features
======================================

- Exceptions
- Class inheritance, metaclasses
- Default arguments, keywords, \args, kwargs
- Closures
- Generators
- Integer promotion

Articles
=========

.. toctree::
   :maxdepth: 3
   
   articles/index
   

