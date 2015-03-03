
.. index::
   pair: Async ; Tulip


.. _async_tulipe_30_10_2012:

================================================================
[Python-ideas] Async API: some more code to review (Steve Dower)
================================================================


.. seealso::

   - https://bitbucket.org/stevedower/wattle/src
   - https://bitbucket.org/stevedower/wattle/wiki/Proposal

.. contents::
   :depth: 3


Message from Steve Dower
========================


::

    Steve Dower Steve.Dower@microsoft.com via python.org
    à:   "python-ideas@python.org" <python-ideas@python.org>
    date:    30 octobre 2012 02:40
    objet:   [Python-ideas] Async API: some more code to review


Introduction
============

To save people scrolling to get to the interesting parts, I'll lead with the
links: Detailed write-up: https://bitbucket.org/stevedower/tulip/wiki/Proposal


Source code: https://bitbucket.org/stevedower/tulip/src


(Yes, I renamed my repo after the code name was selected. That would have been
far too much of a coincidence.)

Practically all of the details are in the write-up linked first, so anything
that's not is either something I didn't think of or something I decided is
unimportant right now (for example, the optimal way to wait for ten thousand
sockets simultaneously on every different platform).

There's a reimplemented Future class in the code which is not essential, but it
is drastically simplified from concurrent.futures.Future (CFF).

It can't be directly replaced by CFF, but only because CFF requires more state
management that the rest of the implementation does not perform ("set_running_or_notify_cancel").

CFF also includes cancellation, for which I've proposed a different mechanism.



For the sake of a quick example, I've modified Guido's main.doit function
(http://code.google.com/p/tulip/source/browse/main.py) to how it could be written
with my proposal (apologies if I've butchered it, but I think it should behave
the same).

::


    > On Monday, October 29, 2012, Steve Dower wrote:
    >
    >> Possibly I should have selected a different code name,
    >> now I come to think of it, but we came up with such
    >> similar code that I don't think it'll stay separate for too long.
    >
    > Hm, yes, this felt weird. I figured the code names would be
    > useful to reference the proposals when comparing them, not
    > as the ultimate eventual project name once it's beeb PEP-ified
    > and put in the stdlib.
    >
    > Maybe you can call yours "wattle"? That's a Pythonic plant name. :-)

Nice idea. I renamed it and (hopefully) made it so the original links still work.

https://bitbucket.org/stevedower/wattle/src
https://bitbucket.org/stevedower/wattle/wiki/Proposal

I was never expecting the name to last, I just figured you had to make something up to create a project. Eventually it will all just become a boring PEP-xxx number...

