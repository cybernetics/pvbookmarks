

.. index::
   26 february 2011
   Python dev with mercurial

====================================================
python dev with mercurial announce, 26 february 2011
====================================================


Mercurial branches are not bazaar branches
==========================================

::

    Date: Sat, 26 Feb 2011 01:49:46 +0100
    Organization: Eric Conspiracy Secret Labs
    To: Barry Warsaw <barry@python.org>
    Cc: python-dev@python.org
    Subject: Re: [Python-Dev] Mercurial conversion repositories

Hi,


::

    Le 25/02/2011 20:43, Barry Warsaw a écrit :
    > > On Feb 25, 2011, at 06:40 PM, Adrian Buehlmann wrote:
    > > [snip]
    >> >> Note that each of these branch clones will initially have your local
    >> >> master repo as the default path [3,4]. If you'd like to have the default
    >> >> push/pull path to point to ssh://hg@hg.python.org/cpython instead, you'd
    >> >> want to edit the [paths] section in the .hg/hgrc file in each of the
    >> >> branch repos.

I plan on having one clone per branch but pushing and pulling from only
one repository, so I don’t need to edit hgrcs.

> > It does leave me with an empty 'master' directory that I basically won't
> > touch, though I suppose I could hide it in a dot-filename.
Or have the master clone do double duty as the py3k clone.  (IOW, I have
2.7 3.1 3.2 py3k, I pull/push in py3k and also do merges and new
features in py3k).

::

    > > And I have to remember to fiddle with .hg/hgrc when I clone a new branch
    > > working directory, but I guess that's mostly a one-time cost.


You don’t, see above.  I’ve wanted to tell you something for a long
time: Mercurial branches are not at all like Bazaar branches.

See:

- http://mercurial.selenic.com/wiki/Branch and
- http://stevelosh.com/blog/2009/08/a-guide-to-branching-in-mercurial/

Anecdote: I migrated from Subversion to Mercurial a few years ago, and
found Mercurial branches very intuitive.  When I saw mentions of Bazaar
branches I was driven nuts by (what I saw as) the conflation between a
branch and a clone.  Later I understood how it made sense from the
perspective of Bazaar, so I shifted my judgment from “insanely
confusing” to “a particular choice that I don’t approve” <wink>.

Bazaar terminilogy does not map as-is to mercurial
==================================================

What I’m saying is that a lot of Bazaar terminology using “branch” does
not map as-is to Mercurial.  We clone a repo, we pull from a repo/clone,
we have named branches (e.g. 3.2) in a repo, we have unnamed branches on
one named branch.  I think you know that already, since you went from
using Bazaar terms applied to Mercurial to mixing terms from both
(“clone a new branch working directory” → “clone a repo”, probably).  I
salute your willingness to learn Mercurial, considering how fluent (and
fluffly) you appear to be with Bazaar.

::

    > > I'll have to remember that 'hg pull' does not update the working copy by
    > > default,


That pull does not update is a feature: The operation between a remote
repo and the local repo (the .hg directory) is separate from the
operation from the local repo to the working directory.  When you know
that you want pull + update (like when you have a clean working
directory), you use “hg pull -u”.  (I don’t like the fetch command.)


.. index::
   mercurial resources

Some mercurial resources
========================

::

    >> and eventually I'll figure out the whole merge thing.


Without anything specific, I’ll point to some resources:

Short tuto
----------

http://hginit.com/04.html

Concepts and examples
---------------------

- http://mercurial.selenic.com/wiki/Merge


Longer narratives
-----------------

http://hgbook.red-bean.com/read/a-tour-of-mercurial-merging-work.html
http://hgbook.red-bean.com/read/managing-releases-and-branchy-development.html


.. index::
   hgeditor
   CrecordExtension (mercurial)


Commit messages
===============

::
    > > One immediate thing that I'm missing from Bazaar is that 'bzr commit' invokes
    > > my editor and always shows me a 'diff -u' in the commit message buffer.  This
    > > is incredibly handy because I don't have to remember to do the diff in a
    > > different window, and I always have all the information I want right there to
    > > craft the commit message.


You speak to my heart, sir.  In your ~/.hgrc, under the section [ui],
set “editor = path/to/mercurial/source/hgeditor” and enjoy your diffs.

I use it and love it.

If you want to commit a subset of your local changes, I use
http://mercurial.selenic.com/wiki/CrecordExtension , a curses-based diff
selection UI that works like a charm.

Kind regards,
your friendly Mercurial whippersnapper


Response from Barry Warsaw (to Eric Araujo)
===========================================


::
    > >Le 25/02/2011 20:43, Barry Warsaw a écrit :
    >> >> On Feb 25, 2011, at 06:40 PM, Adrian Buehlmann wrote:
    >> >> [snip]
    >>> >>> Note that each of these branch clones will initially have your local
    >>> >>> master repo as the default path [3,4]. If you'd like to have the default
    >>> >>> push/pull path to point to ssh://hg@hg.python.org/cpython instead, you'd
    >>> >>> want to edit the [paths] section in the .hg/hgrc file in each of the
    >>> >>> branch repos.
    > >
    > >I plan on having one clone per branch but pushing and pulling from only
    > >one repository, so I don’t need to edit hgrcs.


