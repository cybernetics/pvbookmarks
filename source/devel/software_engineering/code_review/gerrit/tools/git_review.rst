
.. index::
   pair: git; review

.. _git_review:

=====================
Git review
=====================


.. seealso::

   - https://github.com/openstack-ci/git-review
   - :ref:`git`

A git command for submitting branches to Gerrit

git-review is a tool that helps submitting git branches to gerrit for review.


Setup
=====

git-review, by default, looks for a git remote called gerrit, and submits the
current branch to HEAD:refs/for/master at that remote.

If the "gerrit" remote does not exist, git-review looks for a file
called .gitreview at the root of the repository with information about the
gerrit remote.

Assuming that file is present, git-review should be able to automatically
configure your repository the first time it is run.
