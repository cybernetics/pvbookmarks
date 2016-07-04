

.. index::
   pair: Windows HTML Help ; Format
   ! Windows HTML Help 
   pair: CHM ;  Windows HTML Help

.. _whm_chm:

==========================================
Windows HTML Help format (or known as CHM)
==========================================

.. seealso::

   - http://www.wikiwand.com/fr/Microsoft_Compressed_HTML


.. contents::
   :depth: 3
   
   
Introduction
============

Microsoft Compressed HTML (MCH), ou Microsoft HTML Help, est un format 
propriétaire pour les fichiers d'aide sur internet, développé par 
Microsoft et publié pour la première fois en 1997 comme étant le 
successeur du format Microsoft WinHelp. 

Introduit sur le marché pour Windows 98, il est toujours utilisé sur 
Windows XP et sur Windows 7 pour des logiciels tiers.


Formats de fichier
===================

Les fichiers d'aide portent l'extension:

- CHM (compressed HTML) pour la version 1, 
- et HXS pour la version 2. 


Un fichier d'aide compressé est une archive contenant plusieurs fichiers 
HTML, un par rubrique (topic) ainsi que les images et d'autres fichiers 
permettant une visualisation avec l'interface d'aide. 

Le système utilise un algorithme de compression LZX.

Un fichier CHM peut être décompressé en utilisant le programme hh.exe de 
Microsoft Windows : il suffit de taper en ligne de commande[1]::

    hh -decompile dossier_cible nom_de_fichier.chm

où nom_de_fichier est le fichier CHM que l'on veut décompresser et 
dossier_cible est le dossier dans lequel on va le décompresser.



Création de l'aide
===================

Le fichier d'aide est obtenu en compilant plusieurs fichiers :

- le fichier de projet, qui porte l'extension .hhp (HTML Help Project) 
  il fait le lien avec les différents fichiers ;
- les rubriques d'aide, sous la forme de fichiers HTML (avec 
  l'extension .htm ou .html) ; il y a un fichier par rubrique ;
- les images auxquelles il est fait référence dans les fichiers HTML, 
  au format GIF ;
- la table des matières, qui porte l'extension .hhc (HTML Help Contents) 
- l'index, qui porte l'extension .hhk.

La compilation est faite par le programme hhc.exe, qui fait partie de 
la suite de développement Microsoft HTML Help SDK (software development kit), 
ou bien par un programme de création d'aide d'un autre éditeur (comme 
par exemple RoboHelp d’Adobe Systems ou Doc-To-Help de ComponentOne)