So let's start from the basics.  I want separate working directories for each
active line-of-development (I'll use that term instead of "branch"),
e.g. working directories containing the tip of the 2.6 LoD, 2.7, 3.1, 3.2, and
3.3.  I will not be doing feature or bug development in any of these
directories.  They are purely for local tracking of the remote masters.  Thus,
I want to be able to synchronize any one of those LoDs against the remote
master with one command, like I would using Subversion's 'svn up'.

I clone the remote repository using the command in the devguide, so I now have
a 'cpython' directory containing the history of all LoDs, but with a working
directory that reflects the 'default' LoD.  Now, in the parent of 'cpython', I
do the following to get my separate-directory-LoDs:

$ hg clone -u 2.6 cpython py26
$ hg clone -u 2.7 cpython py27
# repeat and rinse for all other active LoDs

(Aside: that cpython directory still bugs me.  It doesn't naturally reflect a
LoD, so why do I have to stare at it?  Yes, I can make it play double duty by
naming it "3.3" or whatever and updating it to the 3.3 LoD, but that feels
artificial.)

Now I want to synchronize my local py27 directory with the state of that LoD
on python.org.  This is a two step process::

    $ cd py27 # now I want to synchronize
    $ (cd ../cpython && hg pull)
    $ hg pull -u

Editing hgrc to point to hg.python.org means the sync-to-remote-master
operation is one command.

I could do this::

    $ cd py27 # now I want to synchronize
    $ hg pull -u ssh://hg@hg.python.org/cpython

but I'm not going to remember that url every time.  It wouldn't be so bad if
Mercurial remembered the pull URL for me, as (you guessed it :) Bazaar does.

::

    > >Anecdote: I migrated from Subversion to Mercurial a few years ago, and
    > >found Mercurial branches very intuitive.  When I saw mentions of Bazaar
    > >branches I was driven nuts by (what I saw as) the conflation between a
    > >branch and a clone.  Later I understood how it made sense from the
    > >perspective of Bazaar, so I shifted my judgment from “insanely
    > >confusing” to “a particular choice that I don’t approve” <wink>.


That's funny because to my eyes, Mercurial conflates "branches" and "clones".
Why a clone operation should give me the history for all lines-of-development
inside a working directory for one "arbitrary" one strikes me as bizarre
(pardon the pun :).  I get that for folks who like the "svn switch" method of
working on multiple LoDs, this probably makes a lot of sense.  I don't
personally like or trust that approach much though.

::

    > >What I’m saying is that a lot of Bazaar terminology using “branch” does
    > >not map as-is to Mercurial.  We clone a repo, we pull from a repo/clone,
    > >we have named branches (e.g. 3.2) in a repo, we have unnamed branches on
    > >one named branch.  I think you know that already, since you went from
    > >using Bazaar terms applied to Mercurial to mixing terms from both
    > >(“clone a new branch working directory” → “clone a repo”, probably).  I
    > >salute your willingness to learn Mercurial, considering how fluent (and
    > >fluffly) you appear to be with Bazaar.


This is an inevitable problem with trying to converse fluently about three
major dVCSs and at least one or two other non-dVCSs.  They all use the same
words to mean vaguely similar things, but quickly get bogged down in the
implementation details assigned to those words.  It all makes perfect sense
when you've been immersed in those technologies, but it makes discussions and
comparisons exceedingly difficult.  I've no doubt it's doubly painful to many
people who have no prior experience with a dVCS.

(Aside: Bazaar could have potentially eased these folks transition because you
can use Bazaar just like you would Subversion - as a centralized VCS --
without stopping others from using it with full dVCS features on the same code
base.  I don't know if Mercurial offers the same flexibility.)

It's a little like trying to teach Python to a Java programmer.  "Object",
"Class", "Instance", "Import" all mean roughly similar things, which lulls you
into a false sense of understanding.  We learn by holding up the new to the
light of the familiar and looking for interference patterns. :)

::

    >> >> I'll have to remember that 'hg pull' does not update the working copy by
    >> >> default,
    > >
    > >That pull does not update is a feature: The operation between a remote
    > >repo and the local repo (the .hg directory) is separate from the
    > >operation from the local repo to the working directory.  When you know
    > >that you want pull + update (like when you have a clean working
    > >directory), you use “hg pull -u”.  (I don’t like the fetch command.)

Sure, I get that.  Again, this feature appears odd because I have the full
history of all LoDs embedded in a working directory of a single LoD.  With the
arrangement I outlined above (which is independent of the dVCS backing it), it
makes no sense for each LoD working directory to contain all the history of
all the other LoDs.

In Bazaar, a "branch" is an independent LoD and it's "repository" contains
only its own history.  Sure, it might have identical history with other LoDs
up to the point of divergence, and I have ways to efficiently share that
history across multiple LoD working directories, but they are still separate
and I don't need them if I don't care about them.  With Mercurial, all history
for all LoDs in a repository always come along for the ride.

::

    > >You speak to my heart, sir.  In your ~/.hgrc, under the section [ui],
    > >set “editor = path/to/mercurial/source/hgeditor” and enjoy your diffs.
    > >I use it and love it.


Great, I'll try that, thanks.  One thing Mercurial and Bazaar definitely share
is a wealth of magical awesomeness hidden in manpages, wiki pages, mailing
list posts, people's heads, configuration files, and source code. :)

::
    > >If you want to commit a subset of your local changes, I use
    > >http://mercurial.selenic.com/wiki/CrecordExtension , a curses-based diff
    > >selection UI that works like a charm.

I very rarely want to do that.  It's more common (but still, IME not *that*
common) to commit the changes to just a few files at a time.  One thing Bazaar
has that's very nice is the ability to "shelve" some changes for a time.
Let's say I'm working on a bug and I want to merge your changes in or sync to
the master.  I can shelve some or all of my uncommitted changes, which saves
them essentially out-of-the-way patch files, and then reverts my uncommitted
changes.  Unshelving then is the process of re-applying those patch files, and
yes, resolving conflicts.

This is also a great way to work when you want to do test-driven-development
but need to do some exploration first.  You can hack around non-TDD until
you're confident of your approach, shelve all your changes, then incrementally
apply them back as you write each test.  I'm sure Mercurial has something
equally awesome lurking about. :)

-Barry


Response from David Murray to Barry
===================================

