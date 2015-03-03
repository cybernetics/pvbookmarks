
.. index::
   pair: hg ; revert
   pair: hg ; backout

.. _hg_subrepository:

=============
Subrepository
=============


- http://mercurial.selenic.com/wiki/Subrepository


.. contents::
   :depth: 3

Introduction
============

Subrepositories is a feature that allows you to treat a collection of 
repositories as a group. This will allow you to clone, commit to, push, and 
pull projects and their associated libraries as a group.

This feature was introduced in a preliminary form in Mercurial 1.3 and has been 
improved steadily since then. There are still some commands that lack proper 
support for sub-repositories, but we will fix them as we come across them and 
as we figure out how to best make them subrepo-aware.

For those used to Subversion, this concept is closest to what you can achieve 
with Subversion directories marked with the svn:externals property. 

Mercurial 1.5 has support for using Subversion repositories as subrepos.

Basic usage
===========

Start
-----

To start using subrepositories, you need two repositories, a main repo and a nested repo:

::

	$ hg init main
	$ cd main
	$ hg init nested
	
Next we'll mark 'nested' as a subrepository by creating an entry for it in the 
special .hgsub file.

::

	$ echo nested = nested > .hgsub
	$ hg add .hgsub

On the left hand side of the assignment is the path in our working dir ('nested'), 
and the right hand side is a URL or path to pull from. Here we're simply going 
to pull from 'nested' using a path relative to main. This says 'anyone who can 
find our main repo can find the nested repo just by tacking nested onto that path'.

Note that the nested repository must actually exist for the line in .hgsub to 
do anything. For instance, if rather than creating a local nested repository 
you attempt to link to a pre-existing remote one, you must ALSO clone that repository:

::

	$ echo nested = https://example.com/nested/repo/path > .hgsub
	$ hg add .hgsub
	$ hg clone https://example.com/nested/repo/path nested
	
	
If you intend to track something other than the current revision of the default 
branch this is also the time when you would update the subrepo to the desired 
revision.

Now let's add some files to nested, and add them.

::

	$ echo test > nested/foo
	$ hg -R nested add nested/foo
	$ hg -R nested commit --message "Initial commit."
	
	
SVN subrepositories
====================

As of version 1.5, Mercurial can also support other repository types for your 
subrepo. For example, if you wanted a subrepo that referred to a Subversion 
repository, you would do something like this:

::

	$ echo 'nested = [svn]https://example.com/nested/trunk/path' >.hgsub
	$ hg add .hgsub
	$ svn co https://example.com/nested/trunk/path nested
	
Currently, Mercurial treats all URLs that do not begin with a '[<repo type>]' 
as beginning with '[hg]'.

Git subrepositories
===================

As of version 1.8, Mercurial supports git subrepositories:

::

	$ echo 'nested = [git]git://example.com/nested/repo/path.git' > .hgsub
	$ hg add .hgsub
	$ git clone git://example.com/nested/repo/path.git nested
	
	
Committing
==========

When we commit, Mercurial will attempt to create a consistent snapshot of the 
state of the entire project and its subrepos. It does this by first attempting 
to commit in all modified subrepos and then recording the state of all subrepos.

::

	$ hg ci -mtest
	
	
committing subrepository nested

Subrepo states are stored in a .hgsubstate file that is managed automatically 
by Mercurial.

Update
======

Whenever Mercurial encounters a changeset containing subrepos, it will attempt 
to pull the specified subrepos and update them to the appropriate state:


::

    $ cd ..
    $ hg clone main main2
    updating working directory
    pulling subrepo nested
    requesting all changes
    adding changesets
    adding manifests
    adding file changes
    added 1 changesets with 1 changes to 1 files
    2 files updated, 0 files merged, 0 files removed, 0 files unresolved


$ cat main2/nested/foo


Subrepos may also contain their own subrepos and Mercurial will recurse as necessary.

Push
====

Mercurial will automatically attempt to first push all subrepos of the current 
repository when you push. This will ensure new changesets in subrepos are 
available when referenced by top-level repositories.

Pull
=====

Notably, the 'pull' command is not recursive. This is because Mercurial won't 
know which subrepos are required until an update to a specific changeset is 
requested. To get pull and update in one step, use 'pull --update'.

Note that this matches exactly how pull works without subrepositories:

'hg pull' gives you the upstream changesets but doesn't affect your working 
directory.

'hg update' updates the contents of your working directory (both in the top 
repo and in all subrepos)

Synchronizing in subrepositories
=================================

Subrepos don't automatically track the latest changeset of their sources. 
Instead, they are updated to the changeset that corresponds with the changeset 
checked out in the top-level changeset. This is so developers always get a 
consistent set of compatible code and libraries when they update.

Thus, updating subrepos is a manual process. Simply run 'hg pull' and 'hg up' 
in the target subrepo, test in the top-level repo, then commit in the top-level 
repo to record the new combination.

The pull in the subrepo is necessary because the automatic subrepo pull that 
happens when you run 'hg up' in the top-level repo only pulls the exact 
revision it needs, as specified in .hgsubstate. Any changesets that are more 
recent than that one will not get pulled.

Delete
======


To remove a subrepo from the parent repo, you must delete the subrepo definition 
from the .hgsub file at the top level of the parent repo. Once you do this, the 
subrepo tree will show up as a set of unknown files when you run hg status, and 
you can delete the files.

Caveats
========

As this is a complex new feature, there are a number of rough edges:

Some commands require a -S or --subrepos switch to operate on subrepos (available 
since Mercurial 1.7)

- Many commands are not aware of subrepos
- Update/merge currently can't remove subrepositories entirely as that might lose 
  local-only changes
- There's no support for merging across renaming/moving subrepos
- Collisions between normal files and subrepos are not handled
- Subrepository pulls are always delayed until needed by an update
- Pull -r will not filter revisions pulled in subrepositories
- Push similarly ignores URLs and revision filters
- Commit doesn't propagate some flags like -A to subrepos




