
.. index::
   pair: Raspberry Pi; B


.. _raspberrypi_b:

======================
Raspberry Pi Modèle B
======================

.. seealso::

   - http://fr.wikipedia.org/wiki/Raspberry_Pi#Mod.C3.A8le_B

.. contents::
   :depth: 3

Différences
============

- 2 ports USB 2.0 au lieu de l'unique port du modèle A, mais sur un seul 
  bus, via le composant SMSC LAN95126 ;
- 1 port réseau Fast Ethernet (10/100 Mbits/s) via le même composant SMSC.

Le circuit LAN9512 qui gère les deux ports USB2 et le port réseau, est 
connecté au CPU via un unique port USB2 ; la bande passante est donc 
partagée entre ces trois ports.

Modèle B Rev1
=============

Différences :

- 2 ports USB 2.0 au lieu de l'unique port du modèle A, mais sur un seul 
  bus, via le composant SMSC LAN95126 ;
- 1 port réseau Fast Ethernet (10/100 Mbits/s) via le même composant SMSC.

Le circuit LAN9512 qui gère les deux ports USB2 et le port réseau, est 
connecté au CPU via un unique port USB2 ; la bande passante est donc 
partagée entre ces trois ports.


Modèle B Rev1 + ECN0001
========================

Différences :

- Suppression des fusibles protégeant les sorties USB
- Suppression de D14 (pouvait provoquer des interférences avec des périphériques CEC)


Modèle B Rev2
=============

Différences :

- Implémentation du reset (en reliant les broches 1 et 2 de P6)
- Support JTAG (deux broches GPIO interchangées)
- Support I2C (canaux primaire et secondaire inversés)
- Suppression de quatre signaux GPIO utilisés pour l'identification de 
  version, et réaffectation à d'autres rôles
- SMSC +1V8
- Deux trous de fixation
- Correction du marquage des LEDs sur la platine


Modèle B 512 Mio
=================

.. seealso::

   - http://www.blaess.fr/christophe/2012/10/22/un-raspberry-pi-avec-512-mo/


Prise pour alimentation micro-USB (consommation : 700mA) ;

Différences :

- La RAM passe à 512 Mio (au lieu de 256 Mio sur les modèles précédents) ;
- Le modèle est estampillé avec la référence 4G en lieu et place de 
  l'ancienne référence 2G.

Pour utiliser les 512 Mio de RAM, le firmware de la carte mère doit être 
mis à jour
