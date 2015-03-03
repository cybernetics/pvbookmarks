
.. index::
   pair: Language; Topaz
   pair: Topaz; Ruby

.. _topaz:

======================
Topaz
======================

.. seealso::

   - https://github.com/topazproject/topaz
   - http://topaz.readthedocs.org/en/latest/

.. contents::
   :depth: 3


Announce
========

.. seealso::

   - http://docs.topazruby.com/en/latest/blog/announcing-topaz/

I’m extraordinarily pleased to today announce Topaz, a project I started
10 months ago, to create a brand new implementation of the Ruby programming
language (version 1.9.3).

Topaz is written in Python on top of the RPython translation toolchain (the same
one that powers PyPy). Its primary goals are simplicity and performance.

Because Topaz builds on RPython, and thus much of the fantastic work of the
PyPy developers, it comes out of the box with a high performance garbage collector,
and a state of the art JIT (just-in-time) compiler.

**What does this mean? Out of the box Topaz is extremely fast.**

Topaz is far from complete and is missing many builtin methods and classes.

However, it does have nearly every element of Ruby, including classes, blocks,
many builtin types, all sorts of method calls, and much much more.

We don’t yet consider it stable, but it’s getting closer every day.

Introduction
=============


Topaz is a high performance implementation of the Ruby programming language,
written in Python on top of RPython (the toolchain that powers PyPy).
