
.. index::
   pair: Python ; Macropy
   pair: Macro; Py


.. _macropy:

=======
MacroPy
=======

.. seealso::

   - https://github.com/lihaoyi/macropy/blob/master/readme.md
   - https://pypi.python.org/pypi/MacroPy
   - https://raw.github.com/lihaoyi/macropy/master/readme.md

.. contents::
   :depth: 3


What is MacroPy
===============

.. seealso::

   - http://en.wikipedia.org/wiki/Macro_%28computer_science%29#Syntactic_macros

**MacroPy** is an implementation of Macros_
in the `Python Programming Language <http://python.org/>`_. 

MacroPy provides a mechanism for user-defined functions (macros) to 
perform transformations on the `abstract syntax tree <http://en.wikipedia.org/wiki/Abstract_syntax_tree>`_ (AST) of Python code 
at module import time. 

This is an easy way to modify the semantics of a python program in ways 
which are otherwise impossible, for example providing an extremely concise 
way of declaring classes::


    @case
    class Point(x, y)

    p = Point(1, 2)
    print p.x   # 1
    print p     # Point(1, 2)


.. _Macros:  http://en.wikipedia.org/wiki/Macro_%28computer_science%29#Syntactic_macros

Apart from this, MacroPy has been used to implement features such as
=====================================================================

.. seealso:: https://github.com/lihaoyi/macropy/blob/master/readme.md


- [Quasiquotes](#quasiquotes), a quick way to manipulate fragments of a 
  program
- [String Interpolation](#string-interpolation), a common feature in 
  many languages
- [Pyxl](#pyxl-integration), integrating XML markup into a Python program
- [Tracing](#tracing) and [Smart Asserts](#smart-asserts)
- [Case Classes](#case-classes), easy [Algebraic Data Types]
  (https://en.wikipedia.org/wiki/Algebraic_data_type) from Scala
- [Pattern Matching](#pattern-matching) from the Functional Programming world
- [Tail-call Optimization](#tco)
- [LINQ to SQL](#linq-to-sql) from C#
- [Quick Lambdas](#quick-lambdas) from Scala and Groovy,
- [Parser Combinators](#parser-combinators), inspired by [Scala's]
  (http://www.suryasuravarapu.com/2011/04/scala-parser-combinators-win.html).

MacroPy is tested to run on
===========================

- [CPython 2.7.2](http://en.wikipedia.org/wiki/CPython)
- [PyPy 1.9](http://pypy.org/)

It does not yet work on `Jython <http://www.jython.org/>`_, and is available 
on `PyPI <https://pypi.python.org/pypi/MacroPy>`.

All of these are advanced language features that each would have been a 
massive effort to implement in the `CPython <http://en.wikipedia.org/wiki/CPython>`_
interpreter. 

Using macros, the implementation of each feature fits in a single file, 
often taking less than 40 lines of code.

MacroPy is very much a work in progress, for the `MIT class <http://web.mit.edu/>`_
`6.945: Adventures in Advanced Symbolic Programming <http://groups.csail.mit.edu/mac/users/gjs/6.945/>`_

Although it is constantly in flux, all of the examples with source code 
represent already-working functionality. 

The rest will be filled in over the coming weeks.


Inspired by
===========

.. seealso::

   - https://bitbucket.org/birkenfeld/karnickel
   - https://code.google.com/p/metapython/
   - https://github.com/dropbox/pyxl

::

    Am 13.05.2013 19:17, schrieb Haoyi Li:
    > We were aware of Karnickel before we started, along with MetaPython
    > (https://code.google.com/p/metapython/) and Pyxl (https://github.com/dropbox/pyxl)
    >
    > Apart from being abandoned, neither of the first two really demonstrates any
    > usability (although Pyxl is used quite heavily), which is why we went ahead with
    > MacroPy.
    
    
    
MacroPy source code
===================

.. seealso::

   - https://raw.github.com/lihaoyi/macropy

