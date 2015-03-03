
.. index::
   pair: Distil; Packaging
   ! Distil

.. _distil:

=======================
Distil
=======================

.. seealso::

   - https://pythonhosted.org/distil/indexing.html
   - https://bitbucket.org/vinay.sajip/docs-distil/downloads/distil.py
   - :ref:`distlib`


.. contents::
   :depth: 3


.. warning:: distil is not intended to supplant any existing packaging tool, 
   but rather to act as a testbed for distlib and to explore useful areas in 
   packaging. 
   It should be used in virtual environments set up specifically for the purpose 
   of experimenting with it. Remember, it is alpha software.


Introduction
============

Welcome to the documentation for distil, an experimental packaging tool built 
on top of :ref:`distlib`. 

With distil, you can install, upgrade, uninstall, build, test and package 
Python distributions, whether pure-Python, or incorporating C libraries 
and extensions.


Overview
--------

.. seealso:: https://pythonhosted.org/distil/_sources/overview.txt

The ``distil`` tool is a testbed for ``distlib``, which is a low-level library
that implements basic packaging functionality, and is intended for use by
packaging tools.


Distil source code
==================

.. seealso::

   - https://bitbucket.org/vinay.sajip/docs-distil/downloads/distil.py



Why ``distil``?
===============

While maintainers of the `pip <http://pip-installer.org/>`_ project have
expressed an interest in the possibility of implementing some parts of ``pip``
functionality using ``distlib``, this is dependent on available volunteer time
and overall project priorities, and so no specific timescales for any adoption
of particular features of ``distlib`` can be expected. Of course, this also
applies to packaging tools other than ``pip``.

So, ``distil`` aims to fill the gap by providing a packaging tool, based only
on ``distlib`` and the Python standard library. If it is to demonstrate that
``distlib`` is useful for and usable by packaging tools, ``distil`` cannot be a
toy -- it must aim to provide a large part of the functionality of tools like
``pip``, and it must show, where possible, improvements over existing tools
that are possible through the use of ``distlib``.

.. note:: ``distil`` is not intended to supplant any existing packaging tool,
   but rather to act as a testbed for ``distlib`` and to explore useful areas
   in packaging. It should be used in virtual environments set up specifically
   for the purpose of experimenting with it. Remember, it is alpha software.

Features
========

The initial release of ``distil`` provides the following features:

* Install projects from PyPI and wheels
  (see :ref:`python_pep_0427`).
  Distil does not invoke ``setup.py``, so projects that do significant
  computation in ``setup.py`` may not be installable by ``distil``. 
  However, a large number of projects on PyPI *can* be installed, and 
  dependencies are detected, downloaded and installed.
* Optionally upgrade installed distributions, whether installed by ``distil``
  or installed by ``pip``.
* Uninstall distributions installed by ``distil`` or ``pip``.
* Build source distributions in ``.tar.gz``, ``.tar.bz2``, and ``.zip``
  formats.
* Build binary distributions in wheel format. These can be pure-Python, or
  have C libraries and extensions. Support for Cython and Fortran (using
  ``f2py``) is possible, though currently ``distil`` cannot install ``Cython``
  or ``Numpy`` because of how they use ``setup.py``. You can optionally use
  ``pip`` to build wheels, which can then be installed using ``distil``.
* Run tests on built distributions.
* Register projects on PyPI.
* Upload distributions to PyPI.
* Upload documentation to http://pythonhosted.org/ (formerly
  http://packages.python.org/).
* Very simple deployment -- just copy ``distil.py`` to a location on your path,
  optionally naming it to ``distil`` on POSIX platforms. There's no need to
  install ``distlib`` -- it's all included.
* Display dependencies of a distribution -- either as a list of what would be
  downloaded (and a suggested download order), or in Graphviz format suitable
  for conversion to an image.
* Uses either a system Python or one in a virtual environment, but by default
  installs to the user site rather than system Python library locations.
* Tab-completion of commands and parameters on Bash-compatible shells.

Logically, packaging activities can be divided into a number of categories or
roles:

* *Archiver* -- builds source distributions from a source tree

