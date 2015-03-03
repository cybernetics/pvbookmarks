

.. index::
   pair: Debug; wdb


.. _wdb:

====================
wdb
====================


.. seealso::

   - https://github.com/Kozea/wdb
   - http://www.rkblog.rk.edu.pl/w/p/debugging-python-code-browser-wdb-debugger/


.. contents::
   :depth: 3


Description
===========

**wdb** is a full featured web debugger based on a client-server architecture.

The wdb server which is responsible of managing debugging instances along with 
browser connections (through websockets) is based on [Tornado](http://www.tornadoweb.org/).

The wdb clients allow step by step debugging, in-program python code execution, 
code edition (based on [CodeMirror](http://codemirror.net/)) setting breakpoints...

Due to this architecture, all of this is fully compatible with **multithread** 
and **multiprocess** programs.

**wdb** works with python 2, python 3 and pypy.

Even better, it is possible to debug a python 2 program with a wdb server running 
on python 3 and vice-versa or debug a program running on a computer with a debugging 
server running on another computer inside a web page on a third computer!

In other words it's a very enhanced version of pdb directly in your browser with nice features.

