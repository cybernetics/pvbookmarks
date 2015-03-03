
.. index::
   pair: Certificat ; Electronique
   pair: Certificat; EV
   ! Certificat électronique


.. _certificat:

===============================
Certificat électronique
===============================


.. seealso::

   - https://fr.wikipedia.org/wiki/Certificat_%C3%A9lectronique

.. contents::
   :depth: 3


Définition 1
=============

Un ``certificat électronique`` (aussi appelé certificat numérique ou certificat de 
clé publique) peut être vu comme une **carte d'identité numérique**. 

Il est utilisé principalement pour:

- **identifier** une entité physique ou morale, 
- mais aussi pour **chiffrer** des échanges.

Il est signé par un tiers de confiance qui atteste du lien entre l'identité 
physique et l'entité numérique (Virtuel).

Le standard le plus utilisé pour la création des certificats numériques est le 
X.509_.

.. _X.509:  https://fr.wikipedia.org/wiki/X.509


Définition 2
=============

.. seealso::

   - :ref:`pki_definition`

Un **certificat électronique** est un ensemble de données contenant :

- au moins une clé publique ;
- des informations d'identification, par exemple : noms, localisation, E-mails ;
- au moins une signature ; de fait quand il n'y en a qu'une, l'entité signataire 
  est la seule autorité permettant de prêter confiance (ou non) à l'exactitude 
  des informations du certificat.

Les certificats électroniques et leurs cycles de vie (cf. Certificate Revocation List, 
Protocole de vérification en ligne de certificat) peuvent-être gérés au sein 
d'`infrastructures à clés publiques`_.


.. _`infrastructures à clés publiques`:  https://fr.wikipedia.org/wiki/Infrastructure_%C3%A0_cl%C3%A9s_publiques

Différents types
================

Les certificats électroniques respectent des standards spécifiant leur contenu 
de façon rigoureuse. 

Les deux formats les plus utilisés aujourd'hui sont :

- X.509 dont plusieurs RFC définissent les propriétés et usages 
- OpenPGP, défini dans la RFC 4880

La différence notable entre ces deux formats est qu'un certificat X509 ne peut 
contenir qu'un seul identifiant, que cet identifiant doit contenir de nombreux 
champs prédéfinis, et ne peut être signé que par une seule autorité de certification. 

Un certificat OpenPGP peut contenir plusieurs identifiants, lesquels autorisent 
une certaine souplesse sur leur contenu, et peuvent être signés par une multitude 
d'autres certificats OpenPGP. Ce qui permet alors de construire des toiles de confiance.


Utilité
=========

Les certificats électroniques sont utilisés dans différentes applications 
informatiques dans le cadre de la sécurité des systèmes d'information pour 
garantir :

- la non-répudiation et l'intégrité des données avec la signature numérique 
- la confidentialité des données grâce au **chiffrement** des données 
- l'authentification ou l'authentification forte d'un individu ou d'une 
  identité non-physique


Certificats et navigation Internet
==================================

.. toctree::
   :maxdepth: 3
   
   certificat_openpgp
   certificat_x509


Tiers de confiance
===================

.. toctree::
   :maxdepth: 3
   
   tiers_de_confiance/tiers_de_confiance
   
   
