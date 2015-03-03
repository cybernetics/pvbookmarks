
.. index::
   pair: sphinx; robin Doxygen
   pair: sphinx; mongodb


.. _integrate_doxygen_with_robin:

============================================================
Robin : bridge between doxygen (XML) and sphinx via mongodb
============================================================

.. seealso::

   - https://bitbucket.org/reima/robin
   - :ref:`mongodb_database`

.. contents::
   :depth: 3


.. warning:: marche sur l'exemple fourni mais pas avec mes projets :)


Robin
=====

We're happy to announce robin, a new Doxygen/C++ to Sphinx bridge.

Robin provides an easy-to-use, easy-to-hack integration of Doxygen documentation
into Sphinx.

Robin is licensed under the BSD and can be found at Bitbucket: https://bitbucket.org/reima/robin


Features
========

- Robust extraction of Doxygen XML data via an easy-to-hack parser
- Intermediate data is stored in a database (mongodb) for simple extraction
  and processing
- Directive-driven output; each directive provides callbacks and hooks which
  allows for deep customization
- Automated generation of driver ReST documents:
  Similar to automodule; however, robin generates actual ReST documents which
  can be inspected

Prerequisites
=============

Robin expects a running mongodb on the local host.

It uses a minimal set of external libraries: Pymongo, sphinx, progressbar.

All of the dependencies can be easily installed using pip or easy_install.


Robin has been developed with Python 2.7; we have not tested previous versions.

Getting started
===============

- Run Doxygen to generate XML documentation (GENERATE_XML=YES)
- Run extract-doxygen <path to XML> <project name>
- Run create-rst <project name>
  This generates several directories (classes, groups, etc.)
  Include the groups.rst into your toc
- Add 'robin.sphinx' to the Sphinx extensions
- Build (make html) for TOC update
- Build again (make clean && make html)

Status
=======

We're using robin internally for a large C++ codebase, and there are a few
minor issues left that we hope to resolve soon (all of them are tracked on
Bitbucket.)

After that, we expect that robin will go into "maintenance" mode focusing on
bug fixes only.

If someone is interested in contributing, please get in touch with us.

Cheers, the robin developers




