

.. index::
   pair: CLI ; Bash


.. _unix_shell:

============================================
Bash: The shell for the GNU operating system
============================================


.. contents::
   :depth: 3

Introduction
=============

`Bash <http://en.wikipedia.org/wiki/Bash>`_ is a free software Unix shell written for the GNU Project.
Its name is an acronym which stands for Bourne-again shell. The name is a pun on the name of the Bourne shell (sh),
an early and important  Unix shell written by Stephen Bourne and distributed with Version 7 Unix circa 1978,
and "born again". Bash was created in 1987 by Brian Fox. In 1990 Chet Ramey became the primary maintainer.

Bash is the shell for the GNU operating system from the GNU Project. It can be run on most Unix-like
operating systems. It is the default shell on most systems built on top of the Linux kernel
as well as on Mac OS X and Darwin. It has also been ported to Microsoft Windows using Subsystem
for UNIX-based Applications (SUA), or POSIX emulation provided by `Cygwin <http://en.wikipedia.org/wiki/Cygwin>`_ and
`MSYS <http://en.wikipedia.org/wiki/MinGW>`_ .


.. seealso::

    - http://en.wikipedia.org/wiki/Bash
    - http://en.wikipedia.org/wiki/Command-line_interface (CLI)


Commands Line Interface
=======================

.. seealso:: http://www.commandlinefu.com


Research of text inside files
-----------------------------

.. code-block:: bash

    find . -name "*.c" -exec grep -iHA5 -B5 "ioutil.h" {} \;


Renaming files
--------------

.. code-block:: bash

    rename .c .cpp *.c



















