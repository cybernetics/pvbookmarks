
.. index::
   pair: 0MQ; zmq++
   pair: C++ ; 11
   pair: C++; zmq
   pair: Gestion des exceptions; Erreurs


.. _zmq++_library:

======================
C++11 zmq++ library
======================

.. seealso::

   - :ref:`cplusplus_11`
   - http://www.250bpm.com/blog:4


.. contents::
   :depth: 3


History
=======

::

    From: niXman <i.nixman@gmail.com>
    Date: 2012/2/13
    Subject: [zeromq-dev] What do I need to do to create a subproject of the libzmq?
    To: ZeroMQ development list <zeromq-dev@lists.zeromq.org>



Hello ØMQ dev-list !

I want to create a subproject of the ØMQ the main direction of which will be:

1. full implementation of the C++ API. not as cppzmq project, which is
   in fact a wraper over C API.
2. use of exceptions.
3. the use of opportunities of C++11 such as: r-value references and ``move`` semantic.
4. the use of C++11 Thread support library: http://en.cppreference.com/w/cpp/thread
5. implementation of IOCP.
6. implementation of asynchronous handlers.
7. implementation of memory-pool.

I'm going to call this project: zmq++


Why should I have written ZeroMQ in C, not C++
==============================================

.. seealso::

   - http://www.250bpm.com/blog:4


Just to be clear from the very beginning: This is not going to be a Torvalds-ish
rant against C++ from the point of view of die-hard C programmer.

I've been using C++ whole my professional career and it's still my language of
choice when doing most projects.

Naturally, when I started ZeroMQ project back in 2007, I've opted for C++.
The main reasons were:

- Library of data structures and algorithms (STL) is part of the language. With C
  I would have to either depend on a 3rd party library or had to write basic
  algorithms of my own in 1970's manner.
- C++ enforces some basic consistency in the coding style. For example, having
  the implicit 'this' parameter doesn't allow to pass pointer to the object
  being worked on using several disparate mechanisms as it often happens to be
  the case with C projects. Same applies to explicit marking of member variables
  as private and many other features of the language.
- This point is actually a subset of the previous one, but it's worth of explicit
  mention: Implementing virtual functions in C is pretty complex and tends to be
  slightly different for each class which makes understanding and managing the
  code a pain.
- And finally: Everybody loves destructors being invoked automatically at the
  end of the block.

Now, almost 5 years later, I would like to publicly admit that using C++ was a
poor choice and explain why I believe it is so.

First, it's important to take into account that ZeroMQ was intended to be a piece
of infrastructure with continuous uptime.

If should never fail and never exhibit undefined behaviour. Thus, the error
handling was of utmost importance. It had to be very explicit and unforgiving.

C++ exceptions just didn't fill the bill. They are great for guaranteeing that
program doesn't fail — just wrap the main function in try/catch block and you
can handle all the errors in a single place.

However, what's great for avoiding straightforward failures becomes a nightmare
when your goal is to guarantee that no undefined behaviour happens.

The decoupling between raising of the exception and handling it, that makes
avoiding failures so easy in C++, makes it virtually impossible to guarantee
that the program never runs info undefined behaviour.
