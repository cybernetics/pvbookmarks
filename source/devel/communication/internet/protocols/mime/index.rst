
.. index::
   pair: Internet; MIME
   ! Multipurpose Internet Mail Extensions
   ! MIME


.. _mime:

=============================================
Multipurpose Internet Mail Extensions (MIME)
=============================================


.. seealso::

   - http://fr.wikipedia.org/wiki/Multipurpose_Internet_Mail_Extensions
   - :ref:`smime`


.. contents::
   :depth: 3


Introduction
============

Multipurpose Internet Mail Extensions (MIME) ou Extensions multifonctions du 
courrier Internet est un standard internet qui étend le format de données des 
courriels pour supporter des textes en différents codage de caractères autres 
que l'ASCII, des contenus non textuels, des contenus multiples, et des 
informations d'en-tête en d'autres codages que l'ASCII. 

Les courriels étant généralement envoyés via le protocole SMTP au format MIME, 
ces courriels sont souvent appelés courriels SMTP/MIME.

À l'origine, SMTP avait été prévu pour ne transférer que des fichiers textes 
(codés en ASCII). 

Avec l'apparition du multimédia et l'utilisation croissante des applications 
bureautiques, le besoin s'est fait sentir d'échanger, en plus des fichiers 
textes, des fichiers binaires (format des applications bureautiques, images, 
sons, fichiers compressés).

Les types de contenus définis par le standard MIME peuvent être utilisés à 
d'autres fins que l'envoi de courriels, dans les protocoles de communication 
comme le HTTP pour le World Wide Web.

MIME est initialement spécifié dans cinq RFC: 

- RFC 2045, 
- RFC 2046, 
- RFC 2047, 
- RFC 2048, 
- RFC 2049. 

La RFC 2045 est complétée par la RFC 2077. 

La RFC 2048, maintenant obsolète, est remplacée par les RFC 4288 et RFC 4289.


MIME Types
==========

.. toctree::
   :maxdepth: 3
   
   types/index
   
   
