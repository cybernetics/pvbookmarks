

.. index::
   python pypy


=======
pypy
=======

.. seealso::

   - http://pypy.org/
   - http://fr.wikipedia.org/wiki/PyPy


.. image:: pypy-logo.png

PyPy est une mise en œuvre du langage Python écrite elle-même en Python, avec
une architecture flexible

pypi speed
==========

.. seealso:: http://speed.pypy.org/


Sources
=======

::

    hg clone https://pvergain@bitbucket.org/pypy/pypy



.. index::
   pair: Architecture ; pypi
   
   
Architecture pypi
=================

.. seealso:: http://www.aosabook.org/en/pypy.html

PyPy is a Python implementation and a dynamic language implementation framework.

This chapter assumes familiarity with some basic interpreter and compiler 
concepts like bytecode and constant folding.

Little History
--------------

Python is a high-level, dynamic programming language. It was invented by 
the Dutch programmer Guido van Rossum in the late 1980s. 

Guido's original implementation is a traditional bytecode interpreter written 
in C, and consequently known as CPython. 

There are now many other Python implementations. 

Among the most notable are Jython, which is written in Java and allows for 
interfacing with Java code, IronPython, which is written in C# and interfaces 
with Microsoft's .NET framework, and PyPy, the subject of this chapter. 

CPython is still the most widely used implementation and currently the only one 
to support Python 3, the next generation of the Python language. 

This chapter will explain the design decisions in PyPy that make it different 
from other Python implementations and indeed from any other dynamic language 
implementation.


Versions
========

.. toctree::
   :maxdepth: 4

   versions/index



