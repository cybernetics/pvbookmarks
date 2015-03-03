

.. index::
   pair: RTOS ; Xenomai
   ! Xenomai
   ! Adeos


.. _xenomai:

==============================
Xenomai
==============================

.. seealso::

   - http://fr.wikipedia.org/wiki/Xenomai


Introduction
============

Xenomai est une extension libre du noyau Linux lui apportant des 
fonctionnalités **temps réel dures**. 

Il apporte une approche symétrique entre programmation noyau et programmation 
système au niveau utilisateur sous Linux.

Il introduit le concept de machine virtuelle en programmation temps réel 
et permet ainsi de disposer de plusieurs interfaces de programmation, au 
choix du programmeur.

Aspect techniques
=================

Xenomai utilise la couche de virtualisation Adeos.

Il se présente sous la forme d'un patch logiciel à installer 'par-dessus' 
(ie après l'installation de) le noyau Linux choisi.


Adeos
======

.. seealso::

   - http://fr.wikipedia.org/wiki/Adeos
   - http://home.gna.org/adeos/
   
Adeos (Adaptive Domain Environment for Operating Systems) est logiciel 
hyperviseur créé par Philippe Gerum en 2003 et **destiné à partager les 
ressources matérielles entre divers systèmes d'exploitation**. 

Il est utilisé conjointement à Linux afin de lui permettre d'ajouter des 
fonctionnalités temps-réel dures dans les projets RTAI et Xenomai.

Originellement créé par Philippe Gerum en 2003 pour contourner le brevet 
déposé par Victor Yodaiken et Michael Barabanov de FSMLabs concernant une 
technique triviale utilisée dans RTLinux, Adeos est basé sur une idée 
originale de Karim Yaghmour publiée dans un article de février 2002.


   
