
.. index::
   pair: zeromq; pyscale
   pair: projects using zeromq; pyscale
   pair: github projects; pyscale


.. _pyscale_zeromq:

===================
pyscale
===================


.. seealso::

   - http://pypi.python.org/pypi/pyscale/0.1.1
   - https://github.com/alexcepoi/pyscale



General purpose Python framework for writing highly scalable applications.

About
======

A typical application consists of several modules. Each module has its own
process, stores a pidfile in 'tmp/pids', and has a logfile in 'logs'.

A RPC protocol is implemented on top of zeromq in order to allow for inter-module
communication.

Modules have an auto-adjustable number of workers in order to cope with a high
number of requests.

These rpc requests will block until that module becomes available.

Read more about zeromq at http://zguide.zeromq.org/

Each module consists of several gevent greenlets. A basic module will already
contain a few greenlets that handle incoming rpc requests.

You can spawn additional greenlets for your own needs.
Read more about gevent at http://www.gevent.org/
