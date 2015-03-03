
.. index::
   pair: python people ; Steve Dower
   ! Steve Dower


.. _steve_dower:

=================
Steve Dower
=================


.. seealso::

   - http://stevedower.id.au/blog/about/
   - http://pytools.codeplex.com/
   - http://hg.python.org/sandbox/steve.dower


.. contents::
   :depth: 3

:Mail adress: Steve.Dower@microsoft.com


async/await in python
======================

.. seealso::

   - http://stevedower.id.au/blog/asyncawait-in-python/
   - http://stevedower.id.au/blog/async-api-for-python/


For the last week or two, an intense discussion has been occurring on the
python-ideas mailing list about asynchronous APIs, to which I’ve been
contributing/supporting an approach similar to async/await.

Since I wrote a 5000 word essay this week on the topic, I’m going to call that
my post.


October 2012 about async programming
====================================

::

    > I'm (and I think it's not just me) a bit lost here, after reading 100s of
    emails on python-ideas.  And I just want to know where to channel my energy
    and expertise ;)


It's not just you, I'm not entirely clear on what we expect to end up 
with either.

My current view is that we'll get a PEP that defines a convention for user code
and an interface for schedulers.

Adding _async() methods to the entire standard library could take a long time
and should probably be divided up so we can have really experienced devs on
particular areas (e.g. someone on Windows sockets, someone else on Linux sockets,
etc.) and may need individual PEPs.

My hope is that the first PEP provides a protocol for users to defer the rest of
a task until after some/any operation has completed -

I don't really want sockets/networking/files/threads/etc. to leak through at all,
though these are all important use cases that need to be tried.

This is the way I'm approaching it, so please let me know if I'm off the mark :)


Actions
========

.. toctree::
   :maxdepth: 3
   
   actions/actions
   
   
