
.. index::
   pair: ZeroMQ; Circus


.. _circus_zeromq:

===================
circus
===================


.. seealso::

   - https://github.com/mozilla-services/circus
   - http://circus.readthedocs.org/en/latest/index.html


.. contents::
   :depth: 3

Introduction
============

Circus is a program that will let you run and watch multiple processes.

Circus can be driven through a command-line interface, or programmatically
through its APIs.

It shares some of the goals of Supervisord_, BluePill_ and Daemontools_.


.. _Supervisord:  http://supervisord.org/
.. _BluePill: https://github.com/arya/bluepill
.. _Daemontools: http://cr.yp.to/daemontools.html


Circus CLI
==========

.. seealso:: http://circus.readthedocs.org/en/latest/commands/#cli


For each command below, we provide a usage example with circusctl but also the
input / output zmq messages.

