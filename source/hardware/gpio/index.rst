
.. index::
   pair: Hardware; GPIO
   ! GPIO

.. _gpio:

====================================
GPIO (General Purpose Input/Output)
====================================

.. seealso::

   - http://fr.wikipedia.org/wiki/GPIO
   - :ref:`cable_gpio`


.. contents::
   :depth: 3

Introduction
=============

Les ports GPIO (General Purpose Input/Output, c'est-à-dire entrée/sortie 
pour un usage général) sont des ports d'entrée/sortie très utilisés dans 
le monde des microcontrôleurs, en particulier dans le domaine de 
l'électronique embarquée. 

Selon la configuration, ces ports peuvent fonctionner aussi bien en entrée 
qu'en sortie.

Les périphériques GPIO comportent un ensemble de ports d'entrée/sortie 
qui peuvent être configurés pour jouer soit le rôle d'une entrée, soit 
le rôle d'une sortie.

Lorsqu'un port GPIO est configuré en tant que sortie, on peut écrire dans 
un registre interne afin de modifier l'état d'une sortie. 
Lorsqu'il est configuré en tant qu'entrée, on peut détecter son état en 
lisant le contenu d'un registre interne.

De plus, les périphériques GPIO peuvent produire des interruptions et 
des événements d'accès direct à la mémoire (EDMA).




