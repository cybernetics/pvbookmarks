
.. index::
   pair: yield ; from


.. _async_tulipe_29_10_2012:

==================================================================================
[Python-ideas] Async API: some code to review (29 octobre 2012, Guido van Rossum)
==================================================================================


.. seealso::

   - http://code.google.com/p/tulip/source/browse/

.. contents::
   :depth: 3

::

    Guido van Rossum guido@python.org
    à:   Python-Ideas <python-ideas@python.org>
    date:    29 octobre 2012 00:52
    objet:   [Python-ideas] Async API: some code to review


Introduction
============

I am finally ready to show the code I worked on for the past two
weeks. This is definitely not ready for anything except as a quick
demo, but I learned enough while writing it to feel comfortable with
the PEP 380 paradigm.

I've set up a Hg repo on code.google.com, and I picked a codename:
tulip. View the code here:

- http://code.google.com/p/tulip/source/browse/

It runs on Linux and OSX; I have no easy access to Windows but I'd be
happy to take contributions.

Key files in the directory:

- main.py: the main program for testing, and a rough HTTP client
- sockets.py: transports for sockets and SSL, and a buffering layer
- scheduling.py: a Task class and related stuff; this is where the PEP
  380 scheduler is implemented
- polling.py: an event loop and basic polling implementations for:
  select(), poll(), epoll(), kqueue()

Other junk: .hgignore, Makefile, README, p3time.py (benchmark yield
from vs. plain functions), longlines.py (stupid style checker)

More detailed discussions per file follows; please read the code along
with my description (separately they may not make much sense):

polling.py
===========

.. seealso:: http://code.google.com/p/tulip/source/browse/polling.py

I found it remarkably easy to come up with polling implementations
using all those different system calls. I ended up mixing in the
pollster class with the event loop class, although I'm not sure that's
the best design -- perhaps it's better if the event loop just
references the pollster as a separate object.

The pollster has a very simple API: add_reader(fd, callback, args),
add_writer(<ditto>), remove_reader(fd), remove_writer(fd), and
poll(timeout) -> list of events. (fd means file descriptor.) There's
also pollable() which just checks if there are any fds registered. My
implementation requires fd to be an int, but that could easily be
extended to support other types of event sources. I'm not super happy
that I have parallel reader/writer APIs, but passing a separate
read/write flag didn't come out any more elegant, and I don't foresee
other operation types (though I may be wrong).

The event list started out as a tuple of (fd, flag, callback, args),
where flag is 'r' or 'w' (easily extensible); in practice neither the
fd nor the flag are used, and one of the last things I did was to wrap
callback and args into a simple object that allows cancelling the
callback; the add_*() methods return this object. (This could probably
use a little more abstraction.) Note that poll() doesn't call the
callbacks -- that's up to the event loop.

The event loop has two basic ways to register callbacks:
call_soon(callback, args) causes callback(args) to be called the
next time the event loop runs; call_later(delay, callback, args)
schedules a callback at some time (relative or absolute) in the
future. It also inherits add_reader() and add_writer() from the
pollster. Then there is run(), which runs the event loop until there's
nothing left to do (no readers, no writers, no soon or later
callbacks), and run_once(), which goes through the entire list of
event sources once. (I think the order in which I do this isn't quite
right but it works for now.)

Finally, there's a helper class (ThreadRunner) here which lets you run
something in a separate thread using the features of
concurrent.futures. It uses the "self-pipe trick" (Google it :-) to
ensure that the poll() call wakes up -- this is needed by
call_in_thread() at the next layer (scheduling.py). (There may be a
race condition here, but I think it can be fixed.)

Note that there are no yields (or yield froms) here; that's for the next layer:

scheduling.py
=============


.. seealso:: http://code.google.com/p/tulip/source/browse/scheduling.py

This is the scheduler for PEP-380 style coroutines. I started with a
Scheduler class and operations along the lines of Greg Ewing's design,
with a Scheduler instance as a global variable, but ended up ripping
it out in favor of a Task object that represents a single stack of
generators chained via yield-from. There is a Context object holding
the event loop and the current task in thread-local storage, so that
multiple threads can (and must) have independent event loops.

**Most user (and much library) code in this system should be written as
generators invoking other generators directly using yield from.**

However to run something as an independent task, you wrap the
generator call in a Task() constructor, possibly giving it a timeout,
and then calling its start() method. A Task also acts a little like a
future -- you can wait() for it, add done-callbacks, and it preserves
the return value of the generator call. This can be used to introduce
concurrency or to give something a separate timeout. (There are also
primitives to wait for the first N completed of a bunch of Tasks.)

To invoke a primitive I/O operation, you call the current task's
block() method and then immediately yield (similar to Greg Ewing's
approach). There are helpers block_r() and block_w() that arrange for
a task to block until a file descriptor is ready for reading/writing.
Examples of their use are in sockets.py.

There is also call_in_thread() which integrates with
polling.ThreadRunner to run a function in a separate thread and wait
for it. Also used in sockets.py.

In the docstrings I use the prefix "COROUTINE:" to indicate public
APIs that should be invoked using yield from.


sockets.py
==========

.. seealso:: http://code.google.com/p/tulip/source/browse/sockets.py

This implements some internet primitives using the APIs in
scheduling.py (including block_r() and block_w()). I call them
transports but they are different from transports Twisted; they are
closer to idealized sockets. SocketTransport wraps a plain socket,
offering recv() and send() methods that must be invoked using yield
from. SslTransport wraps an ssl socket (luckily in Python 2.6 and up,
stdlib ssl sockets have good async support!). Then there is a
BufferedReader class that implements more traditional read() and
readline() coroutines (i.e., to be invoked using yield from), the
latter handy for line-oriented transports. Finally there are some
functions for connecting sockets, the highest-level one
create_transport(). These use call_in_thread() to run
socket.getaddrinfo() in a thread (this provides IPv6 support).

I don't particularly care about the exact abstractions in this module;
they are convenient and I was surprised how easy it was to add SSL,
but still these mostly serve as somewhat realistic examples of how to
use scheduling.py. (Afterthought: I think the SocketTransport's recv()
and send() methods could be made more similar to SslTransport.)

More examples in the final file:


main.py
=======

.. seealso:: http://code.google.com/p/tulip/source/browse/main.py

There is a simplistic HTTP client here built on top of the
sockets.*Transport abstractions. And the main code exercises this by
spawning four tasks fetching a variety of URLs (more when you
uncomment a block of code) and waiting for their results. The code is
a bit of a mess because I used it as a place to try out various APIs.

Feedback
========

I'm most interested in feedback on the design of polling.py and
scheduling.py, and to a lesser extent on the design of sockets.py;

main.py is just an example of how this style works out in practice.

Sorry for the brain-dump style; I would like to write it all up
better, but at the same time waiting longer doesn't necessarily make
it better, so here it is, for all to see. (I also have a list of
problems I had to debug during the development and what I learned from
that; but that's too raw to post right now.)
