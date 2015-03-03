

.. index::
   27 february 2011

====================================================
python dev with mercurial announce, 27 february 2011
====================================================


.. index::
   hg-git

Response of  Daniel Stuzbach to Brett Cannon
============================================

hg-git
------

.. seealso:: http://wiki.python.org/moin/Git

::

    Date: Sat, 26 Feb 2011 15:08:19 -0800
    From: Daniel Stutzbach <stutzbach@google.com>
    To: Brett Cannon <brett@python.org>
    Cc: python-dev@python.org
    Subject: Re: [Python-Dev] Mercurial conversion repositories


::

    > > There is hg-git, but that is hg on top of git.
    > >



Actually, hg-git is bidirectional.  The hg-git documentation is written from
the perspective of an hg client talking to a git server, but for a DVCS
"client" and "server" are  a matter of perspective.

I spent some time on Friday setting up hg-git on my workstation and making a
few test commits.  It took me awhile to figure out how to get everything
working, but it seems to work smoothly now.

At some point I'll update
http://wiki.python.org/moin/Git with instructions.


.. index::
   hgdevguide
   http://potrou.net/hgdevguide/

hgdevguide, http://potrou.net/hgdevguide/
=========================================

::

    From: Dj Gilcrease <digitalxero@gmail.com>
    Date: Sat, 26 Feb 2011 18:13:15 -0500


So reading the thread about the conversion and the dev guide at
http://potrou.net/hgdevguide/ there seems to not be a list of
recommended extensions that the python devs should have and use, only
a few examples of their use. so I figured I would build up a list for
other people to add to / comment on

File Format Management

    eol

        http://mercurial.selenic.com/wiki/EolExtension
        required

    flake8

        http://pypi.python.org/pypi/flake8/
        recommended especially for new commiters as it will validate
        pep8 compliance and check for common errors
        Maybe update it to do pep7 compliance checks on the c files as well?

Patch Management

    mq
        http://mercurial.selenic.com/wiki/MqExtension
        This is the one the devguide uses in examples

    rebase
        http://mercurial.selenic.com/wiki/RebaseExtension
        used with the --collapse option it is very easy to build up a
        patch patch with incremental commits, but discard the private history
        of the developer
        This one makes more sense to me personally then mq and fits
        how my standard workflow goes better

    shelve
        http://mercurial.selenic.com/wiki/ShelveExtension
        Store un commited changes away so they dont affect generation
        of the patch

    transplant
        http://mercurial.selenic.com/wiki/TransplantExtension
        required to port patches between major versions

    record
        http://mercurial.selenic.com/wiki/RecordExtension
        Allows cherry picking of commits to build a patch, Also works with mq

    Crecord
        http://mercurial.selenic.com/wiki/CrecordExtension
        appears to be a c optimized version or record

Branch Management

    bookmarks
        http://mercurial.selenic.com/wiki/BookmarksExtension
        Great for tracking bug fix work without needing to create a
        separate working directory
        recommended that the central repo NOT have the extension
        enabled so as to ensure bookmarks are a local only tracking system



.. index::
   hg bookmarks

Response of  Daniel Stuzbach to Brett Cannon
============================================

::

    Date: Sun, 27 Feb 2011 00:41:05 +0100
    From: Adrian Buehlmann <adrian@cadifra.com>


::


    > > Branch Management
    > >     bookmarks
    > >         http://mercurial.selenic.com/wiki/BookmarksExtension


Bookmarks will be in Mercurial core for Mercurial 1.8, which will be
released in a few days (March 1st). So, with 1.8 it's no longer needed
to enable this extension in the configuration -- the feature will be
built-in.


Reponse of Antoine Pitrou to Dj Gilcrease
=========================================

::

    From: Antoine Pitrou <solipsis@pitrou.net>
    Date: Sun, 27 Feb 2011 01:59:48 +0100


eol
---

