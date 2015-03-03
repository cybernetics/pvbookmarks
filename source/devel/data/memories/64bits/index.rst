

.. index::
   pair: Data ; 64 bits
   ! 64 bits


.. _64bits:

==================
64 bits
==================

.. seealso::

   - http://fr.wikipedia.org/wiki/64_bits

.. contents::
   :depth: 3


Introduction
============

Un processeur 64 bits est un processeur dont la largeur des registres est de 64
bits sur les nombres entiers.

Inconvénients
=============

Le passage de 32 bits à 64 bits augmente la consommation de mémoire. En effet,
les entiers et les adresses passent de 32 bits (4 octets) à 64 bits (8 octets).

Il faut donc deux fois plus d'octets pour les représenter. Attention, cela ne
veut pas du tout dire qu'un programme consommant 256 MB en 32 bits consommera
automatiquement 512 MB en 64 bits.

Il consommera un peu plus de mémoire, mais pas nécessairement le double.






