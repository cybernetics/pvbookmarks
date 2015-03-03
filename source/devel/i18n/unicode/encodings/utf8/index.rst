

.. index::
   pair: UTF-8 ; encoding
   pair: "€"  ; 8365ème caractère du répertoire Unicode
   pair: "€"  ; 3 octets : 0xE2, 0x82, 0xAC
   pair: "€"  ; point de code est donc 8364

.. _utf8:

======================================
UTF8  UCS transformation format 8 bits
======================================

.. seealso:: http://fr.wikipedia.org/wiki/UTF-8


.. contents::
   :depth: 3


Introduction
============

UTF-8 (UCS transformation format 8 bits) est un moyen de coder les caractères
Unicode sous forme de séquences de un à quatre octets.

La norme Unicode définit entre autres un ensemble (ou répertoire) de caractères.
Chaque caractère est repéré dans cet ensemble par un index entier aussi appelé
« point de code ».

Par exemple le caractère "€" (euro) est le 8365ème caractère du répertoire
Unicode, son index, ou point de code est donc 8364 (on commence à compter à
partir de 0).

Le répertoire Unicode peut contenir plus d'un million de caractères, les points
de code sont compris entre 0 et 0x10FFFF ce qui est bien trop grand pour tenir
dans un seul octet (limité à des valeurs entre 0 et 255).

La norme Unicode définit donc des méthodes standardisées pour coder et stocker
cet index sous forme de séquence d'octets : UTF-8 est l'une d'entre elles, avec
UTF-16, UTF32 et leurs différentes variantes.

La principale caractéristique d'UTF-8 est qu'elle est rétro-compatible avec la
norme ASCII, c'est-à-dire que tout caractère ASCII se code en UTF-8 sous forme
d'un unique octet, identique au code ASCII.

Par exemple ``A`` (A majuscule) a pour code ASCII 65 et se code en UTF-8 par
l'octet 65.

Chaque caractère dont le point de code est supérieur à 127 (caractère non ASCII)
se code sur 2 à 4 octets.

Le caractère "€" (euro) se code par exemple sur 3 octets : 0xE2, 0x82, 0xAC
(ou 226, 130, 172 en déc





