
.. index::
   pair: hg ; graft
   pair: vcs; cherry-picking
   pair: hg ; cherry-picking


.. hg_graft:

=========
hg graft
=========

.. versionadded:: 2.5
   hg graft

.. seealso::

   - http://www.selenic.com/mercurial/hg.1.html#graft


::

    hg graft [OPTION]... REVISION...



This command uses Mercurial's merge logic to copy individual changes from other
branches without merging branches in the history graph.

This is sometimes known as 'backporting' or 'cherry-picking'.

By default, graft will copy user, date, and description from the source changesets.

Changesets that are ancestors of the current revision, that have already been
grafted, or that are merges will be skipped.

If a graft merge results in conflicts, the graft process is interrupted so that
the current merge can be manually resolved. Once all conflicts are addressed,
the graft process can be continued with the -c/--continue option.

Note

The -c/--continue option does not reapply earlier options.

Examples
========

copy a single change to the stable branch and edit its description::

    hg update stable
    hg graft --edit 9393


graft a range of changesets with one exception, updating dates::

    hg graft -D "2085::2093 and not 2091"


continue a graft after resolving conflicts::

    hg graft -c


show the source of a grafted changeset::

    hg log --debug -r tip


Returns 0 on successful completion.
