
.. index::
   pair: AMQP; 0MQ
   pair: AMQP; zeromq
   ! ZeroMQ
   ! 0MQ


.. _zeromq:

===================
The ZeroMQ library
===================

.. seealso::

   - http://www.zeromq.org/
   - http://twitter.com/#!/hintjens
   - http://zguide.zeromq.org/
   - http://www.zeromq.org/docs:labs
   - http://en.wikipedia.org/wiki/ZeroMQ
   - http://lwn.net/Articles/370307/
   - http://www.coastrd.com/zeromq-messaging
   - http://nichol.as/zeromq-an-introduction


.. contents::
   :depth: 3


Introduction
============


Some of us start by saying all the wonderful things it does.:

- It's sockets on steroids.
- It's like mailboxes with routing.
- It's fast!

Others try to share their moment of enlightenment, that zap-pow-kaboom satori
paradigm-shift moment when it all became obvious. Things just become simpler.
Complexity goes away.
It opens the mind.

Others try to explain by comparison. It's smaller, simpler, but still looks
familiar. Personally, I like to remember why we made ØMQ at all, because that's
most likely where you, the reader, still are today.

Physics of software
===================

Programming is a science dressed up as art, because most of us don't understand
the physics of software, and it's rarely if ever taught.

The physics of software is not algorithms, data structures, languages and
abstractions. These are just tools we make, use, throw away.

The real physics of software is the physics of people.

Specifically, our limitations when it comes to complexity, and our desire to
work together to solve large problems in pieces.
This is the science of programming: make building blocks that people can
understand and use easily, and people will work together to solve the very
largest problems.

We live in a connected world, and modern software has to navigate this world.
So the building blocks for tomorrow's very largest solutions are connected and
massively parallel. It's not enough for code to be "strong and silent" any more.

Code has to talk to code.
Code has to be chatty, sociable, well-connected.
Code has to run like the human brain, trillions of individual neurons firing
off messages to each other, a massively parallel network with no central control,
no single point of failure, yet able to solve immensely difficult problems.

And it's no accident that the future of code looks like the human brain,
because the endpoints of every network are, at some level, human brains.
If you've done any work with threads, protocols, or networks, you'll realize this is pretty
much impossible. It's a dream. Even connecting a few programs across a few sockets is
plain nasty, when you start to handle real life situations. Trillions? The cost would be
unimaginable. Connecting computers is so difficult that software and services to do this is
a multi-billion dollar business.

So we live in a world where the wiring is years ahead of our ability to use it. We had a
software crisis in the 1980s, when people like Fred Brooks believed there was no "Silver
Bullet". Free and open source software solved that crisis, enabling us to share knowledge
efficiently. Today we face another software crisis, but it's one we don't talk about much.
Only the largest, richest firms can afford to create connected applications. There is a
cloud, but it's proprietary. Our data, our knowledge is disappearing from our personal
computers into clouds that we cannot access, cannot compete with. Who owns our social
networks? It is like the mainframe-PC revolution in reverse.


We can leave the political philosophy for another book. The point is that while the
Internet offers the potential of massively connected code, the reality is that this is out of
reach for most of us, and so, large interesting problems (in health, education, economics,
transport, and so on) remain unsolved because there is no way to connect the code, and
thus no way to connect the brains that could work together to solve these problems.
There have been many attempts to solve the challenge of connected software. There are
thousands of IETF specifications, each solving part of the puzzle. For application
developers, HTTP is perhaps the one solution to have have been simple enough to work,
but it arguably makes the problem worse, by encouraging developers and architects to
think in terms of big servers and thin, stupid clients.

So today people are still connecting applications using raw UDP and TCP, proprietary
protocols, HTTP, WebSockets. It remains painful, slow, hard to scale, and essentially
centralized. Distributed p2p architectures are mostly for play, not work. How many
applications use Skype or Bittorrent to exchange data?
Which brings us back to the science of programming. To fix the world, we needed to do
two things. One, to solve the general problem of "how to connect any code to any code,
anywhere". Two, to wrap that up in the simplest possible building blocks that people
could understand and use easily.

It sounds ridiculously simple. And maybe it is. That's kind of the whole point.

ØMQ (ZeroMQ, 0MQ, zmq) looks like an embeddable networking library but acts like
a concurrency framework. It gives you sockets that carry whole messages across
various transports like in-process, inter-process, TCP, and multicast.

You can connect sockets Nto-N with patterns like fanout, pub-sub, task
distribution, and request-reply. It's fast enough to be the fabric for clustered
products.

Its asynchronous I/O model gives you scalable multicore applications, built as
asynchronous message-processing tasks. It has a score of language APIs and runs
on most operating systems. ØMQ is from iMatix and is LGPL open source.

Some Assumptions
================

We assume you are using the latest stable release of ØMQ. We assume you are using a
Linux box or something similar. We assume you can read C code, more or less, that's the
default language for the examples. We assume that when we write constants like PUSH or
SUBSCRIBE you can imagine they are really called ZMQ_PUSH or ZMQ_SUBSCRIBE if the
programming language needs it


.. index::
   pair: Architecture ; zeromq

zeromq Architecture
===================

.. seealso:: http://www.aosabook.org/en/zeromq.html

ØMQ is a messaging system, or "message-oriented middleware", if you will.

It's used in environments as diverse as financial services, game development,
embedded systems, academic research and aerospace.

Links
=====

.. seealso:: http://lwn.net/Articles/370307/



Tutorials
===================

.. toctree::
   :maxdepth: 4

   tutorials/index

Versions
=========

.. toctree::
   :maxdepth: 4

   versions/index


Projects using 0mq
==================

.. toctree::
   :maxdepth: 4

   projects_using_0mq/index


Bindings
=========

.. toctree::
   :maxdepth: 4

   bindings/index


News
====

.. toctree::
   :maxdepth: 4

   news/index


Use cases
=========

.. toctree::
   :maxdepth: 4

   use_cases




