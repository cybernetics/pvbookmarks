

.. index::
   pair: Qt; 5.1
   pair: Qt; RS232
   pair: Qt; Serial Port   
   ! Qt5.1

.. _qt_5_1_annouce_linuxfr:

===============================
Technologie Qt 5.1 est juillet
===============================

.. seealso::

   - http://linuxfr.org/news/qt-5-1-est-juillet

.. contents::
   :depth: 3

Introduction
============

Qt est un framework (cadriciel en français) multiplateforme écrit en C++ avec 
des bindings pour Python et Ruby notamment. 

Il est la base de l'environnement de bureau KDE et Razor-qt. 

Certaines applications très connues l'utilisent. 

Citons par exemple VLC, Google Earth, Skype et VirtualBox. 

La version 5.1 vient d'être publiée ce 3 juillet 2013.

Les nouveaux widgets de Qt Quick
=================================

Un gros manque de Qt Quick, le langage de description d'interface de Qt, 
c'était le manque de widget (c'est-à-dire les boutons, barres de progression…). 
En dehors des rectangles et des ronds, il n'y avait pas grand chose. C'est un 
problème résolu avec cette version qui apporte tout cela et, comme toujours 
avec Qt, cela s'adapte bien évidemment au thème actuel de votre plateforme mais 
peut être stylé à votre convenance. 

Cela va permettre de développer (ou de migrer) les applications avec des 
interfaces un peu plus évoluées.

Gestionnaires de mise en page pour Qt Quick
===========================================

Un gestionnaire de mise en page est un widget qui permet de disposer 
automatiquement ses widgets enfants. 

De nouveaux gestionnaires de mise en page font leur apparition pour permettre 
de mieux réaliser vos interfaces graphiques. 

Il est possible de les utiliser pour mélanger des QWidget en C++ et des 
éléments Qt Quick en QML.


Port pour Android et iOS
========================

Des versions pour Android et iOS sont disponibles en tant que technology preview. 

Pour le premier, quasiment tout est fonctionnel (Qt Sensors, Qt Quick 2…) sauf 
la gestion de la caméra dans Qt Multimedia, Qt WebKit et Qt Serialport. 

La version 5.2 est censée fournir un port officiel pour cette plateforme. 

Du côté de la pomme, c'est moins bien pris en charge (pas de Qt Quick 2, 
normalement il viendra avec la 5.2) et le développement doit être fait avec 
XCode et non pas avec Qt Creator.

Qt 5.1 est livré avec la version 2.7.2 de QtCreator
===================================================

L'amélioration principale de cette version est le support du développement 
pour Android, mais de nombreuses corrections de bugs sont de la partie.


.. _qt_serial_port:

Qt Serial Port
===============

.. seealso::

   - http://qt-project.org/doc/qt-5.1/qtserialport/qtserialport-index.html

Un nouveau module nommé Qt Serial Port fait son apparition. 

Comme son nom l'indique, il permet d’interagir avec les ports série du système. 

Ce module est disponible pour les cibles Windows, Linux et OS X.





   
