
.. index::
   pair: Language ; M4
   ! M4


.. _m4:

===================
M4 language
===================


.. seealso::

   - https://fr.wikipedia.org/wiki/GNU_m4
   - https://savannah.gnu.org/projects/m4



.. contents::
   :depth: 3

Introduction
============


``GNU M4`` est la version GNU du préprocesseur de macro M4. Il est conçu pour passer
outre de nombreuses limites rencontrées dans les M4 traditionnels, telles que:

- la taille maximum des lignes;
- la taille maximum d'une macro;
- Le nombre maximal de macros.

Retirer de telles limites est l'un des buts définis des projets GNU.

Le package `GNU autoconf <autoconf>` fait un usage intensif des fonctions de GNU M4.


Savannah
=========

.. seealso:: https://savannah.gnu.org/projects/m4

This project is part of the GNU Project.

GNU M4 is an implementation of the traditional Unix macro processor. It is mostly
SVR4 compatible although it has some extensions (for example, handling more
than 9 positional parameters to macros).

GNU m4 also has built-in functions for including files, running shell commands,
doing arithmetic, etc.

GNU M4 is a macro processor in the sense that it copies its input to the output
expanding macros as it goes. Macros are either builtin or user-defined and can
take any number of arguments.

Besides just doing macro expansion m4 has builtin functions for including named
files, running UNIX commands, doing integer arithmetic, manipulating text in
various ways, recursion etc... m4 can be used either as a front-end to a compiler
or as a macro processor in its own right.

One of the biggest users of GNU M4 is the `GNU autoconf project <autoconf>`.


M4 source code
==============

.. seealso::

   - https://savannah.gnu.org/git/?group=m4
   - http://savannah.gnu.org/maintenance/UsingGit


Anonymous checkout
-------------------

::

    git clone git://git.savannah.gnu.org/m4.git









