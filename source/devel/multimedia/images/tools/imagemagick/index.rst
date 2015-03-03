

.. index::
   pair: Images ; Imagemagick
   ! Imagemagick


.. _imagemagick_image_library:

==========================
imagemagick image library
==========================

.. seealso:: 

   - https://fr.wikipedia.org/wiki/Imagemagick
   - http://www.imagemagick.org/script/index.php

.. figure:: 100px-Imagemagick-logo.png
   :align: center


.. contents::
   :depth: 3

Introduction
============


ImageMagick est un logiciel libre, comprenant une bibliothèque, ainsi qu'un 
ensemble d'utilitaires en ligne de commande, permettant de créer, de convertir, 
de modifier et d'afficher des images dans un très grand nombre de formats. 

Les images peuvent être découpées, les couleurs peuvent être modifiées, 
différents effets peuvent être appliqués aux images, les images peuvent 
subir des rotations, il est possible d'y inclure du texte, des segments, 
des polygones, des ellipses et des courbes de Bézier, etc.

ImageMagick est un logiciel libre : sa licence est compatible avec la licence 
GNU GPL. Il est disponible sur la plupart des plates-formes.

La plupart des fonctionnalités d'ImageMagick peuvent être utilisées en ligne 
de commande, mais souvent, toutefois, ImageMagick est combiné avec d'autres 
programmes écrits dans des langages comme Perl, C, C++, Python, Ruby, PHP, 
OCaml ou Java, pour lesquels des interfaces prêtes à l'emploi (PerlMagick, 
Magick++, :ref:`pystacia <pystacia_python_image_library>` PythonMagick, RMagick, 
MagickWand pour PHP et JMagick) sont  disponibles. Cela permet de manipuler 
des images de façon plus automatisée.

Types de transformation
=======================

.. seealso:: 

   - http://www.imagemagick.org/Usage
   - https://www.quennec.fr/gnulinux/commandes/multim%C3%A9dia/photo/imagemagick

This web pages presents a set of examples using ImageMagick from the command 
line. However they are also examples of what can be done using the ImageMagick 
Application Programming Interface (API). As such these pages should be the 
first stop for IM users after reading the terse user manuals.

Les différentes options d'ImageMagick et leur syntaxe
=====================================================


.. seealso:: http://www.imagemagick.org/script/command-line-options.php


.. _imagemagick_tools:

Les différents outils d'ImageMagick
===================================

Cette suite d'outils inclut en réalité 11 commandes distinctes, chacune dédiée
à un certain type d'opérations.

**animate**
    Permet d'animer une séquence d'images.
    
**compare**
    Permet d'établir les différences d'un point de vue mathématique et visuel
    entre une image et sa reproduction.
    
**composite**
    Permet de superposer 2 images.
    
**conjure**
    Est une commande capable d'interpéter et d'exécuter des scripts MSL 
    (Magick Scripting Language)            
    
**convert**
    Est l'une des commandes les plus utiles : elle permet de réaliser toutes 
    sortes de transformations sur une image (conversion de format, 
    redimensionnement, découpage, effets de flou, retournement, etc..); à noter
    qu'un nouveau fichier image est créé, l'originbal demeure intact.
    
**display**
    Permet d'afficher une image ou une séquence d'images.
    
**identify**
    Précise le format et les caractéristiques d'un ou pluseiurs fichiers images.
    
**import**
    est dédiée à la capture d'écran : elle permet de capturer une fenêtre, 
    l'ensemble de l'écran ou bien n'importe quelle zone à l'écran (à sélectionner 
    à la souris.
    
**mogrify**
    est similaire à la commande ``convert``, à ceci près que l'image originale
    est cette fois-ci écrasée par sa nouvelle version.
    
    .. seealso:: :ref:`resizing_image_sizes`
    
**montage**
    permet de créer une image composite à partir de plusieurs images (à la manière 
    d'une mosaïque)
    
**stream**
    est destinée au streaming d'un ou plusieurs pixels d'une image, ou d'une 
    portion de l'image, dans le format qui vous convient.



ImageMagick wrappers
====================

.. toctree::
   :maxdepth: 3
   
   wrappers/index
   
   




