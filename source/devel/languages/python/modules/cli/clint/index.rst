

.. index::
   pair: CLI ; Clint

.. _clint:

=======================
clint 
=======================

.. seealso::

   - https://github.com/kennethreitz/clint


**Clint** is a module filled with a set of awesome tools for developing
commandline applications.


**C** ommand
**L** ine
**IN** terface
**T** ools
. 


Clint is awesome. Crazy awesome. It supports colors, but detects if the session 
is a TTY, so doesn't render the colors if you're piping stuff around. Automagically.

Awesome nest-able indentation context manager. 

Example: (``with indent(4): puts('indented text')``). 

It supports custom email-style quotes. Of course, it supports color too, if and when needed.

It has an awesome Column printer with optional auto-expanding columns. It detects 
how wide your current console is and adjusts accordingly. It wraps your words 
properly to fit the column size. With or without colors mixed in. All with a 
single function call.

The world's easiest to use implicit argument system w/ chaining methods for 
filtering. Seriously. 


Run the various executables in examples_ to get a good feel for what Clint offers.

.. _examples: https://github.com/kennethreitz/clint/tree/master/examples

You'll never want to not use it.



Current Features:
-----------------
- Little Documentation (bear with me for now)
- CLI Colors and Indents
- Extremely Simple + Powerful Column Printer
- Iterator-based Progress Bar
- Implicit Argument Handling
- Simple Support for Incoming Unix Pipes
- Application Directory management


Future Features:
----------------
- Documentation!
- Simple choice system ``Are you sure? [Yn]``
- Suggestions welcome.





