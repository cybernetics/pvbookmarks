
.. index::
   pair: GNU Project Debugger; GDB
   ! GDB


.. _gdb:

=============================
GDB: The GNU Project Debugger
=============================

.. seealso::

   - https://www.gnu.org/software/gdb/
   - http://sourceware.org/git/gitweb.cgi?p=gdb.git
   - http://www.sourceware.org/gdb/documentation/
   - http://en.wikipedia.org/wiki/GNU_Debugger


.. figure:: archer.jpg
   :align: center

   *Le logo de GDB*


.. contents::
   :depth: 3

What is GDB ?
==============

``GDB``, the GNU Project debugger, allows you to see what is going on *inside*
another program while it executes -- or what another program was doing at the
moment it crashed.

GDB can do four main kinds of things (plus other things in support of these) to help you catch bugs in the act:

- Start your program, specifying anything that might affect its behavior.
- Make your program stop on specified conditions.
- Examine what has happened, when your program has stopped.
- Change things in your program, so you can experiment with correcting the
  effects of one bug and go on to learn about another.

The program being debugged can be written in Ada, C, C++, Objective-C, Pascal
(and many other languages).

Those programs might be executing on the same machine as GDB (native) or
on another machine (remote).

GDB can run on most popular UNIX and Microsoft Windows variants.


GDB source code
===============

.. seealso::

   - http://sourceware.org/git/gitweb.cgi?p=gdb.git


GDB projects
===============


.. toctree::
   :maxdepth: 4

   projects/index


GDB versions
============


.. toctree::
   :maxdepth: 4


   versions/index
