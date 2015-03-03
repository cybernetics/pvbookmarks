


.. index::
   pair: Format ; TIFF


.. _image_tiff_format:

============================================
TIFF "Tag(ged) Image File Format"
============================================

.. seealso::

   - http://fr.wikipedia.org/wiki/Tiff

.. contents::
   :depth: 3


Introduction
============


Le Tag(ged) Image File Format généralement abrégé TIFF est un format de fichier
pour image numérique. Adobe en est le dépositaire et le propriétaire initial
(via Aldus).

Plus exactement, il s'agit d'un format de **conteneur (ou encapsulation)**, à la
manière de avi ou zip, c'est-à-dire pouvant contenir des données de formats
arbitraires.


Source code : https://gitorious.org/imagezero
=============================================

Structure

Un fichier TIFF commence par les deux caractères ASCII MM pour big endian ou II
pour little endian.

Les deux octets suivants représentent 42, en big endian ou little endian.

Historiquement, les images au format TIFF étaient limitées à une taille de 4Go
(taille de l'offset sur 32 bits).

Depuis la libtiff 4.0 (parue en 2007 et appelée BigTIFF ), il est possible
d'avoir des images d'une taille supérieure.


