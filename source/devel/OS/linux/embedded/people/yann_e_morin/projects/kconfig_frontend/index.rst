
.. index::
   pair: kconfig ; Frontend


.. _kconfig_frontend:

================
kconfig-frontend
================


.. seealso::

   - http://ymorin.is-a-geek.org/hg/kconfig-frontends
   - :ref:`kconfig`
   - :ref:`autotools`


.. contents::
   :depth: 3

Introduction
=============

The configuration language used by the Linux kernel, known as :ref:`kconfig <kconfig>`, has gained
some traction in the community, due to its advantages:

- simple syntax and grammar
- limited, yet adequate, option types: boolean and tristates, integers and strings
- simple, yet efficient, organisation of options: indentation, sub-menus, radio-like choices
- direct and reverse dependencies
- L10n possible (although not much used in real life)

The kconfig language is increasingly used by third-party projects, to name a few
of those I know of:

- buildroot, busybox, uClibc
- crosstool-NG
- openWRT
- PTXdist
- and many others...

Up until now, when any such project wanted to use the kconfig language as their
own configuration infrastructure, the usage was to copy-paste the code from any
random Linux kernel snapshot (preferrably a dot-0 release) into the project's
sources, and adapt the build system inherited from the Linux kernel to the project's own build system.

Although this has more-or-less been working so far, this has a few drawbacks:

- not two projects based their copy from the same Linux kernel snapshot, so the
  behavior of kconfig can vary from project to project
- whenever a bug is fixed in, or a new feature added to, the kconfig language
  and/or frontends, all projects must update their local copy
- not all projects even upgrade their local copy, and some even did not update
  since their initial import of kconfig
- some projects maintain their own set of bug-fixes and/or enhancements to their
  local copy, rather than contributing them back upstream

The kconfig-frontends package
=============================

This project aims at centralising the effort of keeping an up-to-date, out of
the Linux source tree, packaging of the kconfig infrastructure, ready for use
by third party projects.

This package provides the kconfig parser, as well as all the frontends (all five
of them, as of 2012-03-19), packaged using the traditional autotools, so the
kconfig infrastructure is easy to deploy, either locally or system-wide.

This kconfig-frontends package does not aim at replacing the in-tree kconfig of
the linux kernel (at least in the foreseeable future!).

Any fix or feature must still be pushed upstream to the Linux tree before it
appears in this package.

Get the source !
=================

You can:

- get a released tarball: /download/kconfig-frontends
- browse the repository on-line: /hg/kconfig-frontends
- clone the repository: hg clone http://ymorin.is-a-geek.org/hg/kconfig-frontends

The version numbering of kconfig-frontends follows the linux version number,
followed by kconfig-frontends' own version digit.


