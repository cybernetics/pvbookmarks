
.. index::
   pair: FaitMain; Raspberry
   pair: FaitMain; GPIO
   
   
.. _volume_1_fait_main_2013:

================================================
Volume 1 "Fait main" 2013
================================================


.. seealso::

   - http://faitmain.org/volume-1/edito.html
   - https://github.com/faitmain/faitmain.org/tree/master/src/volume-1
   - http://faitmain.org/volume-1/faitmain-volume-1.pdf
   
   
.. contents::
   :depth: 3
   
   
Contenu du volume 1
====================

La tribune de ce numéro est un parallèle entre web hébergé et OGM.
`Lire la tribune <http://faitmain.org/volume-1/semences-donnes.html>`_.

Le **premier article** présente une application de reconnaissance de
feuille écrite pendant un Hackathon. C'est l'application qui a été écrite
en 24 heures par Olivier, Ronan & Tarek lors du dernier **AngelHack** à Paris.
On y parle de machine-learning au service des plantes, des *hackathons*
de programmation & de *responsive design*.
`Lire l'article <http://faitmain.org/volume-1/wtf.html>`__

Le **deuxième article** parle de **domotique** et vous explique comment
piloter des dispositifs sans fils - portails, détecteurs de mouvements etc.
On y parle d'**Arduino**, de **Raspberry-PI** et de signal en **433 mhz**.
`Lire l'article <http://faitmain.org/volume-1/dispositifs.html>`__

Le **troisième article** présente le travail de Marcin Ignac: des méduses
animées en 3D. Des captures d'écran de ces méduses ont ensuite été utilisées
pour faire partie d'un projet de livre génératif.
On y parle d'**animation procédurale**, de **processing.js** & d'hachurage.
`Lire l'article <http://faitmain.org/volume-1/cindermedusae.html>`__

Le **quatrième article** vous donne 5 conseils de photos culinaires pour
que vous puissiez prendre en photos vos soupes, gigots et autres
desserts comme un(e) pro. `Lire l'article <http://faitmain.org/volume-1/5-trucs.html>`__,

Suit une **interview** de Hugues Aubin au LabFab de Rennes.
`Lire l'article <http://faitmain.org/volume-1/labfab_rennes.html>`__.

Un **cinquième article** sur la conception d'un Juke box avec un
Raspberry-PI, sans aucune soudure requise :)
`Lire l'article <http://faitmain.org/volume-1/raspberry-jukebox.html>`__.

Le **sixième article** vous explique comment recycler
une vieille nappe de disque dur pour connecter le GPIO de votre
Raspberry. `Lire l'article <http://faitmain.org/volume-1/cable-gpio.html>`__.

Le **septième article** est une rapide présentation du jeu **The Midst**,
conçu avec Processing et WebPD.
`Lire l'article <http://faitmain.org/volume-1/the_midst.html>`__.

Enfin, le **huitième article** aborde les bases du fonctionnement d'une CNC.
`Lire l'article <http://faitmain.org/volume-1/cncs.html>`__.   
   
raspberry-jukebox
==================

.. seealso:: 

   - http://faitmain.org/volume-1/raspberry-jukebox.html
   - https://raw.github.com/faitmain/faitmain.org/master/src/volume-1/raspberry-jukebox.rst
   - :ref:`raspberry_pi_jukebox_2013`
   - http://forums.faitmain.org/viewtopic.php?id=9


Jukebox est écrite en Python avec :ref:`Django <django>` et fournit les fonctionnalités 
de base d'un JukeBox, à savoir un affichage des morceaux présents et un 
moyen pour les utilisateurs du réseau d'ajouter des morceaux dans la 
playlist
   
Le projet est un Juke-Box sans fil que je peux trimballer chez moi, qui
se connecte à mon réseau local en wifi - et qui fournit une application web
où tout le monde peut se connecter pour ajouter des morceaux de musique
dans une file d'attente.

Le projet final est une petite boite qui contient le R-PI et :

- une clé USB pour stocker de la musique. J'ai choisi la
  `PNY 16G <http://www.amazon.fr/dp/B0052QT6BQ>`_ qui est vraiment toute
  petite.

- un dongle USB wifi. J'ai choisi l'`Airlink Nano
  <http://www.amazon.fr/gp/product/B003X26PMO>`_ pour les mêmes raisons : il
  dépasse à peine du port USB.

