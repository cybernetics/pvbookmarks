

.. index::
   pair: Data ; Memories


.. _memories:

==================
Memories
==================

.. seealso::

   - :ref:`data_alignment`

.. contents::
   :depth: 3

Introduction
============


En informatique, un mot est l’unité de base manipulée par un microprocesseur.

La taille d’un mot s’exprime en bits ou en octets, et est souvent utilisée pour
classer les microprocesseurs (32 bits, 64 bits…).

Toutes choses égales par ailleurs, un microprocesseur est d’autant plus rapide
que ses mots sont longs, car les données qu’il traite à chaque cycle sont plus
importantes.

Sur les microprocesseurs qui peuvent manipuler différentes tailles de données,
la taille des mots est choisie arbitrairement, dans le but d’avoir une convention
de nommage (en particulier, les instructions dont le mnémonique ne contient pas
d’indication explicite de taille s’appliquent à des mots).

On prend généralement la taille des principaux registres de données, ou la
taille du bus de données.

Les ordinateurs modernes ou processeurs modernes utilisent généralement des
données de 8, 16, 32 ou 64 bits, bien que d'autres tailles soient possibles.

La nomenclature actuelle est comme suit :

- donnée de 8 bits : « byte » ou «octet» ;
- donnée de 4 bits : « niblle » ou «quartet» ;
- donnée de 16 bits : « word » ou «mot», parfois «seize » ;
- donnée de 32 bits : « dword » ou « double mot, parfois (rarement) « trente-deuzet » ;
- donnée de 64 bits : « qword » ou « quadruple mot ».


Différentes tailles mémoires
=============================

.. toctree::
   :maxdepth: 4

   1bit/index
   4bits/index
   8bits/index
   16bits/index
   32bits/index
   64bits/index
   128bits/index
   tools/index