::


    > >
    > > File Format Management
    > >     eol
    > >         http://mercurial.selenic.com/wiki/EolExtension
    > >         required


Actually, it isn't *required* on each developer's setup, since we
now have a hook that refuses bogus changegroups (if needed, we can even
refuse individual changesets).  In most situations, even without the
eol extension line endings won't get modified anyway.


flake8
------

::

    > >     flake8
    > >         http://pypi.python.org/pypi/flake8/
    > >         recommended especially for new commiters as it will validate
    > > pep8 compliance and check for common errors


IMHO, nothing replaces human reviews and communication for style
and other likewise issues.


mq, rebase, shelve
------------------


::

    > > Patch Management
    > >     mq
    > >     rebase
    > >     shelve


All these depend on each developer's taste, as long as only collapsed
patches get submitted and committed.


transplant
----------


::

    > >     transplant
    > >         http://mercurial.selenic.com/wiki/TransplantExtension
    > >         required to port patches between major versions


Not really required, and actually controversial since it commits
automatically (we would like people to commit and test *before*
committing, otherwise buildbots can get bogus changesets and spurious
failures).


bookmarks
---------

::

    > >     bookmarks
    > >         http://mercurial.selenic.com/wiki/BookmarksExtension
    > >         Great for tracking bug fix work without needing to create a
    > > separate working directory
    > >         recommended that the central repo NOT have the extension
    > > enabled so as to ensure bookmarks are a local only tracking system



Actually quite poor for tracking bug fix work (see my other messages in
this thread :-)).

Regards

Antoine.


Response from Adrian Buehlman to Barry Warsaw
=============================================

::

    Date: Sun, 27 Feb 2011 02:15:51 +0100
    From: Adrian Buehlmann <adrian@cadifra.com>


::


    > > On Feb 26, 2011, at 11:45 PM, Adrian Buehlmann wrote:
    > >
    >> >> You'd have to take this up with Mercurial's BDFL Matt. He is a strong
    >> >> advocate for teaching users to learn edit their .hg/hgrc files.
    > >
    > > Well, I guess it's doubtful I'd change his mind then. :)

Yep.

hg verify
=========

::

    >> >> Regarding Bazaar: FWIW, I periodically retried the speed of 'bzr check'
    >> >> - and always gave up again looking at bzr due to the horrible slowness
    >> >> of that command. If I have to use a DVCS I want to be able to check the
    >> >> integrity of my clones in reasonable time. I do it with a cron job on
    >> >> our internal server here and I expect it to have finished checking all
    >> >> our repos when I get to my desk in the morning and look into my email
    >> >> inbox, reading the daily email with the result of the verify runs.
    >> >>
    >> >> After all, we do have everything secured with hashes, so we can use
    >> >> them, don't we?
    > >
    > > Do you know how thorough 'bzr check' is?  I don't, but then I've never used it
    > > or felt the need to. ;)


That's quite amazing. If I talk with people about that, it often turns
out that they don't check the integrity of their repos.

Well, hg verify *is* through and fast enough. That's good enough for me.

And being slow is not sufficient to earn my trust.

FWIW, be aware that Mercurial does not do integrity checks on normal
operations, so chances are you will be able to use a repo that fails
verify for quite a while -- without even noticing it.

For example you can remove *some* file X inside .hg/store/data and
continue to add history to that repo without any sign of errors, as long
as the file X isn't used during the operations you do.


Response from Adrian Buehlman to Greg Ewing
============================================

::

    Date: Sun, 27 Feb 2011 11:42:21 +0100
    From: Adrian Buehlmann <adrian@cadifra.com>


hg branch  --force, graphlogextension
=====================================


