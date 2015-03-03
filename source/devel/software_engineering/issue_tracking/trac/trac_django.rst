

.. index::
   pair: Trac; Django



.. _trac_django:

===========
trac django
===========


.. seealso::

   - https://code.djangoproject.com/newticket



Email
=====


::


    de  Luke Plant <L.Plant.98@cantab.net>
    heure de l'expéditeur   Envoyé à 16:59 (UTC). Heure locale : 16:12. ✆
    à   Matt Mackall <mpm@selenic.com>
    cc  mercurial-devel@selenic.com
    date    15 mars 2011 16:59
    objet   Re: Roundup -> Trac
    liste de diffusion  <mercurial-devel.selenic.com> Filtrer les messages de cette liste de diffusion

Hi all,

I'm a newcomer to this list, but I thought I'd weigh in to say that I think Trac
is a pretty good option.

We've used it for Django since the beginning, and I haven't come across a serious
contender to replace it.


Painless upgrades
=================

Upgrade procedure is here: http://trac.edgewall.org/wiki/TracUpgrade

It does require a little bit more than 'easy_install -U', but I don't think that
is avoidable due to the need for database upgrades.

We upgraded Django's trac to 0.12 recently and the only issue I'm aware of is
that the 'updates' list has stopped sending out changesets, but I don't think
that is actually Trac related. I happen to use Trac for a personal wiki, and so
just tried the upgrade from 0.11 to 0.12 and it worked fine.

Reliable search
===============

Search has always worked pretty well for me.



Seamless mail gateway, Bulk operations on issues
================================================

Not out of the box, but one of the great things about Trac is that it does have
a large, active community of plugin writers:

http://trac-hacks.org/

The code is clean Python and it is pretty easy to write plugins yourself.
(I've written a couple of simple ones).

A quick search finds this for e-mail:

https://subtrac.sara.nl/oss/email2trac/wiki/Email2tracParse

And this was already mentioned for batch modifications:


http://trac-hacks.org/wiki/BatchModifyPlugin

We use this on Django's Trac.


Doesn't send an endless stream of tracebacks via email
======================================================

I've never had issues with Trac crashing.

You also mentioned query building - I find the search query builder with Trac
pretty powerful and friendly.

Example:

- http://goo.gl/RigdX

(For me that page also shows the 'Batch Modify' interface, which does everything
I would expect)

Trac is also very customisable in terms of what kind of things you want against
each bug - milestone, version, status, triage stage, resolution, bug type,
priority, severity, component - in general if any of these are not used they
disappear from the interface, and you can add other custom flags, as seen above
(like "Needs documentation").

Luke

--

Luke Plant || http://lukeplant.me.uk/
