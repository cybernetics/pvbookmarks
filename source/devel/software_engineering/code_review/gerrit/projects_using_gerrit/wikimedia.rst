

.. index::
   pair: Gerrit; Wikimedia


.. _wikimedia_gerrit:

==================
Wikimedia  gerrit
==================

.. seealso::

   - https://gerrit.wikimedia.org
   - :ref:`wikimedia`



Reports
=======

.. seealso::

   - https://www.mediawiki.org/wiki/Gerrit/Reports#Reports
   - https://github.com/mzmcbride/gerrit-reports


Gerrit's interface can be difficult to navigate for those new to the tool.

The following documentation can help newcomers learn how to navigate Gerrit.

To view all projects in gerrit, go to Projects > List.

Clicking a project name in that list doesn't give you much useful information,
but then you can go to Project > Branches and click the gitweb link for the
"master" branch.

In gitweb then click the " | tree" link at the top of the list of commits to
actually see WTF is in the project.

Clicking the "blob" or "raw" link next to a file name will finally show you some code.

The core MediaWiki source code is in project "mediawiki/core"_, browse away.

In general you want to view the HEAD or master branch. If you want to look at
the code for the version of MediaWiki or an extension deployed on some wiki,
visit that wiki's Special:Version page and look for a corresponding branch or commit.


.. _"mediawiki/core": https://gerrit.wikimedia.org/r/gitweb?p=mediawiki/core.git;a=tree;h=HEAD;hb=HEAD