::

    > > $ cd py27 # now I want to synchronize
    > > $ hg pull -u ssh://hg@hg.python.org/cpython
    > >
    > > but I'm not going to remember that url every time.  It wouldn't be so bad if
    > > Mercurial remembered the pull URL for me, as (you guessed it :) Bazaar does.


How does setting it in the hgrc differ from "remebering" it?  I've never
been comfortable with the bzr --remember option because I'm never
sure what it is remembering.  Much easier for me to see it in a config
file.  But, then, that's how my brain works, and other people's will
work differently.

::
    > > On Feb 26, 2011, at 01:49 AM, Ã‰ric Araujo wrote:
    >> > >Anecdote: I migrated from Subversion to Mercurial a few years ago, and
    >> > >found Mercurial branches very intuitive.  When I saw mentions of Bazaar
    >> > >branches I was driven nuts by (what I saw as) the conflation between a
    >> > >branch and a clone.  Later I understood how it made sense from the
    >> > >perspective of Bazaar, so I shifted my judgment from â€œinsanely
    >> > >confusingâ€ to â€œa particular choice that I donâ€™t approveâ€ <wink>.
    > >
    > > That's funny because to my eyes, Mercurial conflates "branches" and "clones".
    > > Why a clone operation should give me the history for all lines-of-development
    > > inside a working directory for one "arbitrary" one strikes me as bizarre
    > > (pardon the pun :).  I get that for folks who like the "svn switch" method of
    > > working on multiple LoDs, this probably makes a lot of sense.  I don't
    > > personally like or trust that approach much though.

I agree with you that I don't trust the 'svn switch' style.  I also find
it slow.  However....

::

    >> > >That pull does not update is a feature: The operation between a remote
    >> > >repo and the local repo (the .hg directory) is separate from the
    >> > >operation from the local repo to the working directory.  When you know
    >> > >that you want pull + update (like when you have a clean working
    >> > >directory), you use â€œhg pull -uâ€.  (I donâ€™t like the fetch command.)
    > >
    > > Sure, I get that.  Again, this feature appears odd because I have the full
    > > history of all LoDs embedded in a working directory of a single LoD.  With the
    > > arrangement I outlined above (which is independent of the dVCS backing it), it
    > > makes no sense for each LoD working directory to contain all the history of
    > > all the other LoDs.
    > >
    > > In Bazaar, a "branch" is an independent LoD and it's "repository" contains
    > > only its own history.  Sure, it might have identical history with other LoDs
    > > up to the point of divergence, and I have ways to efficiently share that
    > > history across multiple LoD working directories, but they are still separate
    > > and I don't need them if I don't care about them.  With Mercurial, all history
    > > for all LoDs in a repository always come along for the ride.

I find bazaar's model confusing, and hg's intuitive, just like Eric.
And consider that I learned bazaar before mercurial.  To me, it makes
perfect sense that in a DVCS the "unit" is a directory containing
a repository and a working copy, and that the repository is *the*
repository.  That is, it has everything related to the project in it,
just like the master SVN repository does (plus, since it is a DVCS,
whatever I've committed locally but not pushed to the master).  To have
a repository that only has some of the stuff in it is, IMO, confusing.
I advocated for having all the Python history in one repo partly for
that reason.

I can intellectually see your point about not really *needing* the stuff
for the LODs if you are only working on LOD X, but just like 'svn switch'
makes me uncomfortable, I'm just not *comfortable* not having the whole
repo in there :)

As an example, with mercurial, I feel comfortable moving directories
around and renaming them (with the help of google it took me about 1
minute to figure out how to keep the association between the repository
instances intact).  With bazaar I got in trouble trying to do that,
because the interrelationship between the working copy directories
(and their subsets of the repo?) and the master repo(?) was not clear.
I never did figure out how to make it work, I ended up starting over
with a new clone.

Now, as I get farther into learning mercurial I may well find things that
are just as confusing as I found that aspect of bazaar, but at least I
am comfortable with the outermost layer: the repo is the repo is the repo.


R. David Murray                                      www.bitdance.com



Branches and heads
==================

::

    Daniel Stutzbach <stutzbach@google.com> wrote:
    > > On Sat, Feb 26, 2011 at 9:55 AM, Antoine Pitrou <solipsis@pitrou.net> wrote:
    > >
    >> > > There is no such thing as an "unnamed branch". What would "hg branches"
    >> > > show? An empty space?
    > >
    > > I understand now why I was confused.  I had previously read the sentence
    > > "Both Git and Mercurial support unnamed local branches." at
    > > http://mercurial.selenic.com/wiki/BranchingExplained
    > >
    > > But as I dig deeper, I see that there is only one unnamed branch, and it
    > > actually does have an implicit name: "default".


Ok, so beware, the term "branch" can conflate two concepts:

- a path in the topology (or line of development)
- a "named branch" in hg terminology

So, actually, hg promotes a slightly different terminology:

- a "head" is a changeset without a child in the topology
- a "branch" usually means a "named branch": a set of changesets
  bearing the same label (e.g. "default"); that label is freely chosen
  by the committer at any point, and enforces no topological
  characteristic (even though in practice it will have, since it's the
  whole point from the user's perspective, and also because hg's
  default behaviour and concept of a "current branch" encourages it)

A (named) branch can have zero, one, or several heads:

- zero head: if all branch-local heads have a child in another named
  branch (for example, "trunk" is linearly followed by "2.7")
- several heads: if several lines of development were started in this
  branch without bothering to give them separate names

When you have several heads on a branch, you can merge them together if
you want to reconcile the lines of development they represent.

When you have several branches with at least one head each, you can
also merge them together: you must be careful to choose which named
branch the merge changeset will be part of (for example, if you want
to merge "3.1" into "3.2", you will certainly want the merge changeset
to be part of "3.2", otherwise "3.1" will get a lot of unwanted
features ;-)).

