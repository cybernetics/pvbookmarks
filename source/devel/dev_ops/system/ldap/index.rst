

.. index::
   ! LDAP



.. _ldap:

======
LDAP
======

.. seealso:: https://secure.wikimedia.org/wikipedia/fr/wiki/LDAP


.. contents::
   :depth: 3

Présentation
============


Lightweight Directory Access Protocol (LDAP) est à l'origine un protocole
permettant l'interrogation et la modification des services d'annuaire.

Ce protocole repose sur TCP/IP.

Il a cependant évolué pour représenter une norme pour les systèmes d'annuaires,
incluant un modèle de données, un modèle de nommage, un modèle fonctionnel basé
sur le protocole LDAP, un modèle de sécurité et un modèle de réplication.

Un annuaire LDAP respecte généralement le modèle X.500 édicté par l'UIT-T :
c'est une structure arborescente dont chacun des nœuds est constitué d'attributs
associés à leurs valeurs.

Le nommage des éléments constituant l'arbre (racine, branches, feuilles) reflète
souvent le modèle politique, géographique ou organisationnel de la structure
représentée.

La tendance actuelle est d'utiliser le nommage DNS pour les éléments de base de
l'annuaire (racine et premières branches, domain components ou dc=…).

Les branches plus profondes de l'annuaire peuvent représenter des unités
organisationnelles ou des groupes (organizational units ou ou=…), des personnes
(common name ou cn=… voire user identifier uid=…), …

L'assemblage de tous les composants (du plus précis au plus général) d'un nom
forme son distinguished name, l'exemple suivant en présente deux :

- cn=ordinateur,ou=machines,dc=EXEMPLE,dc=FR
- cn=Jean,ou=gens,dc=EXEMPLE,dc=FR

La dernière version en date du protocole est LDAPv3.
Cette version est définie par l'IETF dans plusieurs RFC en commençant par la
`RFC 4510`_

.. _`RFC 4510`: http://tools.ietf.org/html/rfc4510

.. index::
   LDAP python tools


LDAP python tools
=================

-http://pumpkin.prymitive.com/0.1/index.html








