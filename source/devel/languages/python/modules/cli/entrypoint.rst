

.. index::
   pair: Cli ; entrypoint 

.. _python_entrypoint:

=========================
Python entrypoint module
=========================

.. seealso::

   - http://pypi.python.org/pypi/entrypoint/

.. contents::
   :depth: 3
   
Introduction
============   

This is a decorator library that helps one to write small scripts in Python.

There are three main features that it provides:

* Automatically running a function when a script is called directly, but
  not when it is included as a module.

* Automatically generating argument parsers from function signatures and
  docstrings

* Automatically opening and closing files (with a codec or as binary) when
  a function is called and returns.

The raison d'être of this library is to be convenient, and it makes some
sacrifices in other areas. Notably there are some stringent conditions on
the order of application of decorators.



