

.. index::
   pair: Virtualization ; Virtualbox
   ! Virtualbox

.. _virtualbox:

==============
Virtualbox
==============

.. seealso::

   - https://fr.wikipedia.org/wiki/Oracle_VM_VirtualBox
   - https://secure.wikimedia.org/wikipedia/en/wiki/VirtualBox
   - http://virtualboxes.org/images/
   - http://www.commentcamarche.net/download/telecharger-3673479-virtualbox


.. contents::
   :depth: 3

Introduction
============

Oracle VM VirtualBox (anciennement VirtualBox) est un logiciel de virtualisation
créé par InnoTek.

Il est disponible en tant qu'hôte sur les systèmes d'exploitation:

- Windows,
- Linux 32 et 64 bits,
- FreeBSD 32 et 64 bits
- et Mac OS X.

Il supporte en tant qu'invité:

- Windows (dont Vista et 7),
- Linux 2.x, OS/2 Warp,
- OpenBSD
- et FreeBSD entre autres.


VirtualBox permet d'émuler complètement un PC, comme si vous aviez un second
ordinateur dans une simple fenêtre.

C'est utile pour tester d'autres systèmes d'exploitation sans repartitionner
son disque dur, pour naviguer en toute sécurité ou pour tester un logiciel sans
risque de rendre son système d'exploitation instable.

Vous pouvez créer autant de machines virtuelles et installer tous les systèmes
d'exploitation que vous le souhaitez.
Il est possible de définir, pour chaque machine virtuelle, sa mémoire RAM, son
espace disque, si elle aura accès aux ports USB, au réseau, à la carte son, etc.

VirtualBox contient un gestionnaire de disques qui vous permet de créer des
disques virtuels sous forme de fichiers .vdi qui apparaîtront comme de vrais
disques dans les machines virtuelles.

Cela vous permet donc de "créer" à volonté des disques, et cela sans jamais
avoir à repartitionner votre disque dur.

Vous pouvez également **utiliser directement des images ISO de CD et DVD**,
ce qui permet de tester des distributions Linux sans avoir à les graver.

Enfin, VirtualBox possède un serveur RDP intégré, ce qui permet de démarrer une
machine virtuelle sur un ordinateur, et utiliser cette machine virtuelle à partir
d'un autre ordinateur.

.. note:: Pour les machines sous un autre OS que Windows, veuillez choisir une
   autre version parmi celles-ci_.


.. _celles-ci: http://www.virtualbox.org/wiki/Downloads


Virtualbox informations
========================

.. toctree::
   :maxdepth: 4


   addons/index
   linux/index
   tools/index
   tutorials/index
   versions/index
   windows/index






