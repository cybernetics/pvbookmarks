
.. index::
   pair: Debian; 7
   pair: Debian; Wheezy


.. _debian_7:
.. _debian_wheezy:

================================
Debian 7 (wheezy) May 4th, 2013
================================


.. seealso::

   - http://www.debian.org/releases/wheezy/


.. contents::
   :depth: 3

Annonce
=======

.. seealso::

   - http://www.debian.org/News/2013/20130504
   - http://linuxfr.org/news/debian-episode-vii

Après de nombreux mois de développement continu, le projet Debian a le 
plaisir d'annoncer la publication officielle de la version 7.0, surnommée 
"Wheezy".

Cette nouvelle version de Debian contient diverses fonctionnalités 
intéressantes, telles que:

- la prise en charge **multiarchitecture**, 
- plusieurs outils pour déployer des nuages privés, 
- un installateur amélioré et un ensemble complet de codecs et d'interfaces 
  multimédia qui suppriment le besoin de dépôts tiers.

Prise en charge multiarchitecture
---------------------------------

.. seealso::

   - :ref:`multi_arch_debian`

La prise en charge multiarchitecture, un des objectifs principaux de 
publication pour "Wheezy", permettra aux utilisateurs de Debian d'installer 
des paquets pour différentes architectures sur le même système. 
Cela signifie qu'il est maintenant possible, pour la première fois, 
d'installer à la fois des logiciels pour 64 et 32 bits sur la même machine 
avec toutes les dépendances pertinentes satisfaites.

Processus d'installation
------------------------

Le processus d'installation a été amélioré significativement : 
l'installation de Debian peut se faire à l'aide d'un logiciel de synthèse 
vocale, par exemple par les personnes malvoyantes ne disposant pas de 
périphérique braille. Le système d'installation pour Debian est maintenant 
disponible en 73 langues, dont plus d'une douzaine sont disponibles pour 
la synthèse vocale.
De plus, pour la première fois, Debian prend en charge l'installation et 
l'amorçage sur UEFI pour les PC 64 bits récents (amd64), même s'il n'y a 
pas encore de prise en charge pour l'amorçage sécurisé ("Secure Boot"). 


Debian fonctionne sur de nombreux ordinateurs, depuis les systèmes de 
poche jusqu'aux superordinateurs, et sur quasiment tous les systèmes 
intermédiaires. 
Au total, neuf architectures sont gérées : 

- PC 32 bits/Intel IA-32 (i386), 
- PC 64 bits/Intel EM64T/x86-64 (amd64), 
- Motorola/IBM PowerPC (powerpc), 
- Sun/Oracle SPARC (sparc), 
- MIPS (mips (gros-boutiste) et mipsel (petit-boutiste)), 
- Intel Itanium (ia64), 
- IBM S/390 (s390 sur 31 bits et s390x sur 64 bits) 
- et ARM EABI (armel pour du matériel plus ancien et armhf pour du 
  matériel récent avec unité de calcul flottant). 


