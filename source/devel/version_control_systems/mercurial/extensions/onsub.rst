
.. index::
   pair: hg;  onsub extension

==========================
onsub Mercurial extensions
==========================


.. seealso::

   - http://mercurial.selenic.com/wiki/OnsubExtension
   - https://bitbucket.org/aragost/onsub/


**This extension is not distributed with Mercurial**

:Author: MartinGeisler
:Download site: https://bitbucket.org/aragost/onsub/


.. contents::
   :depth: 3


Overview
========

The onsub extension will traverse all subrepositories and execute a command
in each.

This can be used to update all subrepositories with one command::

    $ hg onsub "hg pull -u"


The extension provides a number of environment variables for you to use in your
commands:

- ``HG_REPO``: Absolute path to the top-level repository in which the onsub
  command was executed.
- ``HG_SUBPATH``: Relative path to the current subrepository from the top-level
  repository.
- ``HG_SUBURL``: URL for the current subrepository as specified in the containing
  repository's .hgsub file.
- ``HG_SUBSTATE``: State of the current subrepository as specified in the
  containing repository's .hgsubstate file.

Consult hg help onsub after enabling the extension for the full and up-to-date
documentation.

Configuration
=============

Configure your .hgrc to enable the extension by adding following lines:

::

    [extensions]
    onsub = path/to/onsub/onsub.py
