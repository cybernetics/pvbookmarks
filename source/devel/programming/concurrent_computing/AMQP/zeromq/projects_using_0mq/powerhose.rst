
.. index::
   pair: zeromq; powerhose
   pair: projects using zeromq; powerhose
   pair: github projects; powerhose


.. _powerhose_zeromq:

===================
Powerhose
===================


.. seealso::

   - https://github.com/mozilla-services/powerhose
   - http://tarekziade.wordpress.com/2012/02/06/scaling-crypto-work-in-python/


scaling-crypto-work-in-python
=============================

.. seealso::

   - http://tarekziade.wordpress.com/2012/02/06/scaling-crypto-work-in-python/

It turns out zeromq is perfect for this job – there are clients in Python and
C++, and defining a protocol to exchange data from the Python web server to the
crypto workers is quite simple.

In fact, this can be done as a reusable library that takes care of passing
messages to workers and getting back results. It has been done hundreds of times,
there are many examples in the zmq website, but I have failed to find any Python
packaged library that would let me push some work to workers transparently,
via a simple execute() call — if you know one tell me!.

So I am building one since it’s quite short and simple –

The project is called PowerHose and is located here:

- https://github.com/mozilla-services/powerhose.


...


Here’s an example of using Powerhose:

- The Server – https://github.com/mozilla-services/powerhose/blob/master/examples/square_master.py
- The Python worker – https://github.com/mozilla-services/powerhose/blob/master/examples/square_worker.py
- The C++ worker (don’t look at the code :) – https://github.com/mozilla-services/powerhose/blob/master/examples/square_worker.cpp

For the Token server, we’ll have:

- A JobRunner in our Cornice application
- A C++ worker that uses Crypto++

The first benches look fantastic — probably faster that anything I’d have
implemented myself using plain sockets :)

**I’ll try to package Powerhose so other projects at Mozilla can use it.**

I am wondering if this could be useful to more people, since I failed to find
that kind of tool.

How do you scale your CPU-bound web apps ?