::

    > > From: Antoine Pitrou
    >> >> - a "branch" usually means a "named branch": a set of changesets
    >> >>   bearing the same label (e.g. "default"); that label is freely chosen
    >> >>   by the committer at any point, and enforces no topological
    >> >>   characteristic
    > >
    > > There are *some* topological restrictions, because hg won't
    > > let you assign a branch name that's been used before to a node
    > > unless one of its parents has that name. So you can't create
    > > two disconnected subgraphs whose nodes have the same branch
    > > name.


That's not completely correct. You *can* do that.

Mercurial by default assumes you're probably in error if you are
trying to create such disconnected branch name subgraphs, but you
can convince it that it's really what you want by doing::

    hg branch --force <existing branch name>


Example (glog command requires the graphlog extension enabled [1])::

      $ hg init a
      $ cd a
      $ echo foo > bla
      $ hg ci -Am1
      adding bla
      $ hg branch b1
      marked working directory as branch b1
      $ hg ci -m2
      $ hg branch default
      abort: a branch of the same name already exists (use 'hg update' to switch to it)
      $ hg branch --force default
      marked working directory as branch default
      $ hg ci -m3
      created new head
      $ hg glog --template "{rev}, {branch}\n"
      @  2, default
      |
      o  1, b1
      |
      o  0, default


[1] http://mercurial.selenic.com/wiki/GraphlogExtension


Reponse of Antoine Pitrou to Martin von Lowis, changeset, tip
=============================================================

::

    Date: Sun, 27 Feb 2011 16:08:21 +0100
    From: Antoine Pitrou <solipsis@pitrou.net>


::

    >>> > >> changeset:   72694:e65daae6cf44
    >>> > >> user:        Antoine Pitrou <solipsis@pitrou.net>
    >>> > >> date:        Mon Feb 21 21:30:55 2011 +0000
    >>> > >> summary:     Try s/UINT_MAX/INT_MAX/
    >> > >
    >> > > It's not on an unnamed branch, it's on the "default" branch (which is
    >> > > omitted for concision by "hg log" and other commands with a similar
    >> > > output).
    > >
    > > It's probably a terminology issue, but: the changeset can't be "on"
    > > the default "branch", because the head of the default branch (called
    > > "tip", IIUC) isn't a descendant of that changeset.


Well, a branch (or named branch) in hg terminology can have several
heads (see the other email about heads and branches).

Also, just so you know, "tip" is simply the latest (in pull or commit
order) changeset in the local repository. It can be in any branch (for
example, if you pull of bunch of changesets someone made in "3.2",
then your tip will be in branch "3.2").

I hope it all starts to make sense ;)

Regards

Antoine.


Reponse of Nick Coghlan to Atoine Pitrou, eol extension
=======================================================

::

    Date: Mon, 28 Feb 2011 01:23:29 +1000
    From: Nick Coghlan <ncoghlan@gmail.com>
    To: Antoine Pitrou <solipsis@pitrou.net>
    Cc: python-dev@python.org
    Subject: Re: [Python-Dev] hg extensions was Mercurial conversion repositories


::

    > > On Sun, 27 Feb 2011 07:46:51 +0100
    > > "Martin v. Löwis" <martin@v.loewis.de> wrote:
    >>> >> > Actually, it isn't *required* on each developer's setup, since we
    >>> >> > now have a hook that refuses bogus changegroups (if needed, we can even
    >>> >> > refuse individual changesets).  In most situations, even without the
    >>> >> > eol extension line endings won't get modified anyway.
    >> >>
    >> >> I think this is overly optimistic. Visual Studio will break all your
    >> >> files if you don't use that extension (and you actually use it to
    >> >> modify source code).
    > >
    > > My assumption was that most developers don't use MSVC, so most of them
    > > don't risk breaking eols ;)
    > > True, for Windows devs it might be necessary to promote it.


Windows devs were the original target audience, yes :)

Cheers,
Nick.


Announce of tortoise Hg 2.0 by Adrian Buehlman
==============================================

::

    Date: Sun, 27 Feb 2011 17:01:37 +0100
    From: Adrian Buehlmann <adrian@cadifra.com>


