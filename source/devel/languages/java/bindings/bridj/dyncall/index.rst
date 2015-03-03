

.. index::
   dyncall
   language binding (dyncal)

.. _dyncall:

==========
dyncall
==========

.. image:: dyncall_b.png

.. seealso::

   - http://dyncall.org/
   - http://ochafik.com/blog/?p=674


The dyncall library encapsulates architecture-, OS- and compiler-specific
function call semantics in a virtual "bind argument parameters from left to
right and then call" interface allowing programmers to call C functions in a
completely dynamic manner. In other words, instead of calling a function directly,
the dyncall library provides a mechanism to push the function parameters manually
and to issue the call afterwards.
This means, that a program can determine at runtime what function to call, and
what parameters to pass to it.
The library is written in C and assembly and provides a very simple C interface
to program against.

The library comes in very handy to power flexible message systems, dynamic
function call dispatch mechanisms, closure implementations, to bridge different
programming languages, or to simply wrap a "vararg" function.

When it comes to language bindings, the dyncall library provides a clean and
portable C interface to dynamically issue calls to foreign code using small call
kernels written in assembly. Instead of providing code for every bridged
function call, which unnecessarily results in code bloat, only a couple of
instructions are used to invoke every possible call.


Rough overview of platforms and features
=========================================

The dyncall library runs on many different platforms and operating systems
(including Windows, Linux, OpenBSD, FreeBSD, Darwin, DragonFlyBSD, NetBSD,
Plan9, iOS, Haiku, Nintendo DS, Playstation Portable, Solaris, etc.) and
processors (x86, x64, arm, mips, ppc32, etc.).

Most of the platforms' C-calling conventions are supported - including "vararg"
functions, as well es C++-"thiscalls" on some platforms, and the multitude of
calling conventions on Windows ("fastcall", "stdcall", etc.).
Most of C99's types are supported for setting up a call, however, structure
and union support is still missing (we are working on it, though).

Additionally, dyncall comes with dyncallback, a library for callback support
(missing on some platforms), and dynload, to facilitate portable dynamic library
symbol loading and access (only for platforms with dynamic library support).
