
.. index::
   pair: hg ; bookmark
   pair: bookmark; secret
   pair: bookmark; public

.. _hg_bookmark:

============
hg bookmark
============

.. seealso::

   - http://mercurial.selenic.com/wiki/Bookmarks


.. contents::
   :depth: 3


History
=======

**Since version 1.8 (d4ab9486e514) the bookmark command is part of core.**

The behaviour of the core bookmarks is different from the original Bookmarks
Extension.

For example the track.current option was removed and the behavior of
track.current=True is now the default behavior of bookmarks.

For more details please check the Bookmarks wiki page.

:Author: David Soria

Overview
========

Bookmarks are references to commits that are automatically updated when new
commits are made.

If you do hg bookmark feature the feature bookmark refers to the current
changeset. As you work and commit changes the bookmark will move forward with
every commit you do.

The bookmark will always point to the latest revision in your line of work.
Since bookmarks are automatically updated when committing to the changeset they
are pointing to, they are especially useful to keep track of different heads.

They can therefore be used for trying out new features or pulling changes that
have yet to be reviewed. Bookmarks can be used to access the commit whenever a
usual lookup is allowed (wherever a command takes -r revision, revision can be
a bookmark name), therefore you can merge and update bookmarks by their names.


Secret bookmark
===============

They do not exist yet, The suggestion is to have:

- local-bookmark: only exists in your repository and not exchanged.
- public-bookmark: are always exchanged on pull//push//clone (as non secret-changeset are)