Note: a branch with zero head is marked "inactive" in "hg branches".
This basically means that it has already been merged in another branch.
(of course, you can still develop in that branch, which will certainly
create a new head as soon as you commit your first new changeset)

Regards

Antoine.


.. index::
   LOD (Line of Development)


Response from Brett Cannon to Barry
===================================

::

    From: Brett Cannon <brett@python.org>
    Date: Sat, 26 Feb 2011 12:09:58 -0800
    To: Barry Warsaw <barry@python.org>
    Cc: python-dev@python.org
    Subject: Re: [Python-Dev] Mercurial conversion repositories


::

    > > On Feb 26, 2011, at 01:49 AM, Éric Araujo wrote:
    > >
    >> > >Le 25/02/2011 20:43, Barry Warsaw a écrit :
    >>> > >> On Feb 25, 2011, at 06:40 PM, Adrian Buehlmann wrote:
    >>> > >> [snip]
    >>>> > >>> Note that each of these branch clones will initially have your local
    >>>> > >>> master repo as the default path [3,4]. If you'd like to have the
    > > default
    >>>> > >>> push/pull path to point to ssh://hg@hg.python.org/cpython instead,
    > > you'd
    >>>> > >>> want to edit the [paths] section in the .hg/hgrc file in each of the
    >>>> > >>> branch repos.
    >> > >
    >> > >I plan on having one clone per branch but pushing and pulling from only
    >> > >one repository, so I don’t need to edit hgrcs.
    > >
    > > So let's start from the basics.  I want separate working directories for
    > > each
    > > active line-of-development (I'll use that term instead of "branch"),
    > > e.g. working directories containing the tip of the 2.6 LoD, 2.7, 3.1, 3.2,
    > > and
    > > 3.3.  I will not be doing feature or bug development in any of these
    > > directories.  They are purely for local tracking of the remote masters.
    > >  Thus,
    > > I want to be able to synchronize any one of those LoDs against the remote
    > > master with one command, like I would using Subversion's 'svn up'.
    > >

For other people's benefit, LoD == line of development (I think).

::

    > >
    > > I clone the remote repository using the command in the devguide, so I now
    > > have
    > > a 'cpython' directory containing the history of all LoDs, but with a
    > > working
    > > directory that reflects the 'default' LoD.  Now, in the parent of
    > > 'cpython', I
    > > do the following to get my separate-directory-LoDs:
    > >
    > > $ hg clone -u 2.6 cpython py26
    > > $ hg clone -u 2.7 cpython py27
    > > # repeat and rinse for all other active LoDs
    > >
    > >

That's one way of doing it.

::

    > > (Aside: that cpython directory still bugs me.  It doesn't naturally reflect
    > > a
    > > LoD, so why do I have to stare at it?  Yes, I can make it play double duty
    > > by
    > > naming it "3.3" or whatever and updating it to the 3.3 LoD, but that feels
    > > artificial.)
    > >

It's a clone repository of CPython; the name makes perfect sense. You are
focusing on what the repository happens to be updated to ATM, not the fact
that the repository itself represents any and all LoDs.

::

    > >
    > > Now I want to synchronize my local py27 directory with the state of that
    > > LoD
    > > on python.org.  This is a two step process:
    > >
    > > $ cd py27 # now I want to synchronize
    > > $ (cd ../cpython && hg pull)
    > > $ hg pull -u
    > >
    > > Editing hgrc to point to hg.python.org means the sync-to-remote-master
    > > operation is one command.
    > >
    > > I could do this:
    > >
    > > $ cd py27 # now I want to synchronize
    > > $ hg pull -u ssh://hg@hg.python.org/cpython
    > >
    > > but I'm not going to remember that url every time.  It wouldn't be so bad
    > > if
    > > Mercurial remembered the pull URL for me, as (you guessed it :) Bazaar
    > > does.
    > >

So does Hg: simply edit your .hgrc to have it both pull and push to the same
URL.

Clone the repository at a specific branch
=========================================

Or you can save yourself some trouble, and simply clone the repository at a
specific branch::

    hg clone ssh://hg@hg.python.org/cpython#2.7


I believe that might even strip out other history outside the scope of the
branch.


::

    > >
    >> > >Anecdote: I migrated from Subversion to Mercurial a few years ago, and
    >> > >found Mercurial branches very intuitive.  When I saw mentions of Bazaar
    >> > >branches I was driven nuts by (what I saw as) the conflation between a
    >> > >branch and a clone.  Later I understood how it made sense from the
    >> > >perspective of Bazaar, so I shifted my judgment from “insanely
    >> > >confusing” to “a particular choice that I don’t approve” <wink>.
    > >
    > > That's funny because to my eyes, Mercurial conflates "branches" and
    > > "clones".
    > > Why a clone operation should give me the history for all
    > > lines-of-development
    > > inside a working directory for one "arbitrary" one strikes me as bizarre
    > > (pardon the pun :).

Because Hg views a clone as that: a clone of the entire repository.

A branch just happens to be a part of the repository.

And because it is the entire repository it has to have you point somewhere, so
it goes with default since a lot of people never even work somewhere other than
on default.


::

    > >  I get that for folks who like the "svn switch" method of
    > > working on multiple LoDs, this probably makes a lot of sense.  I don't
    > > personally like or trust that approach much though.
    > >

Neither do I in an svn context and why Hg does let you check out just a
branch and have all pulls and pushes only go to that branch.

::

    > >
    >> > >What I’m saying is that a lot of Bazaar terminology using “branch” does
    >> > >not map as-is to Mercurial.  We clone a repo, we pull from a repo/clone,
    >> > >we have named branches (e.g. 3.2) in a repo, we have unnamed branches on
    >> > >one named branch.  I think you know that already, since you went from
    >> > >using Bazaar terms applied to Mercurial to mixing terms from both
    >> > >(“clone a new branch working directory” → “clone a repo”, probably).  I
    >> > >salute your willingness to learn Mercurial, considering how fluent (and
    >> > >fluffly) you appear to be with Bazaar.
    > >
    > > This is an inevitable problem with trying to converse fluently about three
    > > major dVCSs and at least one or two other non-dVCSs.  They all use the same
    > > words to mean vaguely similar things, but quickly get bogged down in the
    > > implementation details assigned to those words.  It all makes perfect sense
    > > when you've been immersed in those technologies, but it makes discussions
    > > and
    > > comparisons exceedingly difficult.  I've no doubt it's doubly painful to
    > > many
    > > people who have no prior experience with a dVCS.
    > >
    > > (Aside: Bazaar could have potentially eased these folks transition because
    > > you
    > > can use Bazaar just like you would Subversion - as a centralized VCS --
    > > without stopping others from using it with full dVCS features on the same
    > > code
    > > base.  I don't know if Mercurial offers the same flexibility.)
    > >
    > > It's a little like trying to teach Python to a Java programmer.  "Object",
    > > "Class", "Instance", "Import" all mean roughly similar things, which lulls
    > > you
    > > into a false sense of understanding.  We learn by holding up the new to the
    > > light of the familiar and looking for interference patterns. :)
    > >

Yes, fun isn't it? Makes me that much more glad I don't have to care about
other DVCSs anymore; make the decision of which one to go through was
painful partially for this reason.


::

    > >
    >>> > >> I'll have to remember that 'hg pull' does not update the working copy by
    >>> > >> default,
    >> > >
    >> > >That pull does not update is a feature: The operation between a remote
    >> > >repo and the local repo (the .hg directory) is separate from the
    >> > >operation from the local repo to the working directory.  When you know
    >> > >that you want pull + update (like when you have a clean working
    >> > >directory), you use “hg pull -u”.  (I don’t like the fetch command.)
    > >
    > > Sure, I get that.  Again, this feature appears odd because I have the full
    > > history of all LoDs embedded in a working directory of a single LoD.

Not single, _current_. I know you don't like the whole svn switch approach
that this is like, but Hg is very much about "don't forget a thing", which
is why you need to view a clone as a clone repository that you are choosing
to view in a certain way at any moment in time instead of as a single branch
that just happens to be carrying around the weight of other branches.
Totally different approaches to VCS.


::

    > >  With the
    > > arrangement I outlined above (which is independent of the dVCS backing it),
    > > it
    > > makes no sense for each LoD working directory to contain all the history of
    > > all the other LoDs.
    > >

As I said above, use the #<branch> format and you skip this issue (I think).



.. index::
   hg mq extension


Hg mq extension
===============


::

    > >
    > > In Bazaar, a "branch" is an independent LoD and it's "repository" contains
    > > only its own history.  Sure, it might have identical history with other
    > > LoDs
    > > up to the point of divergence, and I have ways to efficiently share that
    > > history across multiple LoD working directories, but they are still
    > > separate
    > > and I don't need them if I don't care about them.  With Mercurial, all
    > > history
    > > for all LoDs in a repository always come along for the ride.
    > >
    >> > >You speak to my heart, sir.  In your ~/.hgrc, under the section [ui],
    >> > >set “editor = path/to/mercurial/source/hgeditor” and enjoy your diffs.
    >> > >I use it and love it.
    > >
    > > Great, I'll try that, thanks.  One thing Mercurial and Bazaar definitely
    > > share
    > > is a wealth of magical awesomeness hidden in manpages, wiki pages, mailing
    > > list posts, people's heads, configuration files, and source code. :)
    > >
    >> > >If you want to commit a subset of your local changes, I use
    >> > >http://mercurial.selenic.com/wiki/CrecordExtension , a curses-based diff
    >> > >selection UI that works like a charm.
    > >
    > > I very rarely want to do that.  It's more common (but still, IME not *that*
    > > common) to commit the changes to just a few files at a time.  One thing
    > > Bazaar
    > > has that's very nice is the ability to "shelve" some changes for a time.
    > > Let's say I'm working on a bug and I want to merge your changes in or sync
    > > to
    > > the master.  I can shelve some or all of my uncommitted changes, which
    > > saves
    > > them essentially out-of-the-way patch files, and then reverts my
    > > uncommitted
    > > changes.  Unshelving then is the process of re-applying those patch files,
    > > and
    > > yes, resolving conflicts.
    > >


