

.. index::
   pair: Building tool ; Pants (Python)

.. _using_pants_for_python:

==================================
Using Pants for Python development
==================================

.. seealso::

   - https://pantsbuild.github.io/python-readme.html
   - :ref:`pex_pants`


Introduction
=============

Pants makes the manipulation and distribution of hermetically sealed Python 
environments painless.



Pants and PEX
==============

The lingua franca of Pants is the PEX file (PEX itself does not stand for 
anything in particular, though in spirit you can think of it as a 
“Python EXecutable”.)

PEX files are single-file lightweight virtual Python environments.

The only difference is no virtualenv setup instructions or pip install foo 
bar baz. 

PEX files are self-bootstrapping Python environments with no strings attached 
and no side-effects. 

Just a simple mechanism that unifies both your development and your deployment.