::

    > > On 2/27/2011 10:18 AM, Antoine Pitrou wrote:
    >> >> Well, chances are TortoiseHG comes with an UI to apply patches
    >> >> (TortoiseSVN had one), so the command-line instructions may be of
    >> >> little use to them.
    > >
    > > I don't believe TortoiseHG has such a feature (or I can't find it),
    > > although if you have TortoiseSVN, you can still use that as a patch tool.


TortoiseHg can import patches just fine.

FWIW, we are very close to releasing TortoiseHg 2.0 (due March 1st),
which ported the current Gtk based TortoiseHg to Qt (although, it was
more like a rewrite :-).

For the old Gtk TortoiseHg, see the online docs here:

  http://tortoisehg.bitbucket.org/manual/1.1/patches.html#import-patches

Homepage for the Qt port
------------------------


https://bitbucket.org/tortoisehg/thg/wiki/Home

For people on Windows, we have beta installers for the new Qt based
TortoiseHg at:

   https://bitbucket.org/tortoisehg/thg/downloads

Feedback is welcome on::

  thg-dev@googlegroups.com or
  tortoisehg-discuss@lists.sourceforge.net

(we moved the development list to google groups)



.. index::
   hgeditor

Annouce of George Brandl for the hgeditor extension
===================================================

::

    To: python-dev@python.org
    From: Georg Brandl <g.brandl@gmx.net>
    Date: Sun, 27 Feb 2011 17:38:26 +0100



Martin v. Lowis, eol
====================


::

    > > On Feb 26, 2011, at 01:49 AM, Éric Araujo wrote:
    > >
    >> >>You speak to my heart, sir.  In your ~/.hgrc, under the section [ui],
    >> >>set “editor = path/to/mercurial/source/hgeditor” and enjoy your diffs.
    >> >>I use it and love it.
    > >
    > > Except it doesn't quite work the way I want it to (hg 1.6.3).  It opens your
    > > editor with two files, one is the commit message and the other is the diff.
    > > (The script itself is a bit buggy too. ;)
    > >
    > > But it's a good clue, and I've modified the default hgeditor script to get
    > > closer, and fix the bug I noticed.  I basically append the diff to the
    > > temporary log message file.  It's still not right though because if the diff
    > > lines aren't prepended with 'HG:', they end up in the commit message.  Arg.
    > >
    > > Oh well, I can clearly hack a more complicated script together.  It's such a
    > > blindingly obvious improvement, it's too bad 'hg commit' doesn't DTRT by
    > > default.


While I understand the usefulness of the diff feature, it is not useful to
everyone, e.g. those using almost exclusively ``commit -m message``.

Of course it would be nice if hg made it easier (a hgrc option, for example)
to do this.

BTW, I had not heard of hgeditor before, and wrote a small hg extension to
do what you want (with HG: prefix :) before I saw that others had already
replied with hgeditor.  The extension had 10 lines of code.

Georg


::

    Cc: Antoine Pitrou <solipsis@pitrou.net>, python-dev@python.org
    Subject: Re: [Python-Dev] hg extensions was Mercurial conversion repositories



::

    >> I think this is overly optimistic. Visual Studio will break all your
    >> >> files if you don't use that extension (and you actually use it to
    >> >> modify source code).
    > >
    > > My assumption was that most developers don't use MSVC, so most of them
    > > don't risk breaking eols ;)
    > > True, for Windows devs it might be necessary to promote it.


If I change code on Windows, I always use MSVC to edit it. It's best
integrated with the build process and the debugger. If I change Python
code on Windows, I use vim or IDLE.

Different MSVC releases took different approaches wrt. LF-separated
files. For a long time, new lines added would be CRLF, whereas existing
line endings would remain unchanged, resulting in a mix of line endings.
It appears that VS 2008 now uniformly converts the entire file to CRLF
on first edit.

Regards,
Martin




