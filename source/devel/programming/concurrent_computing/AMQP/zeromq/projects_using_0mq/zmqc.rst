
.. index::
   pair: zeromq; zmqc
   pair: projects using zeromq; zmqc
   pair: github projects; zmqc


.. _zmqc_zeromq:

===================
zmqc
===================


.. seealso::

   - http://pypi.python.org/pypi/zmqc/0.0.1
   - http://github.com/zacharyvoase/zmqc



zmqc is a small but powerful command-line interface to ØMQ.

It allows you to create a socket of a given type, bind or connect it to
multiple addresses, set options on it, and receive or send messages over it
using standard I/O, in the shell or in scripts.

It's useful for debugging and experimenting with most possible network topologies.

Examples
=========

::

    zmqc -rc SUB 'tcp://127.0.0.1:5000'

Subscribe to tcp://127.0.0.1:5000, reading messages from it and printing them
to the console. This will subscribe to all messages by default (you don't need
to set an empty SUBSCRIBE option). Alternatively:

::

    zmqc -rc SUB -o SUBSCRIBE='com.organization.' 'tcp://127.0.0.1:5000'


This will subscribe to all messages starting with com.organization..

::

    ls | zmqc -wb PUSH 'tcp://*:4000'


Send the name of every file in the current directory as a message from a PUSH
socket bound to port 4000 on all interfaces.

Don't forget to quote the address to avoid glob expansion.
