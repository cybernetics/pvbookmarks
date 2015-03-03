


.. index::
   pair: Autotools; Make
   pair: GNU; Make
   ! GNU make
   ! Make

.. _gnu_make:
.. _make:

==========
GNU Make
==========


.. seealso::

   - http://fr.wikipedia.org/wiki/Make
   - http://www.gnu.org/software/make/
   - https://savannah.gnu.org/users/psmith

.. contents::
   :depth: 3

Introduction
============

``make`` est un logiciel qui construit automatiquement des fichiers, souvent
exécutables, ou des bibliothèques à partir d'éléments de base tels que
du code source.

Il utilise des fichiers appelés makefile qui spécifient comment
construire les fichiers cibles.

À la différence d'un simple script shell, make exécute les commandes
seulement si elles sont nécessaires.

Le but est d'arriver à un résultat (logiciel compilé ou installé,
documentation créée, etc.) sans nécessairement refaire toutes les
étapes.

make est particulièrement utilisé sur les plateformes UNIX.

Introduction to Make
===========================

.. seealso::

   - http://www.gnu.org/software/make/


Make is a tool which controls the generation of executables and other
non-source files of a program from the program's source files.

Make gets its knowledge of how to build your program from a file called
the makefile, which lists each of the non-source files and how to
compute it from other files.

When you write a program, you should write a makefile for it, so that it
is possible to use Make to build and install the program.

Make source code
===================

.. seealso::

   - http://savannah.gnu.org/projects/make/
   - http://savannah.gnu.org/git/?group=make

::

    git clone git://git.savannah.gnu.org/make.git


Makefiles And Conventions
=========================

.. seealso::

   - https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions
   - https://www.gnu.org/prep/standards/

**We have developed conventions for how to write Makefiles, which all GNU packages
ought to follow**.

It is a good idea to follow these conventions in your program even if you don't
intend it to be GNU software, so that users will be able to build your package
just like many other packages, and will not need to learn anything special before
doing so.

These conventions are found in the chapter `Makefile conventions`_ (147 k characters)
of the `GNU Coding Standards`_ (147 k characters).


.. _`Makefile conventions`:  https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions
.. _`GNU Coding Standards`: https://www.gnu.org/prep/standards/


Make tutorials
===============


.. toctree::
   :maxdepth: 3

   tutorials/index

Make versions
=============


.. toctree::
   :maxdepth: 3

   versions/index





