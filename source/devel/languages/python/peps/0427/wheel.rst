
.. index::
   pair: PEP 0427; Wheel

.. _wheel_0427:

=================
wheel ( PEP 0427)
=================

.. seealso::

   - https://bitbucket.org/dholth/wheel/
   - http://wheel.rtfd.org/
   - :ref:`python_pep_0427`
   - :ref:`python_pep_0376`
   - :ref:`wheel`


.. contents::
   :depth: 3

Introduction
============

A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension.

It is designed to contain all the files for a :ref:`PEP 376 <python_pep_0376>` compatible install in a
way that is very close to the on-disk format.

Many packages will be properly installed with only the "Unpack" step (simply
extracting the file onto sys.path), and the unpacked archive preserves enough
information to "Spread" (copy data and scripts to their final locations)
at any later time.

The wheel project provides a bdist_wheel command for setuptools
(requires distribute >= 0.6.28).

Wheel files can be installed with a patched pip from https://github.com/qwcode/pip
or with wheel's own command line utility.

The wheel documentation is at http://wheel.rtfd.org/.

The file format is documented in the draft PEP 427 (http://www.python.org/dev/peps/pep-0427/).


Comparison with eggs
====================

If you’ve made it this far you probably wonder whether I’ve heard of eggs. 

Some comparisons:

- **Wheel is an installation format; egg is importable**.
- Wheel archives do not need to include .pyc and are less tied to a specific
  Python version or implementation.
- Wheel can install (pure Python) packages built with previous versions of
  Python so you don’t always have to wait for the packager to catch up.
- Wheel uses .dist-info directories; egg uses .egg-info.
- Wheel is compatible with the new world of Python packaging and the new concepts
  it brings.
- Wheel has a richer file naming convention for today’s multi-implementation world.
  A single wheel archive can indicate its compatibility with a number of Python
  language versions and implementations, ABIs, and system architectures.
  Historically the ABI has been specific to a CPython release, but when we get a
  longer-term ABI, wheel will be ready.
- Wheel is lossless. The first wheel implementation bdist_wheel always generates
  egg-info, and then converts it to a .whl. Later tools will allow for the
  conversion of existing eggs and bdist_wininst distributions.
- Wheel is versioned. Every wheel file contains the version of the wheel
  specification and the implementation that packaged it.
  Hopefully the next migration can simply be to Wheel 2.0.


Videos
======

Vidéos en français
-------------------

.. seealso::

   - http://www.canalc2.tv/video.asp?idVideo=12325&voir=oui


