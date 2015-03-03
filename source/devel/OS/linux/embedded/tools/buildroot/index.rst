
.. index::
   pair: Linux; Buildroot
   pair: Buildroot ; Source code
   ! Buildroot


.. _buildroot_linux_tool:
.. _buildroot:

=================================================
Buildroot linux tool (Making Embedded Linux easy)
=================================================

.. seealso::

   - http://buildroot.uclibc.org/
   - https://github.com/mbats/eclipse-buildroot-toolchain-plugin


.. figure:: logo_buildroot.png
   :align: center

   *Builroot logo*


.. contents::
   :depth: 3


Introduction
============

Buildroot is a set of Makefiles and patches that makes it easy to generate a
complete **embedded Linux system**.

Buildroot can generate any or all of a cross-compilation toolchain,
a root filesystem, a kernel image and a bootloader image.

Buildroot is useful mainly for people working with small or embedded systems,
using various CPU architectures (x86, ARM, MIPS, PowerPC, etc.) : it automates
the building process of your embedded system and eases the cross-compilation process.


Buildroot source code
=====================

.. seealso::

   - http://git.buildroot.net/buildroot/tree/docs



Features
========

The major Buildroot features are:

- Can handle everything in your embedded system development project:
  cross-compiling toolchain, root filesystem generation, kernel image compilation
  and bootloader compilation.
  Buildroot is also sufficiently flexible that it can also be used for only one
  or several of these steps.
- Is very easy to set up, thanks to its menuconfig, gconfig and xconfig
  configuration interfaces, familiar to all embedded Linux developers.
  Building a basic embedded Linux system with Buildroot typically takes 15-30 minutes.
- Supports several hundreds of packages for userspace applications and libraries:
  X.org stack, Gtk2, Qt, DirectFB, SDL, GStreamer and a large number of
  network-related and system-related utilities and libraries are supported.
- Supports multiple filesystem types for the root filesystem image: JFFS2, UBIFS,
  tarballs, romfs, cramfs, squashfs and more.
- Can generate an uClibc cross-compilation toolchain, or re-use your existing
  glibc, eglibc or uClibc cross-compilation toolchain
- Has a simple structure that makes it easy to understand and extend.
  It relies only on the well-known Makefile language.

Buildroot is maintained by Peter Korsgaard, and licensed under the GNU GENERAL
PUBLIC LICENSE V2 (Or later).

Stable releases are delivered every three months.


Communications
===============

:Mailing list:  http://buildroot.net/lists.html

Versions
========

.. toctree::
   :maxdepth: 4

   versions/index


Buildroot conferences
=====================

.. toctree::
   :maxdepth: 4

   conferences/index

Buildroot People
================

.. toctree::
   :maxdepth: 4

   people/index


Buildroot news
==============

.. toctree::
   :maxdepth: 4

   news/index


