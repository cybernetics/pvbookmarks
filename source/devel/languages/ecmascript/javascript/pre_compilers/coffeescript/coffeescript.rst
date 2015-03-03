
.. index::
   pair: Compiler ; Coffeescript


.. _coffeescript_compiler:

======================
coffeescript compiler
======================

.. figure:: CoffeeScript-logo.png
   :align: center


.. seealso::

   - http://jashkenas.github.com/coffee-script/
   - https://github.com/jashkenas/coffee-script/wiki
   - https://github.com/jashkenas/coffee-script/wiki/FAQ
   - http://stackoverflow.com/tags/coffeescript
   - :ref:`javascript_language`


.. contents::
   :depth: 3


Introduction
============

CoffeeScript is a little language that compiles into JavaScript.

Underneath all  of those embarrassing braces and semicolons, JavaScript
has always had a  gorgeous object model at its heart.

CoffeeScript is an attempt to expose the  good parts of JavaScript in
a simple way.

The golden rule of CoffeeScript is: **It's just JavaScript**. The code
compiles  one-to-one into the equivalent JS, and there is no
interpretation at runtime.

You can use any existing JavaScript library seamlessly (and vice-versa).

The compiled output is readable and pretty-printed, passes through JavaScript
Lint without warnings, will work in every JavaScript implementation, and tends
to run as fast or faster than the equivalent handwritten JavaScript.

Installation and Usage
======================

The CoffeeScript compiler is itself written in CoffeeScript, using the Json
parser generator. The command-line version of coffee is available as a Node.js
utility. The core compiler however, does not depend on Node, and can be run
in any JavaScript environment, or in the browser (see "Try CoffeeScript", above).

To install, first make sure you have a working copy of the latest stable
version of Node.js, and npm (the Node Package Manager). You can then install
CoffeeScript with npm::

    npm install -g coffee-script

(Leave off the -g if you don't wish to install globally.)

If you'd prefer to install the latest master version of CoffeeScript, you can
clone the CoffeeScript source repository from GitHub, or download the source
directly. To install the CoffeeScript compiler system-wide under /usr/local,
open the directory and run::

    sudo bin/cake install

If installing on Ubuntu or Debian, be careful not to use the existing
out-of-date package. If installing on Windows, your best bet is probably to
run Node.js under Cygwin. If you'd just like to experiment, you can try the
CoffeeScript Compiler For Windows.

Once installed, you should have access to the coffee command, which can execute
scripts, compile .coffee files into .js, and provide an interactive REPL.

Language Reference
==================

This reference is structured so that it can be read from top to bottom, if you
like. Later sections use ideas and syntax previously introduced. Familiarity
with JavaScript is assumed. In all of the following examples, the source
CoffeeScript is provided on the left, and the direct compilation into
JavaScript is on the right.

Many of the examples can be run (where it makes sense) by pressing the run
button on the right, and can be loaded into the "Try CoffeeScript" console
by pressing the load button on the left.

First, the basics: CoffeeScript uses significant whitespace to delimit blocks
of code. You don't need to use semicolons ; to terminate expressions, ending
the line will do just as well (although semicolons can still be used to fit
multiple expressions onto a single line). Instead of using curly braces { }
to surround blocks of code in functions, if-statements, switch, and try/catch,
use indentation.

Books and Screencasts
=====================

There are a number of excellent books and screencasts to help you get started
with CoffeeScript, some of which are freely available online.

- `The Little Book on CoffeeScript`_ is a brief 5-chapter introduction to
  CoffeeScript, written with great clarity and precision by Alex MacCaw.
- `Smooth CoffeeScript`_ is a reimagination of the excellent book Eloquent
  JavaScript, as if it had been written in CoffeeScript instead. Covers
  language features as well a the functional and object oriented programming
  styles. By E. Hoigaard.


.. _`The Little Book on CoffeeScript`:  http://arcturo.github.com/library/coffeescript/
.. _`Smooth CoffeeScript`: http://autotelicum.github.com/Smooth-CoffeeScript/



Tools
=====

.. toctree::
   :maxdepth: 3
   
   tools/tools