Hg's is the mq (Mercurial Queue) extension.


::

    > >
    > > This is also a great way to work when you want to do
    > > test-driven-development
    > > but need to do some exploration first.  You can hack around non-TDD until
    > > you're confident of your approach, shelve all your changes, then
    > > incrementally
    > > apply them back as you write each test.  I'm sure Mercurial has something
    > > equally awesome lurking about. :)



They all have the same history from the Linux kernel for the patch queue
concept. I suspect it's pretty universally implemented, just with different
command names (of course as gods forbid it be consistent).


Response of Barry Warsaw to Eric Araujo
=======================================

::

    From: Barry Warsaw <barry@python.org>
    To: = Araujo <merwok@netwok.org>
    Mime-Version: 1.0
    Cc: python-dev@python.org
    Subject: Re: [Python-Dev] Mercurial conversion repositories


::

    > >You speak to my heart, sir.  In your ~/.hgrc, under the section [ui],
    > >set “editor = path/to/mercurial/source/hgeditor” and enjoy your diffs.
    > >I use it and love it.


Except it doesn't quite work the way I want it to (hg 1.6.3).  It opens your
editor with two files, one is the commit message and the other is the diff.
(The script itself is a bit buggy too. ;)

But it's a good clue, and I've modified the default hgeditor script to get
closer, and fix the bug I noticed.  I basically append the diff to the
temporary log message file.  It's still not right though because if the diff
lines aren't prepended with 'HG:', they end up in the commit message.  Arg.

