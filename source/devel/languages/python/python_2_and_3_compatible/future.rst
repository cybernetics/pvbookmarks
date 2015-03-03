
.. index::
   pair: Python ; Future
   pair: Python ; futurize
   pair: Python ; pasteurize



.. _future_module:

=========================================
Future module
=========================================

.. seealso::

    - http://python-future.org/index.html


.. contents::
   :depth: 3


Description
===========

``python-future`` is the missing compatibility layer between Python 2 and Python 3. 

It allows you to use a single, clean Python 3.x-compatible codebase to support 
both Python 2 and Python 3 with minimal overhead

Automatic conversion to Py2/3-compatible code
=============================================

future comes with two scripts called futurize and pasteurize to aid in making 
Python 2 code or Python 3 code compatible with both platforms (Py2&3). 

It is based on 2to3 and uses fixers from lib2to3, lib3to2, and python-modernize, 
as well as custom fixers.

futurize
--------

``futurize`` passes Python 2 code through all the appropriate fixers to turn it 
into valid Python 3 code, and then adds __future__ and future package imports 
so that it also runs under Python 2.

pasteurize
----------

For conversions from Python 3 code to Py2/3, use the ``pasteurize`` script 
instead. 

This converts Py3-only constructs (e.g. new metaclass syntax) to Py2/3 compatible 
constructs and adds __future__ and future imports to the top of each module.

In both cases, the result should be relatively clean Py3-style code that runs 
mostly unchanged on both Python 2 and Python 3.


