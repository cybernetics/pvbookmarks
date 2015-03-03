
.. index::
   pair: python people ; Yury Selivanov
   ! Steve Dower


.. _yury_selivanov:

=================
Yury Selivanov
=================

.. contents::
   :depth: 3

Contact
=======

:Mail adress: yselivanov.ml@gmail.com


October 2012 about async programming
====================================


Guido,

Thank you for such a detailed and deep response.  Lots of good thoughts
to digest.

One idea: the scope of the problem is enormously big.  It may take
months/years to synchronize all ideas and thoughts by just communicating
ideas over mail list without a concrete thing and subject to discuss.
How about you/we create a repository with a draft implementation of
scheduler/io loop/coroutines engine and we simply start tweaking an
discussing that particular design?  That way people will see where
to start the discussion, what's done, and some will even participate?
The goal is not to write a production-quality software, but rather to
have a common place to discuss/try things/benchmark etc.  I'm not sure,
but maybe places like bitbucket, where you can have a wiki, issues, and
the actual code is a better place, than a mail-list.

I also think that there's need to move concurrency-related discussions
to a separate mail-list, as everything else on python-ideas is lost
now.


::

    > class Socket:
    >     def sendall(self, payload):
    >         f = Future()
    >         IOLoop.sendall(payload, future=f)
    >         return f
    >
    > class SMTP:
    >     def send(self, s):
    >         ...
    >         # yield the returned future to the scheduler
    >         yield self.sock.sendall(s)
    >         ...
    >
    > # And later:
    > s = SMTP()
    > yield from s.send('spam')
    >
    > Is it (roughly) how you want it all to look like?  I.e. using 'yield' to
    > send a future/task to the scheduler, and 'yield from' to delegate?


Guido response
===============

I think that's the style that Steve Dower prefers. Greg Ewing would
rather see all public APIs use yield from, and reserve plain yield
exclusively as an implementation detail of the scheduler. In my own
experimental code I am using Greg's style and it is working out great.
My main reason for taking a hard stance on this is that it would
otherwise be too confusing for users -- should they use yield, yield
from, or a plain call? I'd like to tell them "if it blocks, use yield
from".
