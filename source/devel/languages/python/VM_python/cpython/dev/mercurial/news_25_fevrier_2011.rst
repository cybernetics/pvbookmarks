

.. index::
   25 february 2011
   Python dev with mercurial
   mercurial python transition

====================================================
python dev with mercurial announce, 25 february 2011
====================================================


 
The announce by Antoine Pitrou
==============================
  
::

	To: python-dev@python.org
	From: Antoine Pitrou <solipsis@pitrou.net>
	Date: Fri, 25 Feb 2011 01:19:04 +0100
	Lines: 95
	Subject: [Python-Dev] Mercurial conversion repositories



Hello,

Georg and I have been working on converting the SVN repository to
Mercurial. We can now present you a test repository (actually, two).


CPython repository
------------------

.. seealso:: http://hg.python.org/cpython/


This is the main conversion repository. It contains all history of
trunk and py3k (since 1990!) up to now, including all maintenance
branches starting from 2.0 up to 3.2.


For core developer
------------------


If you are a core developer, get your local clone of the repository
using::

    $ hg clone ssh://hg@hg.python.org/cpython

(this uses the same SSH key as your Subversion access; for more
information about Mercurial and SSH keys, see the converted development
FAQ: http://potrou.net/hgdevguide/faq.html#faq )


For non-core developer
----------------------

If you are not a core developer::

    $ hg clone http://hg.python.org/cpython

Your clone will contain the following branches::

    $ hg branches
    default                    68026:f12ef116dd10
    3.2                        68025:cef92ee1a323
    2.7                        68010:8174d00d0797
    3.1                        67955:5be8b695ea86
    2.6                        67287:5e26a860eded
    2.5                        65464:e4ecac76e499
    trunk                      62750:800f6c92c3ed
    3.0                        60075:1d05144224fe
    2.4                        58552:df72cac1899e
    2.3                        45731:a3d9a9730743
    2.2                        40444:d55ddc8c8501
    2.1                        30171:06fcccf6eca8
    2.0                        18214:dc0dfc9565cd

The branch "default" is the current py3k branch from SVN. The branch
"trunk" represents SVN trunk history until 2.7 was branched for
maintenance.

The full list of tags is too long to print here, but you can get it
using:

    $ hg tags

The size of the repository on-disk is (depending on your filesystem):

    $ du -hs .hg
    176M    .hg

(the size of the network transfer is estimated to be around 80MB)

You can commit and even push to this repository (the latter if you are a
core developer).  Since this is a test repository, whatever you push
will be discarded when we do the final conversion.


CPython with extra history
==========================


.. seealso:: http://hg.python.org/cpythonextrahist/


This repository is bigger, and has a much more complicated topology. It
is a superset of the other repository, and contains the totality of the
branches from the SVN repository (it has more than 450 repository
heads, of which 87 non-closed). It also weighs quite a bit more:

    $ du -hs .hg
    248M    .hg

This repository is unnecessary for development work, since even for
history-digging purposes the normal repository has the necessary
information. This repository is only to preserve historical record of
some of the non-trunk development work from the SVN repository (such
as orphaned/deleted feature branches).


Development guide
=================

.. seealso:: http://potrou.net/hgdevguide/

This is the development guide adapted for Mercurial. 

Sources
-------

You can get its sources from the branch "hg_transition" in http://hg.python.org/devguide/.


Regards

Antoine.


Barry Warsaw question
=====================

::
   
	Date: Fri, 25 Feb 2011 11:12:53 -0500
	From: Barry Warsaw <barry@python.org>
	To: python-dev@python.org
	Subject: Re: [Python-Dev] Mercurial conversion repositories

	 
On Feb 25, 2011, at 01:50 AM, Raymond Hettinger wrote::

	>
	>On Feb 25, 2011, at 12:09 AM, Martin v. Löwis wrote:
	>
	>> I think I would have liked the strategy of the PEP better (i.e.
	>> create clones for feature branches, rather than putting all
	>> in a single repository).
	>
	>In my brief tests, the single repository has been easy to work with.
	>If they were separate, it would complicate backporting patches
	>and merges.  So, I'm happy with how George and Benjamin put this together.

The way I work with the Subversion branches is to have all the active 
branches checked out into separate directories under a common parent, e.g::

	~/projects/python/py26
	~/projects/python/py27
	~/projects/python/trunk
	~/projects/python/py31
	~/projects/python/py32
	~/projects/python/py3k

This makes it very easy to just cd, svn up, make distclean, configure, 
make  to test things.  

How can I do this with the hg clone when all the branches are in the single 
repository, but more or less hidden?  After doing the 'hg clone'
operation specified by Antoine, I'm left with a single cpython directory
containing (iiuc) the contents of the 'default' branch.

I'm sure I'm not the only one who works this way with Subversion.  IWBN to
cover this in the devguide (or is it there and I missed it?).

Cheers,
-Barry

Response from adrian@cadifra.com
================================

.. seealso:: https://bitbucket.org/abuehl

::

	Date: Fri, 25 Feb 2011 18:40:53 +0100
	From: Adrian Buehlmann <adrian@cadifra.com>


I know (almost) nothing about developing Python (this is my first post
to this list after lurking for quite a while now), but as a regular
Mercurial contributor, I think the following could be useful for you:

First, get an initial clone (let's name it 'master') over the wire
using: [1_]

  $ hg clone -U ssh://hg@hg.python.org/cpython master

Then create a hardlinked clone [2_]_ for working in each branch,
specifying the branch to check out using option -u::

	$ hg clone master py26 -u 2.6
	updating to branch 2.6
	NNN files updated, 0 files merged, 0 files removed, 0 files unresolved

	$ hg clone master py27 -u 2.7
	updating to branch 2.7
	NNN files updated, 0 files merged, 0 files removed, 0 files unresolved

	$ hg clone master trunk -u trunk
	updating to branch trunk
	NNN files updated, 0 files merged, 0 files removed, 0 files unresolved

	$ hg clone master py31 -u 3.1
	updating to branch 3.1
	NNN files updated, 0 files merged, 0 files removed, 0 files unresolved

	$ hg clone master py32 -u 3.2
	updating to branch 3.2
	NNN files updated, 0 files merged, 0 files removed, 0 files unresolved

This will be fast and save space as these local 'branch clones' will
share diskspace inside .hg/store by using hardlinks, and you need to do
the initial slow clone over the wire only once.

Note that each of these branch clones will initially have your local
master repo as the default path [3_,4_]. If you'd like to have the default
push/pull path to point to ssh://hg@hg.python.org/cpython instead, you'd
want to edit the [paths] section in the .hg/hgrc file in each of the
branch repos. But of course you can also leave the default paths as they
are and synchronize via the master repo (e.g. pull new changesets into
master first, and then pull into the specific branch repo).

.. _1: http://selenic.com/repo/hg/help/clone
.. _2: http://mercurial.selenic.com/wiki/HardlinkedClones
.. _3: http://www.selenic.com/mercurial/hgrc.5.html#paths
.. _4: http://selenic.com/repo/hg/help/urls


Barry Warsaw question
=====================

::

	Date: Fri, 25 Feb 2011 14:43:15 -0500
	From: Barry Warsaw <barry@python.org>

Thanks very much Adrian, this is exactly what I was looking for.  It maps
almost directly to my current mental model for working on Python in Subversion
(and truth be told, also how I do/did it with Bazaar).

It does leave me with an empty 'master' directory that I basically won't
touch, though I suppose I could hide it in a dot-filename.  And I have to
remember to fiddle with .hg/hgrc when I clone a new branch working directory,
but I guess that's mostly a one-time cost.

I'll have to remember that 'hg pull' does not update the working copy by
default, and eventually I'll figure out the whole merge thing.

One immediate thing that I'm missing from Bazaar is that 'bzr commit' invokes
my editor and always shows me a 'diff -u' in the commit message buffer.  This
is incredibly handy because I don't have to remember to do the diff in a
different window, and I always have all the information I want right there to
craft the commit message.  It doesn't look like this is possible with 'hg
commit' though, right?

Cheers,
-Barry


::

	> > 
	> > I'll have to remember that 'hg pull' does not update the working copy by
	> > default, and eventually I'll figure out the whole merge thing.
	You can use "hg pull -u" to update (and "hg pull -uv" if you want to
	see the list of updated files).