Oh well, I can clearly hack a more complicated script together.  It's such a
blindingly obvious improvement, it's too bad 'hg commit' doesn't DTRT by
default.

-Barry


Response of Barry Warsaw to David Murray
========================================

::

    Date: Sat, 26 Feb 2011 16:06:45 -0500
    From: Barry Warsaw <barry@python.org>
    To: "R. David Murray" <rdmurray@bitdance.com>
    Cc: python-dev@python.org
    Subject: Re: [Python-Dev] Mercurial conversion repositories


::

    > >On Sat, 26 Feb 2011 13:08:47 -0500, Barry Warsaw <barry@python.org> wrote:
    >> >> $ cd py27 # now I want to synchronize
    >> >> $ hg pull -u ssh://hg@hg.python.org/cpython
    >> >>
    >> >> but I'm not going to remember that url every time.  It wouldn't be so bad if
    >> >> Mercurial remembered the pull URL for me, as (you guessed it :) Bazaar does.
    > >
    > >How does setting it in the hgrc differ from "remebering" it?


It's different because you don't use a familiar interface to set it (i.e hg).
You have to know to hack a file to make it work.

That's not awesome user interface. ;)


::

    > >I've never been comfortable with the bzr --remember option because I'm never
    > >sure what it is remembering.  Much easier for me to see it in a config file.
    > >But, then, that's how my brain works, and other people's will work
    > >differently.


It's easy to tell what it remembers because it's exactly what you told it to
remember ;).  But I guess you're talking about push and pull automatically
remembering the location when none was previously set.  I love that feature.

And of course, bzr 'remembers' by setting a value in a config file, which of
course you *could* hack if you wanted to.  It's just that you don't normally
have to open your editor and remember which value in which config file you
have to manually modify to set the push and pull locations.  I think that's a
win, but YMMV. :)

Oh, and 'bzr info' always tells you what the push and pull locations are.

