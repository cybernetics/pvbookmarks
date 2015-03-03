


.. index::
   pair: Autotools; Pkg-config
   pair: Pkg-config; 2003
   ! Pkg-config

.. _pkg-config:

==========
Pkg-config
==========


.. seealso::

   - https://fr.wikipedia.org/wiki/Pkg-config
   - http://www.unixgarden.com/index.php/gnu-linux-magazine/pkg-config-et-les-auto-tools

.. contents::
   :depth: 3

Introduction
============

pkg-config est un logiciel qui fournit une interface unifiée pour interroger les
bibliothèques installées lors de la compilation de code source qui utilise une
de ces bibliothèques.


Historique
===========

La première implémentation de cet outil a été développée en script shell (en) par
James Henstridge, et les premiers prototypes sont réalisés en septembre 2003.

En 2005, le programme est entièrement réécrit en langage C par Havoc Pennington.

Des versions bêta sont ainsi distribuées une fois par an, excepté en 2009,
jusqu'en mai 2011, date de la dernière réalisation.


.. _alternative_pkgconfig:

Alternative : le projet pkgconf
===============================

.. seealso::

   - :ref:`pkgconf`


``pkgconf`` est un programme développé indépendamment du projet pkg-config durant
l'été 2011 dans le but de le remplacer.

Comme toutes les implémentations du logiciel pkg-config, cet outil permet donc
de définir les options de compilation et de liaison.

Une option de compilation est une option envoyée à un compilateur pour lui dire
de faire autre chose que sa valeur par défaut.

Elles sont généralement écrites sous la forme d'un paramètre, et sont dans de
nombreux cas écrites en ligne de commande et envoyées au compilateur en tant
qu'arguments.

Les deux outils utilisent les scripts produits par autoconf pour automatiser la
configuration du code source. La vérification des dépendances des bibliothèques
logicielles est en grande partie assurée par le préprocesseur de macro m4, via la
macro d'autoconf PKG_CHECK_MODULES.

À la différence de pkg-config, ce programme ne dépend pas de la bibliothèque
logicielle GLib, alors que pkg-config nécessite GLib pour être compilé,
la bibliothèque Glib a aussi besoin de pkg-config pour compiler, ce qui provoque
une dépendance circulaire.

Heureusement depuis la version en développement pkg-config intègre sa propre
copie de GLib, ce qui permet de compiler pkg-config sans dépendance.


Caractéristiques techniques
============================

Il a été conçu à l'origine pour GNU/Linux, mais est aujourd'hui également
disponible pour divers systèmes BSD, pour Microsoft Windows, Mac OS X et Solaris.

``pkg-config`` fournit diverses informations au sujet des bibliothèques installées.

Ces informations peuvent comprendre :

- des paramètres pour un compilateur C ou C++
- des paramètres pour l'éditeur de liens
- la version de la bibliothèque en question
- indique la présence des bibliothèques installées ou pas avec un intervalle de
  version requis


Use of pkgconf{ig}
===================

.. toctree::
   :maxdepth: 3

   pkgconfxx_with_qt



