

.. index::
   pair: Android; Pintool
   ! Pintool

.. _pintool:

=======================================
Pintool
=======================================


.. seealso::

   - http://www.pintool.org/
   - http://software.intel.com/en-us/articles/pintool-downloads
   - http://software.intel.com/sites/default/files/article/256671/pindroid-tutorial-01_1.pdf


.. contents::
   :depth: 3


Introduction
============


Pin is a dynamic binary instrumentation engine. Instrumentation is a technique
that inserts code into a program to collect run

Pin allows a tool to insert arbitrary code (written in C or C++) in arbitrary places in the
executable. The code is added dynamically while the executable is running.

Pin provides a rich API that abstracts away the underlying instruction set idiosyncracies and
allows context information such as register contents to be passed to the injected code as
parameters. Pin automatically saves and restores the registers that are overwrit
ten by the injected code so the application continues to work.

Pin includes the source code for a large number of example instrumentation tools
like basic block profilers, cache simulators, instruction trace generators, etc.