::

    > >I find bazaar's model confusing, and hg's intuitive, just like Ã‰ric.
    > >And consider that I learned bazaar before mercurial.  To me, it makes
    > >perfect sense that in a DVCS the "unit" is a directory containing
    > >a repository and a working copy, and that the repository is *the*
    > >repository.  That is, it has everything related to the project in it,
    > >just like the master SVN repository does (plus, since it is a DVCS,
    > >whatever I've committed locally but not pushed to the master).  To have
    > >a repository that only has some of the stuff in it is, IMO, confusing.
    > >I advocated for having all the Python history in one repo partly for
    > >that reason.

I would feel better about Mercurial's if the repo where not intimately tied
with a default working tree (yes, I know -U).  In a sense, that's what
Bazaar's shared repositories are: a place where all your history goes.  In
Bazaar's model though, it's not tied to a specific working tree, and it's
hidden in a dot-directory.

It's still kind of beside the point - this is the way Mercurial works, and I
don't really mean this thread to be an in-depth comparison between the two.

-Barry


Response of Antoine Pitrou to Barry Warsaw
==========================================


Mercurial extensions
====================

.. seealso:: http://mercurial.selenic.com/wiki/ShareExtension


::

    > >
    >> > >I find bazaar's model confusing, and hg's intuitive, just like Ã‰ric.
    >> > >And consider that I learned bazaar before mercurial.  To me, it makes
    >> > >perfect sense that in a DVCS the "unit" is a directory containing
    >> > >a repository and a working copy, and that the repository is *the*
    >> > >repository.  That is, it has everything related to the project in it,
    >> > >just like the master SVN repository does (plus, since it is a DVCS,
    >> > >whatever I've committed locally but not pushed to the master).  To have
    >> > >a repository that only has some of the stuff in it is, IMO, confusing.
    >> > >I advocated for having all the Python history in one repo partly for
    >> > >that reason.
    > >
    > > I would feel better about Mercurial's if the repo where not intimately tied
    > > with a default working tree (yes, I know -U).  In a sense, that's what
    > > Bazaar's shared repositories are: a place where all your history goes.  In
    > > Bazaar's model though, it's not tied to a specific working tree, and it's
    > > hidden in a dot-directory.


Often (but not always), when you're wanting to do something, there's an
extension for Mercurial which can be enabled ;)
http://mercurial.selenic.com/wiki/ShareExtension

Regards

Antoine.

Response of Barry Warsaw to Brett Cannon
========================================

::

    > >For other people's benefit, LoD == line of development (I think).


Yes.  It's just a word that isn't intimately tied to the implementation
details of a specific dVCS.

::

    >> >> I clone the remote repository using the command in the devguide, so I now
    >> >> have
    >> >> a 'cpython' directory containing the history of all LoDs, but with a
    >> >> working
    >> >> directory that reflects the 'default' LoD.  Now, in the parent of
    >> >> 'cpython', I
    >> >> do the following to get my separate-directory-LoDs:
    >> >>
    >> >> $ hg clone -u 2.6 cpython py26
    >> >> $ hg clone -u 2.7 cpython py27
    >> >> # repeat and rinse for all other active LoDs
    >> >>
    >> >>
    > >That's one way of doing it.

I'm sure there are many different ways of setting things up.  I am totally in
favor of the devguide documenting and encouraging one particular way, and I'm
sure Mercurial will prove to be a flexible tool that can conform to user's
preferences rather than the other way 'round.

::

    >> >> (Aside: that cpython directory still bugs me.  It doesn't naturally reflect
    >> >> a
    >> >> LoD, so why do I have to stare at it?  Yes, I can make it play double duty
    >> >> by
    >> >> naming it "3.3" or whatever and updating it to the 3.3 LoD, but that feels
    >> >> artificial.)
    >> >>
    > >It's a clone repository of CPython; the name makes perfect sense. You are
    > >focusing on what the repository happens to be updated to ATM, not the fact
    > >that the repository itself represents any and all LoDs.

No, I get all that.  I'm just not sure why I should care where all the history
is stored.  I'm not actually going to do any coding in the cpython directory,
so it just seems like a wart I have to carry around.  But as I said before,
this is the Mercurial Way, so be it.

::

    >> >> Now I want to synchronize my local py27 directory with the state of that
    >> >> LoD
    >> >> on python.org.  This is a two step process:
    >> >>
    >> >> $ cd py27 # now I want to synchronize
    >> >> $ (cd ../cpython && hg pull)
    >> >> $ hg pull -u
    >> >>
    >> >> Editing hgrc to point to hg.python.org means the sync-to-remote-master
    >> >> operation is one command.
    >> >>
    >> >> I could do this:
    >> >>
    >> >> $ cd py27 # now I want to synchronize
    >> >> $ hg pull -u ssh://hg@hg.python.org/cpython
    >> >>
    >> >> but I'm not going to remember that url every time.  It wouldn't be so bad
    >> >> if
    >> >> Mercurial remembered the pull URL for me, as (you guessed it :) Bazaar
    >> >> does.
    >> >>
    > >
    > >So does Hg: simply edit your .hgrc to have it both pull and push to the same
    > >URL.

Right, see my follow up to RDM.


::

    > >Or you can save yourself some trouble, and simply clone the repository at a
    > >specific branch:
    > >
    > >  hg clone ssh://hg@hg.python.org/cpython#2.7
    > >
    > >I believe that might even strip out other history outside the scope of the
    > >branch.

That might be a better way if it doesn't slurp down the entire repository
history.

::

    >>> >> >Anecdote: I migrated from Subversion to Mercurial a few years ago, and
    >>> >> >found Mercurial branches very intuitive.  When I saw mentions of Bazaar
    >>> >> >branches I was driven nuts by (what I saw as) the conflation between a
    >>> >> >branch and a clone.  Later I understood how it made sense from the
    >>> >> >perspective of Bazaar, so I shifted my judgment from “insanely
    >>> >> >confusing” to “a particular choice that I don’t approve” <wink>.
    >> >>
    >> >> That's funny because to my eyes, Mercurial conflates "branches" and
    >> >> "clones".
    >> >> Why a clone operation should give me the history for all
    >> >> lines-of-development
    >> >> inside a working directory for one "arbitrary" one strikes me as bizarre
    >> >> (pardon the pun :).
    > >
    > >Because Hg views a clone as that: a clone of the entire repository. A branch
    > >just happens to be a part of the repository. And because it is the entire
    > >repository it has to have you point somewhere, so it goes with default since
    > >a lot of people never even work somewhere other than on default.


Yep, I get all that.  It's Mercurial's model of the world.

::

    > >Yes, fun isn't it? Makes me that much more glad I don't have to care about
    > >other DVCSs anymore; make the decision of which one to go through was
    > >painful partially for this reason.


Lucky you!  I interact with tons of projects, so I still have to deal with
everything from CVS to git.  This will be my first serious foray into hg, and
for that I'm glad.

And really, *any* dVCS is better than a non-dVCS, so I'm really happy this is
finally happening, despite any initial grumbling you're reading into my posts. :)

::

    >>>> >> >> I'll have to remember that 'hg pull' does not update the working copy by
    >>>> >> >> default,
    >>> >> >
    >>> >> >That pull does not update is a feature: The operation between a remote
    >>> >> >repo and the local repo (the .hg directory) is separate from the
    >>> >> >operation from the local repo to the working directory.  When you know
    >>> >> >that you want pull + update (like when you have a clean working
    >>> >> >directory), you use “hg pull -u”.  (I don’t like the fetch command.)
    >> >>
    >> >> Sure, I get that.  Again, this feature appears odd because I have the full
    >> >> history of all LoDs embedded in a working directory of a single LoD.
    > >
    > >Not single, _current_. I know you don't like the whole svn switch approach
    > >that this is like, but Hg is very much about "don't forget a thing", which
    > >is why you need to view a clone as a clone repository that you are choosing
    > >to view in a certain way at any moment in time instead of as a single branch
    > >that just happens to be carrying around the weight of other branches.
    > >Totally different approaches to VCS.


No really, I do get all that!  I just don't like it much.  Maybe it'll grow on
me though.


Mq, shelve, loom, pipeline extensions
=====================================


::

    >> >> I very rarely want to do that.  It's more common (but still, IME not *that*
    >> >> common) to commit the changes to just a few files at a time.  One thing
    >> >> Bazaar
    >> >> has that's very nice is the ability to "shelve" some changes for a time.
    >> >> Let's say I'm working on a bug and I want to merge your changes in or sync
    >> >> to
    >> >> the master.  I can shelve some or all of my uncommitted changes, which
    >> >> saves
    >> >> them essentially out-of-the-way patch files, and then reverts my
    >> >> uncommitted
    >> >> changes.  Unshelving then is the process of re-applying those patch files,
    >> >> and
    >> >> yes, resolving conflicts.
    >> >>
    > >
    > >Hg's is the mq (Mercurial Queue) extension.


I think mq is more like quilt than shelve.  The moral equivalents in Bazaar
would probably be the loom and pipeline extensions.


hg-git, bzr-hg
==============

