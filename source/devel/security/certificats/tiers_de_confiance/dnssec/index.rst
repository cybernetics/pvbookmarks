
.. index::
   pair: RFC ; 6698
   pair: Protocole; DANE
   pair: MISC; 71
   ! DANE


.. _rfc_6698:
.. _dnssec:
.. _dane:

===============================
DNSSEC, Protocole DANE RFC 6698
===============================


.. seealso::

   - https://www.rfc-editor.org/rfc/rfc6698.txt
   - https://dane.rd.nic.fr/
   - https://github.com/pieterlexis/swede
   
   
.. contents::
   :depth: 3   
   
Présentation 1
===============

Encrypted communication on the Internet often uses Transport Layer
Security (TLS), which depends on third parties to certify the keys
used.  This document improves on that situation by enabling the
administrators of domain names to specify the keys used in that
domain's TLS servers.  This requires matching improvements in TLS
client software, but no change in TLS server software.


Présentation 2 MISC 71 Janvier/Février 2014 par Benjamin Sonntag 
===================================================================


Enfin, plus proche des protocoles historiques de l’Internet, et d’ailleurs 
normalisés sous la RFC 6698, DANE (pour DNS-based Authentication of Named Entities) 
et TLSA (nom du type de ressource DNS associé) proposent tout simplement de 
publier les signatures numériques des clés publiques des sites web ou d’autres 
protocoles (pop, imap, smtp...) dans le DNS de la zone concernée.

Ajoutée à DNSSEC, cela permet de garantir un niveau de confiance équivalent à 
celui des autorités de certification, mais en se basant sur le DNS, dont vous
disposez déjà dès que vous avez un nom de domaine.

Hélas, la faible pénétration de DNSSEC dans l’Internet rend cette solution pour 
l’instant peu utile, et si Chrome 14 savait valider ainsi les sites HTTPS, les 
nouvelles versions en ont enlevé le support, trop peu utilisé.


Présentation 3 MISC 71 Janvier/Février 2014 par Sandoche Balakrichenan 
=======================================================================

On peut dire que c’est à partir de mars 2011 que les remparts de l’authentification 
sur Internet s’écroulaient les uns après les autres. 

Le 15 mars 2011, Comodo, un fournisseur leader sur le marché des certificats
X.509 a découvert que l’un de ses affiliés avait été compromis par un attaquant 
ayant créé un compte utilisateur chez eux. Avec ce compte, l’attaquant a
créé des demandes de certificats pour plusieurs sites web importants comme 
login.live.com, mail.google.com, login.yahoo.com, etc., et il est sûr qu’il a 
obtenu au moins un certificat X.509 pour ces sites.

Alors que l’on pensait que l’attaque Comodo était un cas isolé dans la vie de 
l’industrie de l’Autorité de Certification (AC), quatre mois plus tard, une 
autre AC, DigiNotar, subit une attaque. L’attaquant qui avait agi en mars contre 
Comodo a revendiqué l’attaque sur DigiNotar.

Même si rien ne prouve que les deux attaques viennent de la même personne, dans 
les deux cas, l’attaquant a réussi à trouver un chemin dans l’infrastructure de
l’AC et à délivrer des certificats X.509 valides pour des domaines hors de leur 
contrôle.

Ces attaques très médiatisées ont suscité un certain nombre de questions. 
En particulier celle-ci : le modèle d’authentification existant fourni par 
l’infrastructure AC est-il vulnérable ? Et si oui, comment précisément
atténuer ces vulnérabilités? Il y a un consensus assez large au sein des parties 
prenantes pour dire que quelque chose doit être fait, mais peu d’entente sur 
comment cela devrait être techniquement fait.

Depuis de nombreuses années, l’attestation de l’authenticité des noms de
domaines était effectuée par les Autorités de certification (AC). 

**Une solution alternative a été recherchée suite à plusieurs attaques mettant 
en exergue la vulnérabilité de l’infrastructure AC**.

Le protocole ``DANE`` développé par l’IETF permet à un domaine d’attester lui-même
les entités autorisées à le représenter, une PKI alternative – DNSSEC basée sur
le DNS.

Le début de cet article présente le problème, puis introduit brièvement DNSSEC,
explique comment DANE pourrait être implémenté, et enfin conclut sur les défis
à relever pour passer du modèle d’authentification web actuel à DNSSEC.


Conclusion
==========

Jusqu’à présent, les navigateurs web se sont basés sur la certification des AC 
pour s’assurer de la validité des serveurs web avec un nom de domaine. 

La promesse de DANE, sécurisé par DNSSEC est une interaction plus directe (sans 
l’intervention des AC) entre les clients et les domaines avec lesquels ils 
échangent. 

À court terme, DANE peut être déployé pour renforcer la PKIX existante. 

**À long terme**, DANE avec un DNSSEC entièrement déployé ainsi que les défis de la 
transition relevés permettra aux opérateurs de domaine (avec des certificats 
auto-signés plutôt que de payer un CA) de se porter garants de leur propre nom 
de domaine.



