
.. index::
   pair: Signature ; Numérique
   pair: Signature ; Electronique
   ! Signature électronique
   ! Signature numérique
   ! Digital signature


.. _signature_numerique:

=================================================================
Signature numérique, signature électronique, (Digital signature)
=================================================================


.. seealso::

   - https://fr.wikipedia.org/wiki/Signature_num%C3%A9rique
   - https://en.wikipedia.org/wiki/Digital_signature

.. contents::
   :depth: 3


Définition 1
=============

La signature numérique (parfois appelée signature électronique) est un mécanisme 
permettant de garantir l'intégrité d'un document électronique et d'en authentifier 
l'auteur, par analogie avec la signature manuscrite d'un document papier.

Elle se différencie de la signature écrite par le fait qu'elle n'est pas visuelle, 
mais correspond à une suite de nombres.


Fonctions de la signature
==========================

Un mécanisme de signature numérique doit présenter les propriétés suivantes :

- Il doit permettre au lecteur d'un document d'identifier la personne ou 
  l'organisme qui a apposé sa signature.
- Il doit garantir que le document n'a pas été altéré entre l'instant où 
  l'auteur l'a signé et le moment où le lecteur le consulte.

Pour cela, les conditions suivantes doivent être réunies:

- Authentique : L'identité du signataire doit pouvoir être retrouvée de manière 
  certaine.
- Infalsifiable : La signature ne peut pas être falsifiée. Quelqu'un ne peut se 
  faire passer pour un autre.
- Non réutilisable : La signature n'est pas réutilisable. Elle fait partie du 
  document signé et ne peut être déplacée sur un autre document.
- Inaltérable : Un document signé est inaltérable. Une fois qu'il est signé, 
  on ne peut plus le modifier.
- Irrévocable : La personne qui a signé ne peut le nier.

En pratique, l'essentiel des procédures de signature électronique existantes 
s’appuie sur la cryptographie asymétrique, dans le reste de l'article nous nous 
placerons dans ce cas le plus courant.


Signature numérique des logiciels
==================================

.. toctree::
   :maxdepth: 3
   
   des_logiciels/index
   

Tutoriaux
==========

.. toctree::
   :maxdepth: 3
   
   tutoriaux/index
   
   

