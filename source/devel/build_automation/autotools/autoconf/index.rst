


.. index::
   ! Autoconf
   pair: Autotools; Autoconf
   pair: Compilation; GNU
   ! Autoconf



.. _autoconf:

==========
Autoconf
==========


.. seealso::

   - http://fr.wikipedia.org/wiki/Autoconf
   - http://www.gnu.org/software/autoconf/
   - :ref:`make`

.. contents::
   :depth: 3

Introduction
============

GNU Autoconf est un logiciel servant à produire des scripts shell qui
configurent automatiquement le code source d'un logiciel pour l'adapter
à divers systèmes d'exploitation de type Unix.

Les scripts produits par Autoconf sont indépendants de cet outil quand
ils s'exécutent, de sorte que les usagers de ces scripts n'ont pas besoin
d'avoir Autoconf.

Avec GNU Automake et GNU Libtool, Autoconf forme le système de compilation
de GNU.

Autoconf utilise le préprocesseur GNU m4 pour transformer un fichier
« configure.ac » (ou « configure.in » anciennement) en un script shell
portable nommé « configure ».

Le script « configure » exécute de façon non interactive et génère des
en-têtes adaptés et des makefiles dérivés de modèles préétablis.

**On peut considérer qu'Autoconf compile un programme m4 vers un
script shell**.

Introduction to Autoconf
========================

Autoconf is an extensible package of M4 macros that produce shell
scripts to automatically configure software source code packages.

These scripts can adapt the packages to many kinds of UNIX-like systems
without manual user intervention.

Autoconf creates a configuration script for a package from a template
file that lists the operating system features that the package can use,
in the form of M4 macro calls.

Producing configuration scripts using Autoconf requires GNU M4.

You should install GNU M4 (at least version 1.4.6, although 1.4.13 or
later is recommended) before configuring Autoconf, so that Autoconf's
configure script can find it.

The configuration scripts produced by Autoconf are self-contained, so
their users do not need to have Autoconf (or GNU M4).


Autogen source code
===================

.. seealso::

   - http://git.savannah.gnu.org/gitweb/?p=autoconf.git

::

    git clone git://git.sv.gnu.org/autoconf


