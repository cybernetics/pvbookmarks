.. module:: MinGW
    :synopsis: MinGW ou Mingw32 (Minimalist GNU for Windows) and msys


.. index::
    ! MinGW
    pair: Minimalist GNU for Windows (MinGW); Windows



.. _mingw:

==================================
Minimalist GNU for Windows (MinGW)
==================================

.. seealso::

   - http://www.mingw.org


.. figure:: Official_gnu.png

   *GNU*


.. contents::
   :depth: 2



Introduction
============


MinGW (Minimalist GNU for Windows), formerly mingw32, is a native software port
of the GNU Compiler Collection (GCC) to Microsoft Windows, along with a set of
freely distributable import libraries and header files for the Windows API.

MinGW allows developers to create native Microsoft Windows applications [1]_.

Included in MinGW are extensions to the Microsoft Visual C++ runtime library to
support C99 functionality [1]_.


.. note::

    MinGW forked from version 1.3.3 of Cygwin. Although both Cygwin and MinGW can be used to port Unix software
    to Windows, they have different approaches: Cygwin aims to provide a complete POSIX layer (similar to that
    found in a Linux or other Unix systems) on top of Windows, sacrificing performance where necessary for
    compatibility. Accordingly, this approach requires Win32 programs written with Cygwin to run on top of a
    copylefted compatibility library that must be distributed with the program, along with the program's source code.

    MinGW aims to provide native functionality and performance via direct Windows API calls.

.. warning::

    Unlike Cygwin, MinGW does not require a compatibility layer DLL and thus programs do not need to be distributed with source code.


.. [1]  http://sourceforge.net/projects/mingw/


.. seealso::

   - http://www.mingw.org/wiki/MSVC_and_MinGW_DLLs
   - http://sourceforge.net/projects/mingw/files/



Minimal GNU for Windows (MinGW) License
=======================================


::

    Minimal GNU for Windows
    Version 5.1.6
    http://www.mingw.org/

    License, Use and Redistribution

    MinGW contains several different packages.  Some of those packages are
    licensed by the GNU Public License (GPL), some are licensed in the Public
    Domain and some have their own versions of a license.

    You may use MinGW on any number of systems.  There is no restriction to
    your use.  You may use MinGW commercially as well as privately.
    You the user assume the responsibility for the use of the files, binary or
    text, and there is no guarantee or warranty, expressed or implied, including
    but not limited to the implied warranties of merchantability and fitness
    for a particular purpose.   You assume all responsibility and agree to hold
    no entity, copyright holder or distributors liable for any loss of data
    or inaccurate representations of data as a result of using MinGW.

    You may redistribute MinGW in part or in whole as long as you follow the
    guidelines of redistribution of each license contained within.  To be
    certain that you are being legally compliant, always distribute the source.
    Distribution of source is your responsibility should you decide to redistribute
    MinGW.  If you distribute MinGW via a web site then you must put a copy of
    the source for that version of MinGW on your web site as well.
    If you distribute MinGW via removable media then you must distribute
    that version of MinGW source with that same type of removable media.

    Binaries created from the use of MinGW and of MSYS are not bound by
    any license found within this package unless you use a library that
    is itself covered by the GPL license.  If you wish to create
    proprietary software then don't use libiberty.a or any other
    GPL licensed library.  A library licensed with LGPL (Lesser GPL) may
    be used by proprietary software without GPL infection as special permission
    within the LGPL has given you this right.
    Please read and reread the COPYING and COPYING.LIB found in the <prefix>/doc/mingw directory.

    Earnie.
    Earnie@users.sf.net



.. _minGW_for_netbeans:

MinGW for netbeans
==================

MinGW tools in :ref:`netbeans <netbeans_ide>`.


Building an application (.exe)
------------------------------



Last MinGW version used
=======================

February 8th 2010
-----------------

+-----------------+----------------------------------+------------------------------------------+---------------+
|     Fichier     |               MD5                |                   SHA1                   | Size in bytes |
+=================+==================================+==========================================+===============+
| MinGW-5.1.6.exe | 9cf4ab0b4c9f858d32f5d5c89009c4dc | b399983b03115c9f9e8121dd212799fc6c1544c7 |     158842    |
+-----------------+----------------------------------+------------------------------------------+---------------+


.. seealso::

   - :ref:`gcc`
   - :ref:`windres`










