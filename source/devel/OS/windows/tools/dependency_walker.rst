
.. index::
   pair: Dlls; DependencyWalker


.. _dependency_walker:

=========================
Dependency Walker
=========================

.. seealso::

   - http://www.dependencywalker.com/

Introduction
============

Dependency Walker is a free utility that scans any 32-bit or 64-bit Windows
module (exe, dll, ocx, sys, etc.) and builds a hierarchical tree diagram of
all dependent modules. For each module found, it lists all the functions that
are exported by that module, and which of those functions are actually being
called by other modules. Another view displays the minimum set of required
files, along with detailed information about each file including a full path
to the file, base address, version numbers, machine type, debug information,
and more.

Dependency Walker is also very useful for troubleshooting system errors
related to loading and executing modules. Dependency Walker detects many
common application problems such as missing modules, invalid modules,
import/export mismatches, circular dependency errors, mismatched machine types
of modules, and module initialization failures.
