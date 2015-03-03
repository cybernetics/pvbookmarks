

.. index::
   pair: Images ; PDF
   pair; Extraction (d'images) ; PDF


.. _pdfimages:

========================================
Extraction d'images avec ``pdfimages``
========================================


.. contents::
   :depth: 3

Présentation
=============


Voici un petit truc fort sympathique pour extraire toutes les images 
d’un fichier PDF. 

L’outil utilisé se nomme pdfimages, il se trouve dans l’utilitaire Xpdf.

La syntaxe est la suivante::

    $ pdfimages [options] PDF-file image-root

Donc, pour extraire les images du fichier mon_fichier_plein_d_images.pdf::

    $ pdfimages -j mon_fichier_plein_d_images.pdf mes_images


On obtient une suite d’images au format PPM, PBM ou JPEG

