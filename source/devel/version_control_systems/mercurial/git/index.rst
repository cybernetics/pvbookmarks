
.. index::
   pair: mercurial ; git
   pair: hg ; git
   pair: hg ; github

.. _hg_git:

==============
hg git
==============



.. contents::
   :depth: 3


using-hg-git-to-work-in-git-and-push-to-hg
===========================================


.. seealso::

   - http://traviscline.com/blog/2010/04/27/using-hg-git-to-work-in-git-and-push-to-hg/

::

    > Hello,
    > I'd like to use a private git repository, then I need to migrate my
    > actual private mercurial repository.
    >
    > I've tried to use https://bitbucket.org/repo/import but my mercurial
    > url is not found by bitbucket.

You'll have to convert it locally using hg-git or similar. This blog
posts should help you: http://traviscline.com/blog/2010/04/27/using-hg-git-to-work-in-git-and-push-to-hg/



hg github
=========


.. seealso::

   - http://pypi.python.org/pypi/hg-github/0.1.2



hg-github is a Mercurial extension that wraps hg-git, and supports a work-flow
where repositories are hosted on Bitbucket and mirrored on GitHub.

This work-flow normally requires adding Git paths to each repository's
config file, and creating Mercurial bookmarks pointing to the GitHub repository's
branch name. hg-github takes care of these for you automatically.

hg-github is BSD licensed.


