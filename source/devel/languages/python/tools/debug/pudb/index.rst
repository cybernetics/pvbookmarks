

.. index::
   pair: Python tools; Pudb


.. _debug_pudb:

====================
PuDB
====================


.. seealso::

   - https://pypi.python.org/pypi/pudb
   - http://wiki.tiker.net/PuDB


.. contents::
   :depth: 3


Description
===========

A full-screen, console-based Python debugger

PuDB is a full-screen, console-based visual debugger for Python.

Its goal is to provide all the niceties of modern GUI-based debuggers in a more
lightweight and keyboard-friendly package.

PuDB allows you to debug code right where you write and test it--in a terminal.

If you've worked with the excellent (but nowadays ancient) DOS-based Turbo Pascal
or C tools, PuDB's UI might look familiar.



PuDB Source code
================

.. seealso::

   - http://git.tiker.net/pudb.git


::

    git clone http://git.tiker.net/trees/pudb.git



Programming PuDB
================

At the programming language level, PuDB displays the same interface as Python's
built-in pdb module.

Just replace pdb with pudb. (One exception: run is called runstatement.)


License and Dependencies
========================

PuDB is distributed under the MIT license.

It relies on the following excellent pieces of software:

- Ian Ward's urwid_ console UI library
- Georg Brandl's pygments_ syntax highlighter


.. _urwid : http://excess.org/urwid
.. _pygments: http://pygments.org/



