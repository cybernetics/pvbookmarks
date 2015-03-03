.. module:: USB_doc
    :synopsis: USB introduction


.. index::
   pair: USB ; introduction

================
USB introduction
================

.. contents::
   :depth: 3


.. seealso::

   - http://en.wikipedia.org/wiki/Universal_Serial_Bus
   - http://www.usb.org/developers/devclass_docs#approved
   - http://kernelnewbies.org/USB
   - http://www.linux-usb.org/


USB (Universal Serial Bus) is a specification to establish communication
between devices and a host controller (usually personal computers).
USB is intended to replace many varieties of serial  and parallel ports.
USB can connect computer peripherals such as mice, keyboards, digital
cameras, printers, personal media players, flash drives, and external
hard drives. For many of those devices, USB has become the standard
connection method. USB was designed for personal computers, but it has
become commonplace on other devices such as smartphones, PDAs and video
game consoles, and as a power cord between a device and an AC adapter
plugged into a wall plug for charging.

The design of USB is standardized by the USB Implementers Forum (USB-IF),
an industry standards body incorporating leading companies from the
computer and electronics industries.

Notable members have included Agere (now merged with LSI Corporation),
Apple Inc., Hewlett-Packard, Intel, Microsoft, Sony and NEC.



Caractéristiques générales
==========================

L’Universal Serial Bus est une connexion à haute vitesse qui permet de connecter
des périphériques externes à un ordinateur (hôte dans la terminologie USB).
Il permet le branchement simultané de 127 périphériques par contrôleur (hôte).
Le bus autorise les branchements et débranchements à chaud (« Hot-Plug », sans
avoir besoin de redémarrer l’ordinateur) et fournit l’alimentation électrique
des périphériques sous 5 V, dans la limite de 500 mA.

Le bus possède une topologie arborescente (dite également en étoile) :
les feuilles de cet arbre sont les périphériques ; les nœuds internes
sont des hubs qui permettent de greffer des sous-arborescences dans
l'arborescence principale. On trouve dans le commerce ces hubs sous forme
de petits boîtiers alimentés soit sur le bus, soit sur le secteur, et qui
s'utilisent comme des multiprises.
Certains périphériques intègrent également un hub (moniteurs, claviers…).
Cependant, tout bus USB possède au moins un hub situé sur le contrôleur :
le hub racine, qui peut gérer les prises USB de l'ordinateur.

Le nombre de hubs connectés en cascade est limité : hub racine compris, il
ne doit pas exister plus de 7 couches dans l'arborescence.



USB 1.x
-------


La version 1.x du bus peut communiquer dans deux modes:

- mode lent (1,5 Mbit/s) (« Low Speed ») permet de connecter des périphériques
  qui ont besoin  de transférer peu de données, comme les claviers et souris ;

- mode rapide (12 Mbit/s, soit 1,5 Mo/s) (« Full Speed ») est utilisé pour
  connecter des imprimantes, scanners, disques durs, graveurs de CD et autres
  périphériques ayant besoin de plus de rapidité.
  Néanmoins il est insuffisant pour beaucoup de périphériques de stockage de masse
  (ce mode permet la vitesse « 10 X » des CD).



USB 2.0
-------



USB 2.0 introduit un troisième mode permettant de communiquer à 480 Mbit/s
(soit 60 Mo/s).  Ce mode est appelé « high Speed ».
Il est utilisé par les périphériques rapides : disques durs, graveurs…
Mais en 2009, la plupart des périphériques ont une vitesse inférieure à ce
que permet l'USB 2.0.



USB 3.0
-------


La dernière version, l’USB 3.0, comporte un quatrième mode (« Super Speed »)
permettant de communiquer à 4,8 Gbit/s (soit 600 Mo/s).

Les premiers appareils commercialisés sont prévus pour 2010.

Lorsque l’on parle d’un équipement USB, il est nécessaire de préciser la
révision de la norme (1.1 ou 2.0) mais également la vitesse
(Low, Full ou High Speed).

Une clef USB spécifiée en USB 2.0 n’est pas forcément High Speed si cela n’est pas
précisé par un logo « High Speed ».

Le bus USB reste plus lent que des bus internes comme PCI ou AGP.



.. _connexion_plug_and_play_enumeration:

Connexion à chaud et Plug and Play : processus d'énumération
=============================================================

Les ports USB supportent la connexion à chaud et la reconnaissance automatique
des dispositifs (Plug and Play). Ainsi, les périphériques peuvent être branchés
sans éteindre l’ordinateur.

Lors de la connexion du périphérique à l’hôte, ce dernier détecte l’ajout du
nouvel élément grâce au changement de la tension entre les fils D+ et D-.
À ce moment, l’ordinateur envoie un signal d’initialisation au périphérique
pendant 10 ms, puis lui fournit du courant grâce aux fils GND et VBUS
(jusqu’à 100 mA). Le périphérique est alors alimenté en courant électrique et
peut utiliser temporairement l’adresse par défaut (l’adresse 0).

L’étape suivante consiste à lui fournir son adresse définitive et à obtenir
sa description : c’est la procédure d’énumération.

En effet, après avoir reçu son adresse, le périphérique transmet à l'hôte
une liste de caractéristiques qui permettent à ce dernier de l'identifier
(type, constructeur, nom, version). L’hôte, disposant de toutes les
caractéristiques nécessaires est alors en mesure de charger le pilote approprié.

Les périphériques sont regroupés en types ou classes dans la terminologie USB.
**Tous les dispositifs d'une classe donnée reconnaissent le même protocole
normalisé.**

Il existe par exemple une classe pour les périphériques de stockage de masse
(mass storage class, MSC), implémentée par la quasi-totalité des clés USB,
disques durs externes, appareils photo et par certains baladeurs.

La plupart des systèmes d’exploitation possèdent des pilotes génériques,
pour chaque type de périphérique. Ces pilotes génériques donnent accès aux
fonctions de base, mais des fonctions avancées peuvent manquer.


USB device classes
==================


.. toctree::
   :maxdepth: 2

   usb_device_classes



USB devices and hosts, OTG (On-The-Go)
======================================


Il existe deux types de périphériques USB:

- 'host' : un périphérique de type ordinateur;

- 'device' e:un périphérique moins évolué, comme un appareil photo,
  une souris, un clavier.

Cependant, certains processeurs embarqués (comme l'AT91-RM9200) intègrent
à la fois une interface host et une interface device.

**La nouvelle norme OTG (On-The-Go) permet de connecter 2 périphériques
devices entre eux sans passer par un host.**

.. toctree::
   :maxdepth: 2

   usb_host
   usb_device
   usb_on_the_go



