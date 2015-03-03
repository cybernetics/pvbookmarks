

.. index::
   pair: C ; Czmq coding styles
   pair: C++ ; ZeroMQ coding styles

.. _czmq_coding_style:


===========
czmq manual
===========

.. seealso:: 

   - http://czmq.zeromq.org/manual:czmq



.. contents::
   :depth: 3

Design ideology The problem with C
==================================

C has the significant advantage of being a small language that, if we take a
little care with formatting and naming, can be easily interchanged between
developers.

Every C developer will use much the same 90% of the language.

Larger languages like C++ provide powerful abstractions like STL containers but
at the cost of interchange.

The huge problem with C is that any realistic application needs packages of
functionality to bring the language up to the levels we expect for the 21st
century.

Much can be done by using external libraries but every additional library is a
dependency that makes the resulting applications harder to build and port.
While C itself is a highly portable language (and can be made more so by careful
use of the preprocessor), most C libraries consider themselves part of the
operating system, and as such do not attempt to be portable.

The answer to this, as we learned from building enterprise-level C applications
at iMatix from 1995-2005, is to create our own fully portable, high-quality
libraries of pre-packaged functionality, in C. Doing this right solves both
the requirements of richness of the language, and of portability of the final
applications.


[zeromq-dev] C++ coding standard ?
===================================

::

    Tom Nakamura tnakamura@eml.cc
    répondre à:	 ZeroMQ development list <zeromq-dev@lists.zeromq.org>
    à:	 zeromq-dev@lists.zeromq.org
    date:	 4 mars 2014 06:09
    objet:	 [zeromq-dev] C++ coding standard?

Hello,

I've noticed that ZeroMQ, like most other large libraries written in
C++, chooses a specific subset of C++ and consistently adheres to it.

For example, I don't see a single throw/catch outside the tests/, most
classes have only 1 simple constructor and STL classes are used
sparingly.  

So:

Do the ZeroMQ developers have a coding standard/guideline for C++
development, akin to MISRA or Google's C++ Style Guide?

I know there is RFC 21 (CLASS) but that seems to be more about
aesthetics and high-level project architecture.  I ask because I want to
learn enough C++ so I can better understand ZeroMQ but don't want to
waste time learning stuff that the project does not use.  (I already
know C).

thank you,
Tom


::

    Pieter Hintjens ph@imatix.com
    répondre à:	 ZeroMQ development list <zeromq-dev@lists.zeromq.org>
    à:	 ZeroMQ development list <zeromq-dev@lists.zeromq.org>
    date:	 4 mars 2014 07:44
    objet:	 Re: [zeromq-dev] C++ coding standard ?
    
    

Hi Tom,

The original authors of the C++ code didn't write coding standards.
CLASS covers C, specifically (CZMQ, and related projects).

You might enjoy writing a coding standard for the libzmq C++ usage as
part of learning that subset.
