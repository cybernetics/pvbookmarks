

.. index::
   pair: Async ; Node.js


.. _nodejs_async:

=============================
Nodejs
=============================

.. seealso::

   - http://nodejs.org/
   - http://en.wikipedia.org/wiki/Node.js
   - :ref:`nodejs`
     


.. figure:: logo_nodejs.png
   :align: center



.. contents::
   :depth: 3

Introduction
============

Node.js is a server side software system designed for writing scalable Internet
applications, notably web servers.

Programs are written on the server side in JavaScript, using event-driven,
**asynchronous** I/O to minimize overhead and maximize scalability


Details
=======

Node.js consists of Google's V8 JavaScript engine, libUV, and several built-in
libraries.

Node.js was created by Ryan Dahl starting in 2009, and its growth is sponsored
by Joyent, his employer.

Dahl's original goal was to create the ability to make web sites with push
capabilities as seen in web applications like Gmail. After trying solutions in
several other programming languages he chose JavaScript because of the lack of
an existing I/O API. This allowed him to define a convention of non-blocking,
event-driven I/O.

Similar environments written in other programming languages include Twisted for
Python, Perl Object Environment for Perl, libevent for C, Vert.x for Java and
EventMachine for Ruby.

Unlike most JavaScript programs, it is not executed in a web browser, but is
instead a server-side JavaScript application.

Node.js implements some CommonJS specifications.

**It provides a REPL environment for interactive testing**
