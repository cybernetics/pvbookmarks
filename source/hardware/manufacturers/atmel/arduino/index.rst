
.. index::
   ! Arduino
   pair: Computer; Arduino
   ! Massimo Banzi


.. _arduino:

========================================
Arduino
========================================

.. seealso::

   - https://fr.wikipedia.org/wiki/Arduino
   - http://arduino.cc/
   - http://code.google.com/p/arduino/


   

.. contents::
   :depth: 3


Matériel
=========

Un module Arduino est généralement construit autour d'un microcontrôleur Atmel 
AVR (ATmega328 ou ATmega2560 pour les versions récentes, ATmega168 ou ATmega8 
pour les plus anciennes), et de composants complémentaires qui facilitent la 
programmation et l'interfaçage avec d'autres circuits. 

Chaque module possède au moins un régulateur linéaire 5 V et un oscillateur à 
quartz 16 MHz (ou un résonateur céramique dans certains modèles).

Le microcontrôleur est préprogrammé avec un bootloader de façon à ce qu'un 
programmateur dédié ne soit pas nécessaire.


Logiciel
=========

Le logiciel de programmation des modules Arduino est une application Java, libre 
et multi-plateforme, servant d'éditeur de code et de compilateur, et qui peut 
transférer le firmware et le programme au travers de la liaison série (RS-232, 
Bluetooth ou USB selon le module). 

Il est également possible de se passer de l'interface Arduino, et de compiler et 
uploader les programmes via l'interface en ligne de commande2.

Le langage de programmation utilisé est le C++, compilé avec avr-g++ 3, et lié 
à la bibliothèque de développement Arduino, permettant l'utilisation de la carte 
et de ses entrées/sorties. 

La mise en place de ce langage standard rend aisé le développement de programmes 
sur les plates-formes Arduino, à toute personne maîtrisant le C ou le C++.


Réseaux sociaux
================

Twitter
-------

.. seealso::

   - https://twitter.com/planetarduino
   - https://twitter.com/arduino
   
   
Massimo Banzi
--------------

.. seealso::

   - https://twitter.com/mbanzi
   
   
   
   


   
   
   




