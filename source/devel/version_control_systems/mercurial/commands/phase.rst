
.. index::
   pair: hg ; phase


.. _hg_phase:

=========
hg phase
=========

.. seealso::

   - http://mercurial.selenic.com/wiki/Phases#Introduction
   - http://mercurial.selenic.com/wiki/Phases#Available_Phases
   - http://mercurial.selenic.com/wiki/Phases#Phase_Movements
   - http://mercurial.selenic.com/wiki/Phases#Upgrade_Notes
   - http://mercurial.selenic.com/wiki/Phases#Publishing_Repository


.. contents::
   :depth: 3


Introduction
============


The phase concept improves safety of history rewriting and control over
changesets exchanged (read more). This phase concept aims to "just works" in a
transparent manner for any user (read more). It is part of Core and always
enabled in any new client but doesn't prevent older client to work on a
repository (read more). Advanced user may decides to handle phase manually
(read more).

Like bookmarks, phases are not stored in history and thus are not permanent and
leave no audit trail.

This concept is introduced in Mercurial 2.1


Introduction To Mercurial Phases (Part I)
=========================================


.. seealso::

   - http://www.logilab.org/blogentry/88203


Introduction To Mercurial Phases (Part II)
===========================================


.. seealso::

   - http://www.logilab.org/blogentry/88219


This is the second part of a series of posts about the new phases feature we
implemented for mercurial 2.1.

The first part talks about how phases will help mercurial users, this second
part explains how to control them.

Controlling automatic phase movement
------------------------------------

Sometimes it may be desirable to push and pull changesets in the draft phase to
share unfinished work. Below are some cases:

- pushing to continuous integration,
- pushing changesets for review,
- user has multiple machines,
- branch clone.

You can disable publishing behavior in a repository configuration file::

    [phases]
    publish=False


Introduction To Mercurial Phases (Part III)
===========================================

.. seealso::

   - http://www.logilab.org/blogentry/88259

This is the final part of a series of posts about the new phases feature we
implemented for mercurial 2.1.

The first part talks about how phases will help mercurial users, the second part
explains how to control them.

This one explains what people should take care of when upgrading.


Conclusion
==========

Mercurial's phases are a simple concept that adds always on and transparent
safety for most users while not preventing advanced ones from doing whatever
they want.

Behind this safety-enabling and useful feature, phases introduce in Mercurial
code the concept of sharing mutable parts of history.

The introduction of this feature paves the way for advanced history rewriting
solutions while allowing safe and easy sharing of mutable parts of history.

I'll post about those future features shortly.