* *Builder* -- builds binary distributions from source

* *Installer* -- installs source or binary distributions

This version of ``distil`` incorporates (for convenience) all of the above
roles. There is a school of thought which says that that these roles should be
fulfilled by separate programs, and that's fine for production quality tools --
it's just more convenient for now to have everything in one package for an
experimental tool like ``distil``.


Actual Improvements
===================

Despite the fact that ``distil`` is in an alpha stage of development and has
received no real-world exposure like the existing go-to packaging tools, it
does offer some improvements over them:

* Dependency resolution can be performed without downloading any distributions.
  Unlike e.g. ``pip``, you are told of which additional dependencies will be
  downloaded and installed, before any download occurs.
* Better information is stored for uninstallation. This allows better feedback
  to be given to users during uninstallation.
* Dependency checking is done during uninstallation. Say you've installed a
  distribution A, which pulled in dependencies B and C.

  * If you request an uninstallation of B (or C), ``distil`` will complain that
    you can't do this because A needs it.
  * When you uninstall A, you are offered the option to uninstall B and C as
    well (assuming you didn't install something *else* that depends on B or C,
    after installing A).
* By default, installation is to the user site and not to the system Python,
  so you shouldn't need to invoke ``sudo`` to install distributions for
  personal use which are not for specific projects/virtual environments.
* There's no need to install ``distil`` -- the exact same script will run with
  any system Python or any venv (subject to Python version constraints of 2.6,
  2.7, 3.2 or greater). There's no need to have umpteen copies of
  ``setuptools``, ``distribute`` and ``pip`` lying about! Not that disk space
  is a particular constraint, of course.

Unlike the ``pysetup`` tool that is part of ``distutils2``, ``distil`` can
install many source distributions that are already on PyPI without the need to
migrate them to ``setup.cfg`` first (or the need to convert them to wheels).
This allows a more gradual transition to new packaging norms, by not requiring
root-and-branch conversion of existing distributions.

More "actual" improvements can be achieved, dependent on feedback from you!


Possible Improvements
=====================

In line with recent thinking in packaging, ``distlib`` and ``distil`` rely on
a declarative format for distribution metadata, as opposed to the *ad hoc* code
approach (i.e. ``setup.py``) taken by ``distutils``/``setuptools``/``distribute``. 

This offers a means for different packaging tools to interoperate because the 
declarative format is standardised, and this can lead to innovations in 
packaging and improved features for Python package developers and users. 

There should be no more "my way or the highway" in Python packaging, which the 
design of ``distutils`` has fostered.


Limitations
===========

As already mentioned above, ``distil`` is not a replacement for ``pip`` or
``easy_install``. The main reason why ``distil`` cannot do things that ``pip``
or ``easy_install`` can do is that some projects use code in ``setup.py`` to
do things like creating new files and moving files around before invoking the
actual setup code in ``distutils``/``setuptools``/``distribute``. Because
``distlib`` and ``distil`` are declarative and don't actually execute
``setup.py``, the code therein cannot be taken advantage of, and so ``distil``
can fail when trying to build or install such projects. However, Python
packaging standards are expected to provide a migration path such that such
code as currently lives in ``setup.py`` can be replaced by other mechanisms
which allow better interoperability between packaging tools.

Distil *can* use ``pip`` to build wheels, for those cases where ``setup.py``
*must* be executed for a correct build. This only exercises the wheel-building
functionality of ``distlib``, but is provided as a convenience when
experimenting with wheels.

There are other areas of functionality which ``distil`` does not aim to
provide, such as direct installation from VCS repositories. These *could* be
provided, but are only really appropriate in a production-quality packaging
tool. Note that ``distil`` and ``distlib`` are free of dependencies other than
the Python standard library, and are expected to remain so for the foreseeable
future. (Although ``distil`` provides an option to use ``pip``, it is not a
hard dependency, and ``distil`` is useful even without ``pip`` being
installed.)


News
========

.. toctree::
   :maxdepth: 3
   
   news/index

Versions
========

.. toctree::
   :maxdepth: 3
   
   versions/index
   
   
   


