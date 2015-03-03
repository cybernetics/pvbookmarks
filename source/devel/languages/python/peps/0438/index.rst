
.. index::
   pair: PEP; 0438
   ! PyPI

.. _python_pep_0438:
.. _python_pep_438:

============================================================================
pep 0438 Transitioning to release-file hosting on PyPI
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0438/


.. contents::
   :depth: 3


Abstract
========

This PEP proposes a backward-compatible two-phase transition process to speed up, 
simplify and robustify installing from the pypi.python.org (PyPI) package index. 

To ease the transition and minimize client-side friction, no changes to distutils 
or existing installation tools are required in order to benefit from the first 
transition phase, which will result in faster, more reliable installs for most 
existing packages.

The first transition phase implements easy and explicit means for a package 
maintainer to control which release file links are served to present-day 
installation tools. 

The first phase also includes the implementation of analysis tools for 
present-day packages, to support communication with package maintainers and 
the automated setting of default modes for controlling release file links. 

The first phase also will default newly-registered projects on PyPI to only 
serve links to release files which were uploaded to PyPI.

The second transition phase concerns end-user installation tools, which shall 
default to only install release files that are hosted on PyPI and tell the user 
if external release files exist, offering a choice to automatically use those 
external files. 

External release files shall in the future be registered together with a 
checksum hash so that installation tools can verify the integrity of the 
eventual download (PyPI-hosted release files always carry such a checksum).

Alternative PyPI server implementations should implement the new simple index 
serving behaviour of transition phase 1 to avoid installation tools treating 
their release links as external ones in phase 2.

