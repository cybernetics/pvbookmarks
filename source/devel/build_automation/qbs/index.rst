

.. index::
   pair: building tool ; qbs
   pair: Qt ; qbs

.. _qbs_building_tool:

============================
Qt Build Suite (Qbs), Cubes
============================

.. seealso::

   - https://qt-project.org/wiki/qbs
   - http://gamesfromwithin.com/the-quest-for-the-perfect-build-system


.. contents::
   :depth: 3


Introducing qbs
===============


Over the years we have developed a kind of a love-hate relationship towards
qmake.
It does its job but also has its quirks and is widely considered unmaintainable.

The blog post [TMQB_] contains a wish list for a qmake replacement. We have
considered the various tools on the market, but none satisfied us – see for
example [WNCM].

So some time ago we have initiated an internal project to try some of the ideas.

This is the outcome of it: the Qt Build Suite, aka qbs (pronounced as “Cubes”).


.. _TMQB: http://labs.qt.nokia.com/2009/10/12/to-make-or-not-to-make-qmake-and-beyond/
.. _WNCM: http://lists.qt.nokia.com/pipermail/qt5-feedback/2011-June/000494.html

It is not qmake
===============

Unlike qmake, qbs is not tied to the Qt version, and it generates a proper
build graph (dependency graph) from the high-level project description in the
project file.

Also, classical makefile generators like qmake and CMake create makefiles and
leave the execution of the actual build commands to tools like make or ninja.

Qbs on the other hand fills the role of a parallel make and directly calls the
compiler, linker and other tools, pretty much like SCons and Ant do.


qbs source code
===============

The source code repository is hosted at qt-project.org [qt-project.org] and
mirrored on gitorious [qt.gitorious.org]::

    git clone git://gitorious.org/qt-labs/qbs.git

To build qbs simply do::

    qmake -r
    make

in the source directory.


Contributions
=============


If you want to contribute code, you can do so by using your Qt Project gerrit
account [wiki.qt-project.org]::

    git clone git://gitorious.org/qt-labs/qbs.git
    git remote add gerrit <gerrit-username>@codereview.qt-project.org:qt-labs/qbs
    ... hack hack hack ...
    git push gerrit HEAD:refs/for/master


Happy Hacking!


qbs news
========

.. toctree::
   :maxdepth: 3

   news/index



