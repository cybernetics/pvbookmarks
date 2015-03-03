
.. index::
   pair: File ; Transfer
   ! FTP


.. _ftp:

============================================================
File Transfer Protocol
============================================================


.. seealso::

   - http://fr.wikipedia.org/wiki/File_Transfer_Protocol
   - http://tools.ietf.org/html/rfc3659
   
   
Introduction
=============
   
File Transfer Protocol (protocole de transfert de fichiers), ou FTP, est un 
protocole de communication destiné à l'échange informatique de fichiers sur 
un réseau TCP/IP. 

Il permet, depuis un ordinateur, de copier des fichiers vers un autre ordinateur 
du réseau, ou encore de supprimer ou de modifier des fichiers sur cet ordinateur. 

Ce mécanisme de copie est souvent utilisé pour alimenter un site web hébergé 
chez un tiers.

La variante de FTP protégée par les protocoles SSL ou TLS (SSL étant le 
prédécesseur de TLS) s'appelle FTPS.

FTP obéit à un modèle client-serveur, c'est-à-dire qu'une des deux parties, le 
client, envoie des requêtes auxquelles réagit l'autre, appelé serveur. 

En pratique, le serveur est un ordinateur sur lequel fonctionne un logiciel 
lui-même appelé serveur FTP, qui rend publique une arborescence de fichiers 
similaire à un système de fichiers UNIX. 

Pour accéder à un serveur FTP, on utilise un logiciel client FTP (possédant une 
interface graphique ou en ligne de commande).

FTP, qui appartient à la couche application du modèle OSI et du modèle ARPA, 
utilise une connexion TCP.

Par convention, deux ports sont attribués (well known ports) pour les connexions 
FTP : le port 21 pour les commandes et le port 20 pour les données. 

Pour le FTPS dit implicite, le port conventionnel est le 990.

Ce protocole peut fonctionner avec IPv4 et IPv6.  


FTP clients
============

.. toctree::
   :maxdepth: 3
   
   client/index


FTP Servers
============

.. toctree::
   :maxdepth: 3
   
   server/index



Tools
======

.. toctree::
   :maxdepth: 3
   
   tools/index
   
    
