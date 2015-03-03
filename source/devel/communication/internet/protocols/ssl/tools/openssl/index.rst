
.. index::
   pair: Open ; SSL
   ! OpenSSL


.. _openssl:

============================================================
OpenSSL
============================================================

.. seealso::

   - https://www.openssl.org/
   - http://fr.wikipedia.org/wiki/Openssl
   - https://www.openssl.org/related/
   

.. figure:: logo_openssl.png
   :align: center
   

.. contents::
   :depth: 3

Introduction
=============


``OpenSSL`` est une boîte à outils de chiffrement comportant deux bibliothèques 
(libcrypto fournit les algorithmes cryptographiques, libssl implémente le 
protocole SSL) et une interface en ligne de commande (openssl).

Les bibliothèques (qui sont écrites en langage C) implémentent les fonctions 
basiques de cryptographie et fournissent un certain nombre de fonctions utiles. 

Grâce aux wrappers, il est possible de les utiliser dans une grande variété de 
langages informatiques.

Les paramètres de l'outil en ligne de commande openssl sont très nombreux ; 
ils permettent entre autres de choisir l'un des nombreux types de chiffrement 
(Blowfish, DES ou Triple DES, DSA, RC4, RC5, RSA...), d'encodage (base64...) 
ou de hachage (MD5, SHA-1...).

Cet utilitaire et les bibliothèques associées sont disponibles pour la plupart 
des Unix dont Linux et Mac OS X, mais aussi pour Microsoft Windows, DOS et OpenVMS. 

Le support des cartes accélératrices câblées est intégré à la branche principale 
depuis la version 0.9.7.

OpenSSL, qui est basé sur SSLeay de Eric Young et Tim Hudson, est distribué 
selon les termes d'une double licence de type BSD.


The goal of the project
=======================

The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, 
full-featured, and Open Source toolkit implementing the Secure Sockets Layer 
(SSL v2/v3) and Transport Layer Security (TLS v1) protocols as well as a 
full-strength general purpose cryptography library managed by a worldwide 
community of volunteers that use the Internet to communicate, plan, and develop 
the OpenSSL toolkit and its related documentation. 



OpenSSL bugs
================

.. toctree::
   :maxdepth: 3
   
   
   bugs/index


OpenSSL books
=============

openssl-cookbook
-----------------

.. seealso::

   - https://www.feistyduck.com/books/openssl-cookbook/


A short book that covers the most frequently used OpenSSL features and commands, 
written by Ivan Ristić

- Comprehensive coverage of OpenSSL installation, configuration, and key
  and certificate management
- Includes SSL/TLS Deployment Best Practices, a design and deployment guide
- Written by the author of SSL Labs and the SSL/TLS configuration assessment tool
- Available in a variety of digital formats (PDF, EPUB, Mobi/Kindle); no DRM
- Continuously updated 




OpenSSL versions
================

.. toctree::
   :maxdepth: 3
   
   
   versions/index
   
   
   
   




