
.. index::
   pair: Réseau ; Confiance
   pair: Web ; Trust
   pair: Toile; Confiance
   pair: Réseau ; Confiance
   pair: Modèle de confiance ; Décentralisé
   ! Réseau de confiance
   ! Web of trust
   ! Toile de confiance


.. _reseau_de_confiance:
.. _reseaux_de_confiance:
.. _toile_de_confiance:
.. _web_of_trust:

=============================================
Réseau ou toile de confiance (Web of trust)
=============================================


.. seealso::

   - :ref:`gpg`
   - https://fr.wikipedia.org/wiki/Toile_de_confiance
   - https://fr.wikipedia.org/wiki/Key_signing_party
   - https://en.wikipedia.org/wiki/Web_of_trust

.. contents::
   :depth: 3


Définition
==========

En cryptographie, la **toile de confiance** est un concept utilisé par :ref:`PGP <pgp>`, :ref:`GnuPG <gnupg>`, 
ainsi que d'autres systèmes compatibles avec :ref:`OpenPGP <openpgp>`. 

La toile de confiance permet de vérifier la relation entre une clé publique 
et son possesseur.

C'est un modèle de confiance **décentralisé**, en alternative aux modèles de confiance 
centralisés de la plupart des autres PKI.

Contrairement aux modèles centralisés où la confiance que l'on peut prêter ne 
passe que par une autorité de certification (CA ou hiérarchie de CA) dont la 
plupart ne sait rien, une toile de confiance est relative à un individu qui 
peut choisir lui-même les tiers (en général d'autres personnes physiques) 
à qui il fait confiance.

De ce fait, il existe de nombreuses toiles de confiances indépendantes. 

N'importe qui peut en faire partie (via son propre certificat), et être un lien 
entre différentes toiles.

Le concept de toile de confiance a été élaboré initialement par Phil Zimmermann, 
créateur de PGP, en 1992, dans la version 2.0 du manuel de PGP.


Fonctionnement d'une toile de confiance
=======================================

Dans OpenPGP, les certificats d'identité sont vérifiés par la signature numérique 
d'autres utilisateurs. 

Ces utilisateurs, en signant ce certificat, peuvent renforcer (pour d'autres) 
l'association entre une clé publique et la personne ou l'entité désignée par ce 
certificat. 

Cette action est habituellement faite lors de `key signing parties`_.


.. _`key signing parties`:  https://fr.wikipedia.org/wiki/Key_signing_party

GNU Privacy Guard
==================

.. seealso::

   - :ref:`gpg`
   
   
   
