



.. _setuptools_0.7.b1:

===================================
Setuptools 0.7.b1
===================================


.. contents::
   :depth: 3


Announce
========

::

    de:	 Jason R. Coombs <jaraco@jaraco.com>
    à:	 "pypa-dev@googlegroups.com" <pypa-dev@googlegroups.com>
    date:	 14 mai 2013 13:49
    objet:	 Setuptools 0.7b1 available for review

I’m excited to announce that the Setuptools/Distribute merge is drawing 
to a close. 

I’ve completed the merge and PJE has completed his review and signed off on the merge.


I’ve published the merged code to https://bitbucket.org/pypa/setuptools.
This repo includes several branches:

distribute
----------

A copy of Distribute, rebased onto the setuptools history. 
This will be where subsequent Distribute releases (if any) are made.

 

setuptools
-----------

The previous trunk of setuptools SVN repo.

setuptools-0.6
---------------

The previous 0.6 branch of the setuptools SVN repo and source of recent 
development against 0.6c11.

 

“Setuptools-Distribute merge”
------------------------------

The branch where the merge was actuated. It includes a file MERGE.txt 
describing the process used (mostly for posterity).

 
default
--------

Based on the merge branch, and additionally merged with later changes 
from setuptools-0.6 and distribute, this branch represents the active 
development and contains the tagged 0.7b1 release.

I’ve uploaded the 0.7b1 release to the downloads section of the project. 

This limited-release of setuptools is intended for PYPA developers and 
other enthusiasts interested in testing and vetting the merged code 
before it goes public on PyPI.

I’m running setuptools 0.7b1 on my personal workstation now, and I 
encourage you to do the same. I’m particularly interested in feedback 
from buildout and other users of setuptools.

If you encounter any issues, please feel free to file them with the new 
project, especially if they’re new, blocking issues. 

Once everyone has had a chance to test and review, I’ll plan to make a 
final release to PyPI. 

Before I do that, I’ll need to update the release.py script, as it assumes 
the same versioning scheme used by distribute (0.6.x for everything).

The next steps will be deliberate and possibly slow to ease the transition 
for everyone involved. 

Thanks for your patience. I look forward to your feedback.






