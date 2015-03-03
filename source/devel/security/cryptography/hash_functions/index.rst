

.. index::
   pair: hash ; functions

.. _hash_functions:

======================
Hash functions
======================


.. seealso::

   - http://fr.wikipedia.org/wiki/Fonction_de_hachage
   - http://en.wikipedia.org/wiki/Hash_function


.. contents::
   :depth: 3

Definitions
===========


English
-------

A hash function is any algorithm or subroutine that maps large data sets of
variable length, called keys, to smaller data sets of a fixed length.

For example, a person's name, having a variable length, could be hashed to a
single integer.

The values returned by a hash function are called hash values, hash codes,
hash sums, checksums or simply hashes.


Français
---------

On nomme fonction de hachage une fonction particulière qui, à partir d'une donnée
fournie en entrée, calcule une empreinte servant à identifier rapidement, bien
qu'incomplètement, la donnée initiale.

Les fonctions de hachage sont utilisées en informatique et en cryptographie.


Terminologie
=============

Le résultat d'une fonction de hachage peut être appelé selon le contexte:

- somme de contrôle,
- empreinte,
- hash,
- résumé de message,
- condensé
- condensat
- ou encore empreinte cryptographique lorsque l'on utilise une fonction de hachage
  cryptographique.

Il ne faut toutefois pas confondre une fonction de hachage avec une signature
numérique qui fournit, en plus du code de hachage, une information sur l'identité
de l'émetteur du message.


SHA3
=======

.. toctree::
   :maxdepth: 4

   sha3


SHA256
=======

.. toctree::
   :maxdepth: 4

   sha256



CRC
=======

.. toctree::
   :maxdepth: 4

   crc/index


Tools
=====

.. toctree::
   :maxdepth: 4

   tools/index
   
   



