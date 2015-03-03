
.. index::
   pair: Autorités ; Certification
   ! Autorités de certification
   ! AC


.. _autorites_certification:

===============================
Autorités de Certification (AC)
===============================


.. seealso::


   - https://fr.wikipedia.org/wiki/Autorit%C3%A9_de_certification
   - https://en.wikipedia.org/wiki/Certificate_authority
   - https://cabforum.org/


Définition 1
============

En cryptographie, l'autorité de certification (AC ou CA) a pour mission, après 
vérification de l'identité du demandeur du certificat par une autorité 
d'enregistrement, de signer, émettre et maintenir

- les certificats (CSR : Certificate Signing Request)
- les listes de révocation (CRL : Certificate Revocation List)

L'autorité de certification (AC) opère elle-même ou peut déléguer l'hébergement 
de la clé privée du certificat à un opérateur de certification (OC) ou autorité 
de dépôt. L'AC contrôle et audite l'opérateur de certification sur la base des 
procédures établies dans la Déclaration des Pratiques de Certification. 

L'AC est accréditée par une autorité de gestion de la politique qui lui permet 
d'utiliser un certificat renforcé utilisé par l'OC pour signer la clé publique 
selon le principe de la signature numérique. 

Sur le plan technique, cette infrastructure de gestion des clés permet ainsi d'assurer que

- les données transmises n'ont pas été modifiées durant le transfert : intégrité 
  par hachage des données
- les données proviennent bien de l'émetteur connu : utilisation de clés et répudiation


Définition 2
============

Une CA, c’est avant tout une société qui met en oeuvre une PKI (pour Public Key Infrastructure), 
une Infrastructure à Clé Publique (ICP), c’est-à-dire un ensemble de logiciels 
permettant de:

- conserver une clé privée, 
- de diffuser sa clé publique, 
- et à l’aide de sa clé privée, signer des certificats ayant certains attributs, en 
  respectant un protocole précis et documenté publiquement, nommé la 
  CPS (Certificate Practice Statement), généralement diffusé en PDF sur son site 
  (par exemple, celle de Verisign à l’adresse https://www.verisign.com/repository/CPS/).


Liste des autorités de certification
=====================================

.. toctree::
   :maxdepth: 3
   
   lets_encrypt/lets_encrypt
   
   
   

