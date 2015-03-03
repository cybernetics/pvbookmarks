
.. index::
   pair: FTP ; VsFTPd


.. _VsFTPd:

============================================================
VsFTPd (Very Secure FTP Daemon)
============================================================


.. seealso::

   - http://fr.wikipedia.org/wiki/VsFTPd
   - https://security.appspot.com/vsftpd.html
   
   
   
Description
===========

vsFTPd (Very Secure FTP Daemon), crée en 2000, est un serveur FTP qui mise 
beaucoup sur la sécurité, ce qui n'a rien d'étonnant puisqu'il est développé 
par Chris Evans chargé de la sécurité de Google Chrome. 

Il est important de noter qu'il est l'un des premiers logiciels serveurs à 
mettre en oeuvre la séparation des privilèges, minimisant ainsi les risques 
de piratage.

La configuration par défaut de VsFTPd est très restrictive :

- Seul le compte anonyme est autorisé à se connecter au serveur, et en lecture seule.
- Les utilisateurs ne peuvent accéder qu'à leur compte.

Fonctions de VSFTPd :

- Configuration accessible
- Utilisateurs virtuels
- Adresses IP virtuelles
- Limitation de la bande passante
- IPv6
- Support du chiffrement au travers de SSL intégré FTPS, méthodes explicites 
  et implicites supportées

Il est distribué selon les termes de la licence Licence publique générale GNU.

    
Installation
=============

.. toctree::
   :maxdepth: 3
   
   installation/index
   
   

      
