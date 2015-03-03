

.. index::
   hg eol

===========================================
[PATCH] eol: add an allcsethook (issue2665)
===========================================

::


    Antoine Pitrou <solipsis@pitrou.net>
    heure de l'expéditeur   Envoyé à 20:28 (GMT+01:00). Heure locale : 13:26. ✆
    à   mercurial-devel@selenic.com
    date    28 février 2011 20:28
    objet   [PATCH] eol: add an allcsethook (issue2665)

::


    # HG changeset patch
    # User Antoine Pitrou <solipsis@pitrou.net>
    # Date 1298920868 -3600
    # Branch stable
    # Node ID f8e1163f93a599c1948f208a11b752dcc3dd4b15
    # Parent  c54c35307a7ab547de32268d42ef2ecdcc37bec2
    eol: add an allcsethook (issue2665)

eol's built-in hook checks the content of modified files in the
final changegroup changeset.  This allows people to fix their
blunder in a subsequent commit and then push the whole bunch.

Another wish can be to reject any individual changeset containing
wrong line endings, because they pollute history (as well as the
subsequent line ending-fixing changesets).  The allcsethook achieves
that.

::

    diff --git a/hgext/eol.py b/hgext/eol.py
    --- a/hgext/eol.py
    +++ b/hgext/eol.py
    @@ -79,6 +79,14 @@
     Remember to enable the eol extension in the repository where you
     install the hook.

    +Another hook named ``eol.allcsethook`` is provided.  While ``eol.hook``
    +checks the contents of files in the last changeset of a changegroup
    +(allowing people to fix their bogus commit in a later changeset before
    +pushing both), ``eol.allcsethook`` examines all incoming changesets for
    +line ending mistakes.  This places a stricter burden on developers while
    +allowing for a cleaner public history (no repository pollution with
    +line ending-fixing changsets).
    +
     See :hg:`help patterns` for more information about the glob patterns
     used.
     """
    @@ -128,6 +136,40 @@
     }


    +def checkfile(ui, repo, node, file):
    +    """check that a file in the given node has expected EOLs"""
    +    for pattern, target in ui.configitems('encode'):
    +        if match.match(repo.root, '', [pattern])(file):
    +            data = node[file].data()
    +            if ((target == "to-lf" and "\r\n" in data) or
    +                (target == "to-crlf" and singlelf.search(data))):
    +                return target
    +            # Ignore other rules for this file
    +            break
    +
    +def allcsethook(ui, repo, node, hooktype, **kwargs):
    +    """verify that files in all new csets have expected EOLs"""
    +    failed = []
    +    for rev in xrange(repo[node].rev(), len(repo)):
    +        ctx = repo[rev]
    +        for f in ctx.files():
    +            if f not in ctx:
    +                # File was removed in rev
    +                continue
    +            target = checkfile(ui, repo, ctx, f)
    +            if target:
    +                failed.append((ctx, f, target))
    +    if failed:
    +        msgs = []
    +        for ctx, f, target in failed:
    +            if target == "to-lf":
    +                msgs.append(_("%s in %s should not have CRLF line endings")
    +                            % (f, ctx))
    +            elif target == "to-crlf":
    +                msgs.append(_("%s in %s should not have LF line endings")
    +                            % (f, ctx))
    +        raise util.Abort("\n".join(msgs))
    +
     def hook(ui, repo, node, hooktype, **kwargs):
        """verify that files have expected EOLs"""
        files = set()
    @@ -137,18 +179,13 @@
        for f in files:
            if f not in tip:
                continue
    -        for pattern, target in ui.configitems('encode'):
    -            if match.match(repo.root, '', [pattern])(f):
    -                data = tip[f].data()
    -                if target == "to-lf" and "\r\n" in data:
    -                    raise util.Abort(_("%s should not have CRLF line endings")
    -                                     % f)
    -                elif target == "to-crlf" and singlelf.search(data):
    -                    raise util.Abort(_("%s should not have LF line endings")
    -                                     % f)
    -                # Ignore other rules for this file
    -                break
    -
    +        target = checkfile(ui, repo, tip, f)
    +        if target == "to-lf":
    +            raise util.Abort(_("%s should not have CRLF line endings")
    +                             % f)
    +        elif target == "to-crlf":
    +            raise util.Abort(_("%s should not have LF line endings")
    +                             % f)

     def preupdate(ui, repo, hooktype, parent1, parent2):
        #print "preupdate for %s: %s -> %s" % (repo.root, parent1, parent2)
    diff --git a/tests/test-eol-hook.t b/tests/test-eol-allcsethook.t
    copy from tests/test-eol-hook.t
    copy to tests/test-eol-allcsethook.t
    --- a/tests/test-eol-hook.t
    +++ b/tests/test-eol-allcsethook.t
    @@ -10,7 +10,7 @@
      > eol =
      >
      > [hooks]
    -  > pretxnchangegroup = python:hgext.eol.hook
    +  > pretxnchangegroup = python:hgext.eol.allcsethook
      > EOF
      $ hg clone main fork
      updating to branch default
    @@ -20,16 +20,15 @@
     Create repo
      $ cat > .hgeol <<EOF
      > [patterns]
    -  > mixed.txt = BIN
    -  > crlf.txt = CRLF
    -  > **.txt = native
    +  > a.txt = CRLF
    +  > **.txt = LF
      > EOF
      $ hg add .hgeol
    -  $ hg commit -m 'Commit .hgeol'
    +  $ hg commit -m 'Commit .hgeol' -d 2010-01-01 -u someuser

    -  $ printf "first\nsecond\nthird\n" > a.txt
    +  $ printf "first\r\nsecond" > a.txt
      $ hg add a.txt
    -  $ hg commit -m 'LF a.txt'
    +  $ hg commit -m 'CRLF a.txt' -d 2010-01-01 -u someuser
      $ hg push ../main
      pushing to ../main
      searching for changes
    @@ -38,53 +37,25 @@
      adding file changes
      added 2 changesets with 2 changes to 2 files

    -  $ printf "first\r\nsecond\r\nthird\n" > a.txt
    -  $ hg commit -m 'CRLF a.txt'
    +  $ printf "first\nsecond" > a.txt
    +  $ hg commit -m 'LF a.txt' -d 2010-01-01 -u someuser
    +  $ printf "third\r\n" > b.txt
    +  $ hg add b.txt
    +  $ hg commit -m 'CRLF b.txt' -d 2010-01-01 -u someuser
    +  $ printf "first\r\nsecond" > a.txt
    +  $ hg rm b.txt
    +  $ hg commit -m 'CRLF a.txt, rm b.txt' -d 2010-01-01 -u someuser
      $ hg push ../main
      pushing to ../main
      searching for changes
      adding changesets
      adding manifests
      adding file changes
    -  added 1 changesets with 1 changes to 1 files
    -  error: pretxnchangegroup hook failed: a.txt should not have CRLF line endings
    +  added 3 changesets with 3 changes to 2 files
    +  error: pretxnchangegroup hook failed: a.txt in 586b8cd9e131 should not have LF line endings
    +  b.txt in ca83fc6c9fac should not have CRLF line endings
      transaction abort!
      rollback completed
    -  abort: a.txt should not have CRLF line endings
    +  abort: a.txt in 586b8cd9e131 should not have LF line endings
    +  b.txt in ca83fc6c9fac should not have CRLF line endings
      [255]
    -
    -  $ printf "first\nsecond\nthird\n" > a.txt
    -  $ hg commit -m 'LF a.txt (fixed)'
    -  $ hg push ../main
    -  pushing to ../main
    -  searching for changes
    -  adding changesets
    -  adding manifests
    -  adding file changes
    -  added 2 changesets with 2 changes to 1 files
    -
    -  $ printf "first\nsecond\nthird\n" > crlf.txt
    -  $ hg add crlf.txt
    -  $ hg commit -m 'LF crlf.txt'
    -  $ hg push ../main
    -  pushing to ../main
    -  searching for changes
    -  adding changesets
    -  adding manifests
    -  adding file changes
    -  added 1 changesets with 1 changes to 1 files
    -  error: pretxnchangegroup hook failed: crlf.txt should not have LF line endings
    -  transaction abort!
    -  rollback completed
    -  abort: crlf.txt should not have LF line endings
    -  [255]
    -
    -  $ printf "first\r\nsecond\r\nthird\r\n" > crlf.txt
    -  $ hg commit -m 'CRLF crlf.txt (fixed)'
    -  $ hg push ../main
    -  pushing to ../main
    -  searching for changes
    -  adding changesets
    -  adding manifests
    -  adding file changes
    -  added 2 changesets with 2 changes to 1 files
    
 
:: index::
   PEP 385
   
      
PEP 385 (Migrating from Subversion to Mercurial)
================================================


.. seealso::  

   - http://www.python.org/dev/peps/pep-0385/
   - http://hg.python.org/hooks/
   - http://mercurial.selenic.com/wiki/EolExtension
   - http://mercurial.selenic.com/wiki/Win32TextExtension

::

	> > Author: antoine.pitrou
	> > Date: Mon Feb 28 19:22:36 2011
	> > New Revision: 88676
	> >
	> > Log:
	> > Update PEP 385 with latest hooks work
	> >
	> >
	> >
	> > Modified:
	> >   peps/trunk/pep-0385.txt
	> >
	> > Modified: peps/trunk/pep-0385.txt
	> >
	> > ==============================================================================
	> > --- peps/trunk/pep-0385.txt     (original)
	> > +++ peps/trunk/pep-0385.txt     Mon Feb 28 19:22:36 2011
	> > @@ -262,7 +262,22 @@
	> >   on every build slave for the branch in which the changeset occurs.
	> >
	> >  The `hooks repository`_ contains ports of these server-side hooks to
	> > -Mercurial.  One additional hook could be beneficial:
	> > +Mercurial, as well as a couple additional ones:
	> > +
	> > +* check branch heads: a hook to reject pushes which create a new head on
	> > +  an existing branch.  The pusher then has to merge the superfetatory
	> > heads
	> > +  and try pushing again.
	> > +
	> > +* check branches: a hook to reject all changesets not on an allowed named
	> > +  branch.  This hook's whitelist will have to be updated when we want to
	> > +  create new maintenance branches.
	> > +
	> > +* check line endings: a hook, based on the `eol extension`_, to reject all
	> > +  changesets committing files with the wrong line endings.  The commits
	> > then
	> > +  have to be stripped and redone, possibly with the `eol extension`_
	> > enabled
	> > +  on the comitter's computer.
	> > +
	> > +One additional hook could be beneficial:
	> >
	> >  * check contributors: in the current setup, all changesets bear the
	> >   username of committers, who must have signed the contributor
	> > @@ -285,9 +300,8 @@
	> >  information is kept in a versioned file called ``.hgeol``, and such a
	> >  file has already been checked into the Subversion repository.
	> >
	> > -A hook on the server side that turns down any changegroup or changeset
	> > -introducing inconsistent newline data can still be implemented, if
	> > -deemed necessary.
	> > +A hook also exists on the server side to reject any changeset
	> > +introducing inconsistent newline data (see above).
	> >
	> >  .. _eol extension: http://mercurial.selenic.com/wiki/EolExtension
	> >  .. _win32text extension: http://mercurial.selenic.com/wiki/Win32TextExtension


