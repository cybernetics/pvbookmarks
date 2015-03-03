
.. index::
   pair: hg ; rebase


=========
hg rebase
=========

.. seealso:: http://mercurial.selenic.com/wiki/RebaseProject


::

    -------- Message original --------
    Sujet:  Re: [Python-Dev] Hg: inter-branch workflow
    Date :  Sun, 20 Mar 2011 16:39:50 +0000
    De :    Georg Brandl <g.brandl@gmx.net>
    Pour :  python-dev@python.org


On 20.03.2011 16:21, Guido van Rossum wrote:
> What is "rebase"? Why does everyone want it and hate it at the same time?

Basically, rebase is a way to avoid having pointless merge commits on the
same branch.

Let's say you have the following history in your local repository::

    ... --- X --- A --- B

where X is the last commit that is in the remote repository, and
A and B are commits you made locally.  Now you pull from the remote,
and see that others have pushed more history in the meantime.  The
graph now looks this::

             A --- B
            /
    ... --- X --- C --- D --- E

To get your history pushed, you need to make a merge commit::

             A --- B ------------.
            /                     \
    ... --- X --- C --- D --- E --- M

Then you can push A, B and M to the remote.

Now, "hg pull --rebase" prevents that by "re-basing" the A-B history
line onto the latest remote head.  After rebasing, the history looks
like this::

    ... --- X --- C --- D --- E --- A' --- B'

without the need to merge before the push.

Obviously, if the merge above gave conflicts, the rebasing process
will also give conflicts.  In both cases you need to solve them
before continuing.

The reason why rebasing is not universally applied is that the
rebased changesets are different from the original ones (therefore
I wrote A' and B') -- even if the diff is the same, the parents
are not, and therefore the changeset id (hash) changes.  This is
called "changing history", and frowned upon by purists.  In reality
it works fine if you know the limits: rebasing really only should be
applied if the changesets are not already known somewhere else,
only in the local repo you're working with.

Georg


