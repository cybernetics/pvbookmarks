
.. index::
   pair: Mono; 3.0


.. _mono_3.0:

=============================
Mono 3.0 (October 18th 2012)
=============================


.. seealso::

   - http://www.mono-project.com/Release_Notes_Mono_3.0


.. contents::
   :depth: 3

Introduction
============

Mono 3.0 is a portable and open source implementation of the .NET framework for
Unix, Windows, MacOS and other operating systems.

Mono 3.0 is an update to Mono 2.10 based on the master branch of github, it is
not a minor upgrade to 2.10.

Mono 3.0 was released on October 18th 2012.

We will continue to bug fix and update Mono 2.10 for another six months for
users that can not upgrade to Mono 3.0

Major Highlights
================

C# Compiler
------------

.. seealso::

    - http://msdn.microsoft.com/en-us/vstudio/async.aspx


Mono now has a complete C# 5.0 compiler with `asynchronous programming support`_.

Our C# compiler has now completed its migration from using System.Reflection.Emit
as its code generation backend to use the IKVM.Reflection API.

This functionality was previewed in Mono 2.10 and is now the default.

With this functionality, developers can use any mscorlib that they want
(for example the MicroFramework one, or a custom one) without having to build a
custom compiler. We were able to eliminate the multiple executables for the
compiler, and unify all the compilers into one as well as reducing our build
times significantly.

.. _`asynchronous programming support`:  http://msdn.microsoft.com/en-us/vstudio/async.aspx


Mono.Data.Sqlite
----------------

It is now possible to configure the threading model for SQLite using the
SetConfig method in the SQLiteConnection class.

Supports iOS crypto APIs.

