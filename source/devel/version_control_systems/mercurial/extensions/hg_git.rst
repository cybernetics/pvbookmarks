
.. index::
   hg-git


.. _hg_git_extension:

=====================
hg-git extension
=====================


.. seealso::

   - http://hg-git.github.com/
   - http://pypi.python.org/pypi/hg-git/0.2.6
   - http://support.appharbor.com/kb/getting-started/using-appharbor-with-mercurial-and-hg-git
   - :ref:`appharbor`


push and pull from a Git server using Mercurial.

This extension lets you communicate (push and pull) with a Git server.

This way you can use Git hosting for your project or collaborate with a project
that is in Git.


.. warning, this software is still beta.


It is basically feature complete and pretty stable now, but there are still
some edge cases we don't handle well yet and it may be slow in some circumstances.

The user interface is also still subject to change. However, there are now a
lot of people using it effectively, so please do use it and let me know if you
run into anything.


Source
======

- hg clone git://github.com/schacon/munger.git


The easy way
============

Run easy_install hg-git, then add make sure the following is in your ~/.hgrc::

    [extensions]
    hgext.bookmarks =
    hggit =


...and that's it!


The more involved way
=====================

First, install version 0.4.0 or newer of dulwich. You can do easy_install
'dulwich>=0.4.0' if you have setuptools installed. Clone this repository
somewhere, or download a snapshot, then make the 'extensions' section in your
'~/.hgrc' file look something like this::

    [extensions]
    hgext.bookmarks =
    hggit = [path-to]/hg-git/hggit

That will enable the Hg-Git extension for you. The bookmarks section is not
compulsory, but it makes some things a bit nicer. Bookmarks will be translated
to git heads when pushing.

