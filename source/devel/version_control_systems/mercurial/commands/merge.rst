
.. index::
   hg rebase


=========
hg merge
=========

.. seealso:: http://stackoverflow.com/questions/5386868/mercurial-merge-two-branches-into-a-3rd-new-branch


Is it possible to, instead of merging one branch into another existing branch,
merge 2 branches into a 3rd new branch?



Just merge your 2 existing branches and consider the merge as the tip of the
3rd new branch and the previous heads of the merged branches as your 1st and 2nd branch:

::

    o    changeset:   3:92692c4a6b12
    |\   bookmark:    masala
    | |  summary:     merge salt and pepper
    | |
    | o  changeset:   2:a5f955adf03d
    | |  bookmark:    pepper
    | |  summary:     add some pepper
    | |
    o |  changeset:   1:2b56f2dc115f
    |/   bookmark:    salt
    |    summary:     add some salt
    |
    o  changeset:   0:e992ce7dd508
       summary:     initial


Here bookmarks have been used to mark different lines in development.
So if you want to work in the new 3rd branch, update to masala, if you want to
work on your 1st branch, update to salt, and similar for the 2nd branch update
to pepper before you continue to work and commit.

If you prefer working with named branches (instead of bookmarks), just issue a
hg branch masala before you commit the merge of revision 2 and 1.

The basic message is that although the graph only has one head, you are free to
interpret it as 3 different lines of development.

Now, let's say you want to continue the work in the 2nd branch, pepper::

    $ hg up pepper
    ... hack ...
    $ hg ci -m "need more pepper"

And then you have some ideas for the salt thing::

    $ hg up salt
    ... hack ...
    $ hg ci -m "less salt please"

Now the history graph shows your 3 branches more clearly::

    o  changeset:   5:d1f8eb72119a
    |  bookmark:    salt
    |  summary:     less salt please
    |
    | o  changeset:   4:acc9b01f584f
    | |  bookmark:    pepper
    | |  summary:     need more pepper
    | |
    +---o  changeset:   3:92692c4a6b12
    | |/   bookmark:    masala
    | |    summary:     merge salt and pepper
    | |
    | o  changeset:   2:a5f955adf03d
    | |  summary:     add some pepper
    | |
    o |  changeset:   1:2b56f2dc115f
    |/   summary:     add some salt
    |
    o  changeset:   0:e992ce7dd508
       summary:     initial


An alternative to bookmarks and named branches is to use different clones for
individual branches. That is you clone your repo with the unmerged branches and
merge them in the clone. Which approach is best, depends on your specific
workflow and personal preferences


::

    de  Éric Araujo <merwok@netwok.org>
    heure de l'expéditeur   Envoyé à 00:26 (GMT+01:00). Heure locale : 10:35. ✆
    à   Sjoerd Mullender <sjoerd@acm.org>
    cc  skip@pobox.com,
    python-dev@python.org
    date    23 mars 2011 00:26
    objet   Re: [Python-Dev] crosses branches?


Hi,

::

    >> I have to admit I don't know how to read this output or what I should look
    >> for in the way of conflicts.

Are these resources helpful?  (You don’t have to read them all, but if
the first doesn’t work, try the following one.)

About log:

- http://mercurial.selenic.com/wiki/TutorialHistory
- http://mercurial.selenic.com/wiki/GraphlogExtension
- http://mercurial.aragost.com/kick-start/en/basic/#inspecting-history


About merges, heads and parents:

- http://hginit.com/04.html
- http://mercurial.selenic.com/wiki/Merge
- http://mercurial.selenic.com/wiki/UnderstandingMercurial#Revisions.2C_changesets.2C_heads.2C_and_tip
- http://mercurial.selenic.com/wiki/MultipleHeads


To help us troubleshoot your issue, can you confirm this: you were in a
clone with the 2.5 branch checked out (“hg id” will tell that), you
pulled from 2.6, and the update action (from “pull -u”) failed.


::

    >> [...] I think that would make my local change unnecessary.

Correct.

::

    >> So, my next project is to try and figure out how to undo my change.

http://mercurial.selenic.com/wiki/PruningDeadBranches#Using_clone
If you follow that method, don’t forget to copy your .hg/hgrc to the new
clone.


::

    >> This seemed to work:


“Seemed” is the right word :(  More on
http://mercurial.selenic.com/wiki/Revert or “hg help revert”.

::

    > No.  Revert just reverts local (non-committed) changes.

This is untrue; Skip used a -r argument.  See above.
One thing to understand is that revert changes file contents only,
whereas update moved you on the revision graph.


Advanced commands like strip (bundled with mq BTW, not rebase) should
*not* be recommended lightly to people who are still learning the normal
use of Mercurial, IMO.  Throwing mentions of rebase, strip, transplant
can be harmful.  Let’s focus on clone, pull, update and merge first.
(That’s why the devguide tries to select one or two workflows; we know
that Mercurial is hella flexible, but choice is not a good thing when
you’re learning.)

Regards


::

    de  R. David Murray <rdmurray@bitdance.com>
    heure de l'expéditeur   Envoyé à 07:46 (GMT-04:00). Heure locale : 06:14. ✆
    à   Glenn Linderman <v+python@g.nevcal.com>
    cc  python-dev@python.org
    date    23 mars 2011 07:46



::

    > I don't recall 5-12 step sequences in the DVCS PEP when I read it once,
    > for any of the tools, but things progressed from the time I read it, so
    > maybe they would all have longer sequences.
    >
    > Back when I used non-distributed VCS systems like SCCS, RCS, PVCS, CVS,
    > and Clearcase, I don't recall any operations that took more than 2 or 3
    > commands to achieve (merges, of course, were onerous in some of those,
    > and locking sometimes stalled progress in some ways in some of those).


The 12 step cases are exactly merges, and the merges themselves are easy
with hg.

For simply getting a patch in to the default branch, svn had::

    svn up
    <apply patch etc>
    svn up
    svn ci


Whereas hg has::

    hg pull -u
    <apply patch etc>
    hg commit
    hg push


Same number of steps, but as has been pointed out, the hg push guarantees
no one else has made changes, whereas that safety-belt svn up before
the svn ci doesn't.

