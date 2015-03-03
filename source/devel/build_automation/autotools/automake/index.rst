


.. index::
   pair: Autotools; Automake
   ! Automake


.. _automake:

==========
Automake
==========


.. seealso::

   - http://fr.wikipedia.org/wiki/Automake
   - http://www.gnu.org/software/automake/
   - https://lists.gnu.org/mailman/listinfo/automake/

.. contents::
   :depth: 3

Introduction
============

GNU Automake est un logiciel générant des makefiles portables qui peuvent 
être utilisés par make pour compiler des programmes. 

C'est un logiciel libre développé et maintenu par le projet GNU et 
utilisé dans le processus de compilation du système GNU. 

Les makefiles produits se conforment aux normes de programmation de GNU.

Automake est écrit en Perl et doit être utilisé avec Autoconf, un autre 
outil GNU. 

Il contient les commandes suivantes:

- aclocal
- automake

Automake peut présenter des difficultés à cause du fait que les versions 
récentes ne sont pas compatibles avec les plus anciennes. 

Par exemple, un projet créé avec Automake 1.4 ne fonctionnera pas avec 
Automake 1.9.


Introduction to Automake
========================

Automake is a tool for automatically generating 'Makefile.in' files 
compliant with the GNU Coding Standards. 

Automake requires the use of :ref:`Autoconf <autoconf>`. 

Automake source code
=====================

.. seealso:: 

   - http://savannah.gnu.org/git/?group=automake

::

    git clone git://git.savannah.gnu.org/automake.git