::

    >> >> This is also a great way to work when you want to do
    >> >> test-driven-development
    >> >> but need to do some exploration first.  You can hack around non-TDD until
    >> >> you're confident of your approach, shelve all your changes, then
    >> >> incrementally
    >> >> apply them back as you write each test.  I'm sure Mercurial has something
    >> >> equally awesome lurking about. :)
    > >
    > >They all have the same history from the Linux kernel for the patch queue
    > >concept. I suspect it's pretty universally implemented, just with different
    > >command names (of course as gods forbid it be consistent).


Truth to that.

I've often advocated for the big three to converge on repository format and
wire protocol, and for them to innovate and differentiate on ui.  The models
might be different enough that you couldn't do it 100%, but the existence of
mapping extensions (e.g. hg-git, bzr-hg) seems to imply that they're pretty
darn close.

If we had this, then all the hand wringing about which dVCS to choose would be
essentially moot.  You'd just pick the cli and gui clients you preferred.


Really, sweating over the dVCS tool detracts from what you do care about,
which is developing Python!

-Barry

Response from Dj Gilcrease to Brett Cannon (shelve extension)
=============================================================


::

    From: Dj Gilcrease <digitalxero@gmail.com>
    Date: Sat, 26 Feb 2011 16:48:05 -0500>
    To: Brett Cannon <brett@python.org>
    Cc: python-dev@python.org
    Subject: Re: [Python-Dev] Mercurial conversion repositories

.. index::
   http://mercurial.selenic.com/wiki/ShelveExtension


Hg shelve extension
-------------------

::

    On Sat, Feb 26, 2011 at 3:09 PM, Brett Cannon <brett@python.org> wrote:
    > > Hg's is the mq (Mercurial Queue) extension.


I prefer the hg shelve plugin
(http://mercurial.selenic.com/wiki/ShelveExtension) for this, more
intuitive to me.


Response of Adrian Buehlman to Barry Warsaw
===========================================

::

    Date: Sat, 26 Feb 2011 23:45:24 +0100
    From: Adrian Buehlmann <adrian@cadifra.com>

::

    > > On Feb 26, 2011, at 02:05 PM, R. David Murray wrote:
    > >
    >> >> On Sat, 26 Feb 2011 13:08:47 -0500, Barry Warsaw <barry@python.org> wrote:
    >>> >>> $ cd py27 # now I want to synchronize
    >>> >>> $ hg pull -u ssh://hg@hg.python.org/cpython
    >>> >>>
    >>> >>> but I'm not going to remember that url every time.  It wouldn't be so bad if
    >>> >>> Mercurial remembered the pull URL for me, as (you guessed it :) Bazaar does.
    >> >>
    >> >> How does setting it in the hgrc differ from "remebering" it?
    > >
    > > It's different because you don't use a familiar interface to set it (i.e hg).
    > > You have to know to hack a file to make it work.  That's not awesome user
    > > interface. ;)


.hg/hgrc files
==============

You'd have to take this up with Mercurial's BDFL Matt. He is a strong
advocate for teaching users to learn edit their .hg/hgrc files.

And he's quite firm on not wanting to have Mercurial touch .hg/hgrc --
with the single exception being to write a initial .hg/hgrc on 'hg
clone', containing the default path with the location from where the
repo was cloned.

Regarding Bazaar: FWIW, I periodically retried the speed of 'bzr check'
- and always gave up again looking at bzr due to the horrible slowness
of that command. If I have to use a DVCS I want to be able to check the
integrity of my clones in reasonable time. I do it with a cron job on
our internal server here and I expect it to have finished checking all
our repos when I get to my desk in the morning and look into my email
inbox, reading the daily email with the result of the verify runs.

After all, we do have everything secured with hashes, so we can use
them, don't we?


hg paths
========


::

    >> >> I've never been comfortable with the bzr --remember option because I'm never
    >> >> sure what it is remembering.  Much easier for me to see it in a config file.
    >> >> But, then, that's how my brain works, and other people's will work
    >> >> differently.
    > >
    > > It's easy to tell what it remembers because it's exactly what you told it to
    > > remember ;).  But I guess you're talking about push and pull automatically
    > > remembering the location when none was previously set.  I love that feature.
    > >
    > > And of course, bzr 'remembers' by setting a value in a config file, which of
    > > course you *could* hack if you wanted to.  It's just that you don't normally
    > > have to open your editor and remember which value in which config file you
    > > have to manually modify to set the push and pull locations.  I think that's a
    > > win, but YMMV. :)
    > >
    > > Oh, and 'bzr info' always tells you what the push and pull locations are.

You can use 'hg paths' for that:

See http://selenic.com/repo/hg/help/paths or 'hg help paths' on the command line


::

    >> >> I find bazaar's model confusing, and hg's intuitive, just like Ã‰ric.
    >> >> And consider that I learned bazaar before mercurial.  To me, it makes
    >> >> perfect sense that in a DVCS the "unit" is a directory containing
    >> >> a repository and a working copy, and that the repository is *the*
    >> >> repository.  That is, it has everything related to the project in it,
    >> >> just like the master SVN repository does (plus, since it is a DVCS,
    >> >> whatever I've committed locally but not pushed to the master).  To have
    >> >> a repository that only has some of the stuff in it is, IMO, confusing.
    >> >> I advocated for having all the Python history in one repo partly for
    >> >> that reason.
    > >
    > > I would feel better about Mercurial's if the repo where not intimately tied
    > > with a default working tree (yes, I know -U).  In a sense, that's what
    > > Bazaar's shared repositories are: a place where all your history goes.  In
    > > Bazaar's model though, it's not tied to a specific working tree, and it's
    > > hidden in a dot-directory.
    > >
    > > It's still kind of beside the point - this is the way Mercurial works, and I
    > > don't really mean this thread to be an in-depth comparison between the two.


I'm quite surprised indeed to read that much about Bazaar in this thread
here :)




