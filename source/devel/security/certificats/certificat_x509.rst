
.. index::
   pair: Certificat ; X509
   ! PKIX

.. _certificat_x509:

==================================
Certificats X509 PKI X509, (PKIX)
==================================

.. contents::
   :depth: 3
   

Introduction
============

Les certificats sont très largement utilisés sur les sites de e-commerce, 
webmails ou autres sites sensibles (banques, impôts, etc.) 

Plusieurs niveaux de chiffrement existent et plusieurs fonctionnalités associées 
rendent la compréhension des certificats complexe.

Certificats X.509 standards
========================----

Ce sont les certificats classiques, qui existent depuis plusieurs années. 

Le chiffrement varie entre 40 bits et 256 bits. Cela est dû en partie à la 
capacité des navigateurs et à la législation en vigueur. 

Généralement, les sociétés éditrices de certificats proposent 40 bits ou 
128 bits garantis.

Certificats X.509 étendus (certificats EV)
==========================================-

Ce sont les certificats qui sont pris en charge dans les navigateurs récents et 
qui permettent l'affichage d'un fond vert (indiquant ainsi un site de confiance 
garantie). L'abréviation EV signifie Extended Validation.

Présentation MISC 71 Janvier/Février 2014 Benjamin Sonntag
-----------------------------------------------------------

Ces certificats sont techniquement identiques aux certificats X.509 historiques, 
mais ils présentent des attributs spéciaux, représentés sous forme d’un
OID X.400 (par exemple, pour Comodo l’OID EV est 1.3.6.1.4.1.6449.1.2.1.5.1)
associé à une CPS distincte décrivant leur validation étendue.
Ainsi , une CA devra vérifier l’existence de la société possédant le nom de
domaine, son adresse, numéro de téléphone, gérant, etc. 

Ce faisant, le certificat EV présentera 3 caractéristiques intéressantes sur 
les navigateurs sur lequel il est utilisé :

- une barre d’adresse https:// verte ;
- le nom de la société à gauche de l’URL ;
- le nom de la CA ayant effectué la vérification.

Le CA/Browser Forum pensait donc améliorer la sécurité et surtout éviter le 
phishing par ce biais (et aussi vendre à nouveau hors de prix une simple 
vérification et une ligne dans une base de données, les EV les plus
simples ayant un prix de 300 à 2200 USD selon la CA !).

Cependant, on voit bien que la belle barre verte n’empêche pas le phishing de 
se développer, et force est de constater que le problème historique des CA
n’est pas résolu : **le fameux cadenas de Netscape que devaient vérifier les 
utilisateurs pour avoir prétendument confiance dans le site concerné n’est plus 
suffisant**.

Certificats X.509 omnidomaines
==============================

Un certificat omnidomaine ou "wildcard" permet de rendre générique une partie 
du nom de domaine certifié::

    *.societe.fr → www.societe.fr, toto.societe.fr, titi.societe.fr 
    (mais ni "societe.fr", ni "www.toto.societe.fr". Cf RFC 28185)

Certificats X.509 multisites
==============================

Ces certificats contiennent une liste de noms. Cette solution se base sur le 
champ subjectAltName.

Dans le cas des serveurs web, ces certificats sont utiles pour fournir plusieurs 
sites HTTPS sur une seule adresse IP. 
En effet, en HTTPS, l'échange du certificat se fait avant que le navigateur 
client n'ait transmis le nom de domaine qui l'intéresse. Or, si le certificat 
fourni par le serveur ne contenait pas le nom requis par le client, celui-ci 
déclencherait une alerte de sécurité.


Processus de création d’un certificat X.509
============================================

Un certificat X.509 est l’attestation par une AC, d’une liaison entre une clé 
publique du site et son nom de domaine. 

L’AC fournit le certificat à un titulaire de domaine après la validation de ses 
références. Le certificat qui est créé par l’AC contient des informations telles 
que la clé publique du domaine, le nom de domaine, le nom de l’AC qui a créé le 
certificat, la période de validité du certificat, etc. 

Ensuite, l’AC crée un condensat (hash) du certificat et le chiffre avec sa propre 
clé privée. Le condensat chiffré est la « signature numérique ». 

Le certificat doté de cette signature est désormais appelé ``Certificat numérique``.



