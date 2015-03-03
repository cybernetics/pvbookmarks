
.. index::
   pair: language ; Go
   pair: language ; exceptions (no exceptions)
   ! Go

.. _go_language:

===================
Go language
===================



.. figure:: Golang.png
   :align: center
   

.. seealso::

   - http://golang.org/
   - https://twitter.com/golangweekly
   - http://www.golangweekly.com/
   - http://labix.org/gopkg.in


.. contents::
   :depth: 3

Introduction
=============

Go is an open source programming language that makes it easy to build simple, 
reliable, and efficient software. 

The ``Go`` programming language is an open source project to make programmers more
productive.

Go is expressive, concise, clean, and efficient.

**Its concurrency mechanisms** make it easy to write programs that get the most out
of multicore and networked machines, while its novel type system enables
flexible and modular program construction.

Go compiles quickly to machine code yet has the convenience of garbage
collection and the power of run-time reflection.

It's a fast, statically typed, compiled language that feels like a dynamically
typed, interpreted language.


No exceptions
=============

.. seealso::  http://golang.org/doc/go_faq.html#exceptions


We believe that coupling exceptions to a control structure, as in the
try-catch-finally idiom, results in convoluted code. It also tends to encourage
programmers to label too many ordinary errors, such as failing to open a file,
as exceptional.

Go takes a different approach.

For plain error handling, Go's multi-value returns make it easy to report an
error without overloading the return value. A canonical error type, coupled
with Go's other features, makes error handling pleasant but quite different
from that in other languages.

Go also has a couple of built-in functions to signal and recover from truly
exceptional conditions.

The recovery mechanism is executed only as part of a function's state being
torn down after an error, which is sufficient to handle catastrophe but
requires no extra control structures and, when used well, can result in clean
error-handling code.

See the Defer_, Panic_, and Recover_ article for details.


.. _Defer:  http://blog.golang.org/2010/08/defer-panic-and-recover.html
.. _Panic:  http://blog.golang.org/2010/08/defer-panic-and-recover.html
.. _Recover:  http://blog.golang.org/2010/08/defer-panic-and-recover.html



Source
------


::

    From: Thiago Cangussu <cangussu@gmail.com>
    Date: 2012/2/13
    Subject: Re: [zeromq-dev] What do I need to do to create a subproject of the libzmq?
    To: ZeroMQ development list <zeromq-dev@lists.zeromq.org>


> Show me at least one modern programming language that has no exceptions.


The Go language has no exceptions:

http://golang.org/doc/go_faq.html#exceptions



Projects using Go
==================


.. seealso::

   - :ref:`docker`
   
   


