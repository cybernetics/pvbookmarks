
.. index::
   hg tips

.. _mercurial_tips:

==============
Mercurial tips
==============

.. seealso:: 

   - http://hgtip.com
   - http://docs.python.org/devguide/

Tips1 : merging heads
=====================

.. seealso:: http://mail.python.org/pipermail/python-dev/2011-September/113749.html

A while ago Éric suggested a nice tip to make merges easier and since I
haven't seen many people using it and now I got a chance to use it again, I
think it might be worth showing it once more::

	# so assume you just committed some changes:
	$ hg ci Doc/whatsnew/3.3.rst -m 'Update and reorganize the whatsnew entry
	for PEP 393.'
	# you push them, but someone else pushed something in the meanwhile, so the
	push fails
	$ hg push
	pushing to ssh://hg@hg.python.org/cpython
	searching for changes
	abort: push creates new remote heads on branch 'default'!
	(you should pull and merge or use push -f to force)
	# so you pull the other changes
	$ hg pull -u
	pulling from ssh://hg@hg.python.org/cpython
	searching for changes
	adding changesets
	adding manifests
	adding file changes
	added 4 changesets with 5 changes to 5 files (+1 heads)
	not updating, since new heads added
	(run 'hg heads' to see heads, 'hg merge' to merge)
	# and use "hg heads ." to see the two heads (yours and the one you pulled)
	in the current branch
	$ hg heads .
	changeset:   72521:e6a2b54c1d16
	tag:         tip
	user:        Victor Stinner <victor.stinner at haypocalc.com>
	date:        Thu Sep 29 04:02:13 2011 +0200
	summary:     Fix hex_digit_to_int() prototype: expect Py_UCS4, not Py_UNICODE
	changeset:   72517:ba6ee5cc9ed6
	user:        Ezio Melotti <ezio.melotti at gmail.com>
	date:        Thu Sep 29 08:34:36 2011 +0300
	summary:     Update and reorganize the whatsnew entry for PEP 393.
	# here comes the tip: before merging you switch to the other head (i.e. the
	one pushed by Victor),
	# if you don't switch, you'll be merging Victor changeset and in case of
	conflicts you will have to review
	# and modify his code (e.g. put a Misc/NEWS entry in the right section or
	something more complicated)
	$ hg up e6a2b54c1d16
	6 files updated, 0 files merged, 0 files removed, 0 files unresolved
	# after the switch you will merge the changeset you just committed, so in
	case of conflicts
	# reviewing and merging is much easier because you know the changes already
	$ hg merge
	1 files updated, 0 files merged, 0 files removed, 0 files unresolved
	(branch merge, don't forget to commit)
	# here everything went fine and there were no conflicts, and in the diff I
	can see my last changeset
	$ hg di
	diff --git a/Doc/whatsnew/3.3.rst b/Doc/whatsnew/3.3.rst
	[...]
	# everything looks fine, so I can commit the merge and push
	$ hg ci -m 'Merge heads.'
	$ hg push
	pushing to ssh://hg@hg.python.org/cpython
	searching for changes
	remote: adding
	changesets
	remote: adding manifests
	remote: adding file changes
	remote: added 2 changesets with 1 changes to 1 files
	remote: buildbot: 2 changes sent successfully
	remote: notified python-checkins at python.org of incoming changeset
	ba6ee5cc9ed6
	remote: notified python-checkins at python.org of incoming changeset
	e7672fe3cd35



This tip is not only useful while merging, but it's also useful for
python-checkins reviews, because the "merge" mail has the same diff  of the
previous mail rather than having 15 unrelated changesets from the last week
because the committer didn't pull in a while.

Tip 2 -- extended diffs
=======================

If you haven't already, enable git diffs, adding to your ~/.hgrc the
following two lines::

	[diff]
	git = True

(this is already in the devguide, even if 'git = on' is used there. The
mercurial website uses git = True too.)
More info:  http://hgtip.com/tips/beginner/2009-10-22-always-use-git-diffs/

Tip 3 -- extensions: color , progress
=====================================

I personally like the 'color' extension, it makes the output of commands
like 'hg diff' and 'hg stat' more readable (e.g. it shows removed lines in
red and added ones in green).
If you want to give it a try, add to your ~/.hgrc the following two lines::

	[extensions]
	color =


If you find operations like pulling, updating or cloning too slow, you might
also want to look at the 'progress' extension, which displays a progress bar
during these operations::

	[extensions]
	progress =

Tip 4 -- porting from 2.7 to 3.2
================================

The devguide suggests::

    hg export a7df1a869e4a | hg import --no-commit -
    

but it's not always necessary to copy the changeset number manually.
If you are porting your last commit you can just use 'hg export 2.7' (or any
other branch name)::

	* using the one-dir-per-branch setup:
	  wolf at hp:~/dev/py/2.7$ hg ci -m 'Fix some bug.'
	  wolf at hp:~/dev/py/2.7$ cd ../3.2
	  wolf at hp:~/dev/py/3.2$ hg pull -u ../2.7
	  wolf at hp:~/dev/py/3.2$ hg export 2.7 | hg import --no-commit -
	* using the single-dir setup:
	  wolf at hp:~/dev/python$ hg branch
	  2.7
	  wolf at hp:~/dev/python$ hg ci -m 'Fix some bug.'
	  wolf at hp:~/dev/python$ hg up 3.2  # here you might enjoy the progress
	  extension
	  wolf at hp:~/dev/python$ hg export 2.7 | hg import --no-commit -
	  
  
And then you can check that everything is fine, and commit on 3.2 too.
Of course it works the other way around (from 3.2 to 2.7) too.

I hope you'll find these tips useful.

Best Regards,
Ezio Melotti

