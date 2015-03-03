

.. index::
   pair: Python ; Git


.. _python_git:

==================================
cpython development with Git
==================================

.. seealso::

   - https://github.com/python/cpython


Introduction
============

Semi-official read-only mirror of the CPython Mercurial repository

Announce
=========

::

	Sujet: 	[Python-Dev] Semi-official read-only Github mirror of the CPython Mercurial repository
	Date : 	Mon, 30 Sep 2013 06:09:48 -0700
	De : 	Eli Bendersky <eliben@gmail.com>
	Pour : 	Python Dev <python-dev@python.org>


Hi all,

https://github.com/python/cpython is now live as a semi-official, *read only* 
Github mirror of the CPython Mercurial repository. 

Let me know if you have any problems/concerns.

I still haven't decided how often to update it (considering either just 
N times a day, or maybe use a Hg hook for batching). 
Suggestions are welcome.

The methodology I used to create it is via hg-fast-export. 

I also tried to pack and gc the git repo as much as possible before the 
initial Github push - it went down from almost ~2GB to ~200MB (so this 
is the size of a fresh clone right now).

Eli

P.S. thanks Jesse for the keys to https://github.com/python


::


	Sujet: 	Re: [Python-Dev] Semi-official read-only Github mirror of the CPython Mercurial repository
	Date : 	Mon, 30 Sep 2013 08:33:21 -0700
	De : 	Eli Bendersky <eliben@gmail.com>
	Pour : 	Skip Montanaro <skip@pobox.com>
	Copie à : 	Python Dev <python-dev@python.org>


On Mon, Sep 30, 2013 at 7:08 AM, Skip Montanaro <skip@pobox.com> wrote::

    > https://github.com/python/cpython is now live as a semi-official, *read
    > only* Github mirror of the CPython Mercurial repository. Let me know if you
    > have any problems/concerns.
    Thanks for this, Eli. I use git regularly at work, so I'm getting much
    more comfortable with it. Do you have a suggested workflow for people
    who might want to use Git in preference to Hg, but still have write
    access?


Petri Lehtinen runs a clone at https://github.com/akheron/cpython which 
uses more advanced tricks like hg-git and his own git-hg wrapper to allow 
him to do this, AFAIK. 

If this path is important for you, contact Petri and he can provide guidance 
on how to set it up.

For python/cpython I really wanted the simplest flow to reach a read-only 
stage, because I lack the necessary git/hg-fu to set up and maintain 
something more complex "semi-officially". 

I think the most common workflow is to do small changes vs. Mercurial anyway. 

When I'm working on longer-term patches I do them in my Git mirror (because 
I prefer Git branching) and then apply & test patches onto a Mercurial R/W 
clone before committing.

Thus, for most users I think the read-only mirror is preferable because 
it's much easier to use and reason about. All writes go solely through 
Mercurial, so it's clear where the official source is :)

Eli





