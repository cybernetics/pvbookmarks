
.. index::
   pair: Distributed Version Control System; Mercurial
   pair: DVCS; Mercurial
   ! Mercurial


.. _mercurial_dvcs:

=========
Mercurial
=========


.. figure:: mercurial_logo.jpg
   :align: center

.. seealso::

   - https://secure.wikimedia.org/wikipedia/en/wiki/Mercurial
   - http://mercurial.selenic.com/wiki/ (official site)
   - https://plus.google.com/u/0/112477627281544607334/posts
   - hg clone https://pvergain@bitbucket.org/mirror/mercurial-crew
   - http://hg.piranha.org.ua/sphinxedhg/docs/test-hgrc.html


.. contents::
   :depth: 3


Introduction
============

Mercurial is a cross-platform, distributed revision control tool for software
developers. It is mainly implemented using the Python programming language,
but includes a binary diff implementation written in C.

It is supported on Windows, Unix-like systems including FreeBSD, OSX and Linux.

Mercurial is primarily a command line program but graphical user interface
extensions are available. All of Mercurial's operations are invoked as keyword
options to its driver program hg, a reference to the chemical symbol of the
element mercury.

Mercurial's major design goals include high performance and scalability,
decentralized, fully distributed collaborative development, robust handling
of both plain text and binary files, and advanced branching and merging
capabilities, while remaining conceptually simple.[3]
It includes an integrated web interface.

The creator and lead developer of Mercurial is Matt Mackall. Released under
the terms of the GNU General Public License (version 2 or any later version).



Glossary
========

.. seealso:: http://mercurial.selenic.com/wiki/Glossary


Downloads
=========

- http://mercurial.selenic.com/


.. index::
   mercurial hg sources


Mercurial issue_tracker
=======================

.. toctree::
   :maxdepth: 3

   issue_tracker/index


Mercurial versions
===================

.. toctree::
   :maxdepth: 3

   versions/index


Mercurial sources
=================

- http://mercurial.selenic.com/wiki/DeveloperRepos

::

    hg clone https://pvergain@bitbucket.org/mirror/mercurial-crew

Main repositories
-----------------


- http://selenic.com/repo/hg – the main repository, bleeding edge, solely
  managed by mpm who often pulls from other repositories (mirrored at http://hg.intevation.org/mercurial/)


- http://selenic.com/repo/hg-stable – the stable repository, solely managed
  by mpm, contains official releases with safe and important fixes applied,
  always a subset of the main repository

Bugfixes are committed to the branch named stable and pushed to the main
repository.

This branch is automatically pushed to hg-stable to provide a separate
repository.

No new features are going to the stable branch, mainline (the default branch)
will be branched again near each release.


Links
=====

.. seealso::

   - http://doc.fedora-fr.org/wiki/Gestion_et_contr%C3%B4le_de_versions_avec_Mercurial


Other infos
===========


.. toctree::
   :maxdepth: 3

   commands/index
   extensions/index
   dev/index
   git/index
   guides/index
   hgrc/index
   hgignore/index
   news/index
   tips/index
   tools/index
   use_case/index
   web_hosting/index


