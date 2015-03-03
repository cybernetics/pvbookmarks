
.. index::
   pair: Installer;   Innosetup
   pair: Inno-script ; Studio


.. _innosetup:

=========
Innosetup
=========

.. seealso::

   - http://en.wikipedia.org/wiki/Inno_Setup
   - http://www.jrsoftware.org/ishelp/index.php?topic=scriptintro
   - :ref:`pascal_language`


.. contents::
   :depth: 3

Introduction
============

Inno Setup is a free, feature-packed installation builder. The application's
features include a Windows 2000-style wizard interface; the ability to create
a single EXE for easy, online distribution; support for disk spanning; and full
uninstall capabilities. The program also includes customizable setup types,
integrated file compression, support for installing shared files and OCXs,
and the creation of Start menu icons, INI entries, and registry entries

Le logiciel Innosetup est sous http://inno-setup.en.softonic.com/

- http://www.jrsoftware.org/isdl.php
- http://www.jrsoftware.org/ispphelp/
- http://www.jrsoftware.org/ishelp/
- http://www.jrsoftware.org/


:dernière version utilisée: 5.5.3


Innosetup source code
=====================

.. seealso::

   - https://github.com/jrsoftware/issrc
   
   
Inno Setup is a free installer for Windows programs. 

First introduced in 1997, Inno Setup today rivals and even surpasses many 
commercial installers in feature set and stability.

.. seealso:: http://www.jrsoftware.org/isinfo.php
   

Pascal language
===============

.. seealso::

   - http://www.jrsoftware.org/ishelp/index.php?topic=scriptintro


Innosetup tips
==============

.. seealso::

   - http://www.mirality.co.nz/inno/tips.php



.. innosetup_options:

"Inno Setup" options
=====================

Les fenêtres d'installation se présentent de cette façon:
Setup - "Nom de l'application".

Les commutateurs les plus utilisé pour les applications utilisant la
technologie "Inno Setup" sont :

* SP- : désactive le message d'avertissement du début vous demandant
  si vous souhaitez réellement installer l'application.
* /SILENT : seule la barre de progression est montrée.
* /VERYSILENT : l'installation se fera de manière complètement silencieuse
  et sans même que la barre de progression soit visible.
* /NORESTART : demande à ce que l'ordinateur ne soit pas redémarré
  sauf si cela est absolument nécessaire.
* /SAVEINF="Nom_Fichier" : demande au programme d'installation de sauvegarder
  les paramètres d'installation dans le fichier spécifié. Cela vous permet
  d'automatiser les installations.
* /LOADINF="Nom_Fichier" : demande au programme de charger les paramètres
  d'installation à partir du fichier spécifié.
* /DIR="x:\Nom_Répertoire" : permet de remplacer le répertoire d'installation
  définit par défaut par celui que vous aurez spécifié.
* /GROUP="Nom_Répertoire" : permet de remplacer le répertoire d'installation
  du menu Démarrer définit par défaut par celui que vous aurez spécifié.

D'autres possibilités sont expliquées sur ce site : http://www.jrsoftware.org


Innosetup versions
===================

.. toctree::
   :maxdepth: 3
   
   
   versions/index
  
  

Innosetup examples 
===================

.. toctree::
   :maxdepth: 3
   
   examples/index   


Graphical Installer
===================

.. toctree::
   :maxdepth: 3
   
   graphical/index
   