- Une batterie USB pour ne pas avoir à brancher le R-PI sur le courant ou sur
  mon ordinateur. J'ai choisi `celui-ci
  <http://www.amazon.fr/gp/product/B006LR6N3O>`_ qui s'avère être beaucoup plus
  volumineux que le R-PI, mais qui fournit jusqu'à 1 ampère de courant - ce qui
  couvre les besoins et devrait permettre d'éviter à avoir recours à un Hub USB
  alimenté.

- Un mini-speaker. J'ai commandé le `X-Mini II
  <http://www.amazon.fr/gp/product/B001UEBN42>`_ qui est tout simplement
  incroyable. Ce petit speaker sort un très bon son vu sa taille, est
  auto-alimenté et on peut en brancher plusieurs à la suite.  J'en ai acheté un
  deuxième pour mon fils et je le recommande chaudement.  Dans tous les cas, le
  Juke-Box peut toujours être branché sur de vraies enceintes.

Petit détail agréable : Le speaker et la batterie USB ont été tous les deux
livrés pré-chargés.   

jukebox
--------

.. seealso::

   - https://raw.github.com/lociii/jukebox/master/README.rst
   - https://github.com/lociii/jukebox/blob/master/README.rst
   - https://raw.github.com/faitmain/faitmain.org/master/src/volume-1/raspberry-jukebox.rst
 
Pour la partie JukeBox, je_ comptais écrire une petite application web
au dessus de **mpg123** et je le ferais peut-être un jour, mais
il en existe déjà plusieurs.

`Jukebox <https://github.com/lociii/jukebox>`_ est écrite en Python
avec Django et fournit les fonctionnalités de base d'un JukeBox,
à savoir un affichage des morceaux présents et un moyen pour les
utilisateurs du réseau d'ajouter des morceaux dans la playlist.
 
.. _je: https://raw.github.com/faitmain/faitmain.org/master/src/volume-1/raspberry-jukebox.rst 


.. _cable_gpio:
   
Cable GPIO
==========


.. seealso::

   - :ref:`gpio`
   - http://faitmain.org/volume-1/cable-gpio.html
   - http://code.google.com/p/raspberry-gpio-python/
   - https://github.com/faitmain/faitmain.org/blob/master/src/volume-1/cable-gpio.rst
   
Une des fonctions qui a contribué au succès du Raspberry Pi, c'est la
possibilité d'interface avec le monde extérieur. 

On parle ici des `GPIO <http://fr.wikipedia.org/wiki/GPIO>`_ (en anglais les « General Purpose
Input and Output » – entrées et sorties pour tout usage), qui se retrouvent au
connecteur P1. En fabricant notre propre câble, on pourra se connecter à des
`DELs <http://fr.wikipedia.org/wiki/Diode_%C3%A9lectroluminescente>`_ (diodes
électroluminescentes), des moteurs ou autres composants physiques.


Module Python RPi.GPIO
----------------------

.. seealso::

   - http://pypi.python.org/pypi/RPi.GPIO
   - http://code.google.com/p/raspberry-gpio-python/

Avant toute chose, on doit se procurer un module Python du nom de
`RPi.GPIO <http://pypi.python.org/pypi/RPi.GPIO>`_. C'est un module qui
permet de contrôler les GPIO sur un Raspberry Pi. Sur Raspbian, il est
maintenant inclus, mais si on utilise une autre version de Linux, on peut
l'installer grâce a

.. code-block:: sh

    easy_install RPi.GPIO

ou bien par *apt-get*  :

.. code-block:: sh

   $ sudo apt-get install python-rpi.gpio

Créer un fichier portant le nom *flashled.py* ayant le contenu suivant :

.. code-block:: python

   #!/usr/bin/env python
   """ 2 DEL qui s'allument en alternance """
   import RPi.GPIO as gpio
   import time

   PINR = 0  # on utilisera 2 sur un RPi V2
   PING = 1  # on utilisera 3 sur un RPi V2

   gpio.setmode(gpio.BCM)  # mode Broadcom
   gpio.setup(PINR, gpio.OUT)  # DEL rouge en mode sortie (OUT)
   gpio.setup(PING, gpio.OUT)  # DEL verte en mode sortie (OUT)

   #On alterne pour l'eternite
   try:
       while True:
           gpio.output(PINR, gpio.HIGH)
           gpio.output(PING, gpio.LOW)
           time.sleep(1)
           gpio.output(PINR, gpio.LOW)
           gpio.output(PING, gpio.HIGH)
           time.sleep(1)
   except KeyboardInterrupt:
       gpio.cleanup()


- PINR est le GPIO pour la DEL rouge (0 pour un Rpi V1 et 2 pour un V2)
- PING est le GPIO pour la DEL verte (1 pour un Rpi V1 et 3 pour un V2)


   
   
   

   
