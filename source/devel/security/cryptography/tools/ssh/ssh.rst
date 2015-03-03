
.. index::
   pair: Privacy;  SSH
   ! SSH


.. _ssh:

===============================
SSH (Secure SHell)
===============================

.. seealso::

   - https://fr.wikipedia.org/wiki/Secure_Shell


.. contents::
   :depth: 3   
 
Introduction
============

Secure Shell (SSH) est à la fois un programme informatique et un protocole de 
communication sécurisé. 

Le protocole de connexion impose un échange de clés de chiffrement en début de 
connexion. Par la suite, tous les segments TCP sont authentifiés et chiffrés. 

Il devient donc **impossible d'utiliser un sniffer pour voir ce que fait 
l'utilisateur**.

Le protocole SSH a été conçu avec l'objectif de remplacer les différents 
programmes rlogin, telnet, rcp, ftp et rsh.


Le protocole
=============

Le protocole SSH existe en deux versions majeures : la version 1.0 et la version 2.0.

- La première version permet de se connecter à distance à un ordinateur afin 
  d'obtenir un shell ou ligne de commande. Cette version souffrait néanmoins 
  de problèmes de sécurité dans la vérification de l'intégrité des données 
  envoyées ou reçues, la rendant vulnérable à des attaques actives. 
  En outre, cette version implémentait un système sommaire de transmission 
  de fichiers, et du port tunneling.
- La version 2 qui était à l'état de draft jusqu'en janvier 2006 est déjà 
  largement utilisée à travers le monde.

Cette version est beaucoup plus sûre au niveau cryptographique, et possède en 
plus un protocole de transfert de fichiers complet, le SSH file transfer protocol.

Habituellement le protocole SSH utilise le port TCP 22. 

Il est particulièrement utilisé pour ouvrir un shell sur un ordinateur distant. 
Peu utilisé sur les stations Windows (quoiqu'on puisse l'utiliser avec PuTTY, 
mRemote, cygwin ou encore OpenSSH), SSH fait référence pour l'accès distant 
sur les stations Linux et Unix.

SSH peut également être utilisé pour transférer des ports TCP d'une machine 
vers une autre, créant ainsi un tunnel. 

Cette méthode est couramment utilisée afin de sécuriser une connexion qui ne 
l'est pas (par exemple le protocole de récupérations de courrier électronique 
POP3) en la faisant transférer par le biais du tunnel chiffré SSH.


