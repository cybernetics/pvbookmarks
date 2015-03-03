

.. index::
   pair: Versions (3.0); Tortoisehg


.. _tortoisehg_3.0:

=============================
TortoiseHg 3.0 (6 mai 2014)
=============================

.. seealso::

   - https://bitbucket.org/tortoisehg/thg/wiki/ReleaseNotes#!tortoisehg-30


.. contents::
   :depth: 3
   
   
Description
============

TortoiseHg 3.0 is a timed feature release. With 3.0, TortoiseHg is synchronizing 
its release numbers with Mercurial. 

The Windows installers for 3.0 come with a patched version of Mercurial 3.0; 
we've taken the first three stable commits following the 3.0 tag in order to 
fix a file permission regression.


Installer
==========

- bundle hg-git and hgsubversion extensions
- dulwich 0.9.6 (inclues fixes for GitHub, #3653)
- keyring 3.7 and hgkeyring 0.6.2 
