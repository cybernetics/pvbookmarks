
.. index::
   pair: Git ; Android


.. _git_android:

=================================
Version Control with Repo and Git
=================================


.. seealso::

   - http://source.android.com/source/version-control.html



Introduction
============

To work with the Android code, you will need to use both :ref:`Git <git>` and Repo.

In most situations, you can use Git instead of Repo, or mix Repo and Git commands
to form complex commands. Using Repo for basic across-network operations will
make your work much simpler, however.

Git is an open-source version-control system designed to handle very large projects
that are distributed over multiple repositories.

In the context of Android, we use Git for local operations such as local branching,
commits, diffs, and edits. One of the challenges in setting up the Android project
was figuring out how to best support the outside community--from the hobbiest
community to large OEMs building mass-market consumer devices.

We wanted components to be replaceable, and we wanted interesting components to
be able to grow a life of their own outside of Android.

We first chose a distributed revision control system, then further narrowed it
down to Git.

``Repo`` is a repository management tool that we built on top of Git
---------------------------------------------------------------------

Repo unifies the many Git repositories when necessary, does the uploads to our
revision control system, and automates parts of the Android development workflow.

Repo is not meant to replace Git, only to make it easier to work with Git in the
context of Android.

The repo command is an executable Python script that you can put anywhere in your
path. In working with the Android source files, you will use Repo for across-network
operations.

For example, with a single Repo command you can download files from multiple
repositories into your local working directory.

``Gerrit`` is a web-based code review system for projects that use git
-----------------------------------------------------------------------


:ref:`Gerrit <gerrit>` encourages more centralized use of Git by allowing all authorized users
to submit changes, which are automatically merged if they pass code review.

In addition, Gerrit makes reviewing easier by displaying changes side by side
in-browser and enabling inline comments.
