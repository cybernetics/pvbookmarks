

.. index::
   pair: Async; Pulsar

.. _pulsar:

==========================
Pulsar
==========================


.. seealso::

   - http://pypi.python.org/pypi/pulsar
   - http://packages.python.org/pulsar/
   - https://github.com/quantmind/pulsar


.. contents::
   :depth: 3


Introduction
============

Event driven concurrent framework for python.

Tested in Windows and Linux, it requires python 2.6, 2.7, 3.2 or pypy.

With pulsar you can write asynchronous servers performing one or several
activities in different threads and/or processes.

Pulsar's goal is to provide an easy way to build scalable network programs.
In the "Hello world!" web server example above, many client connections can be
handled concurrently. Pulsar tells the operating system (through epoll or select)
that it should be notified when a new connection is made, and then it goes to sleep.

Pulsar uses the multiprocessing module from the standard python library and it
can be configured to run in multi-processing or multi-threading mode.

Kudos
======

Pulsar project started as a fork of gunicorn (from where the arbiter idea) and
has been developed using ideas from nodejs (api design), twisted (the deferred
implementation), tornado web server (the event-loop implementation), celery
(the task queue application) and many other open-source efforts.
