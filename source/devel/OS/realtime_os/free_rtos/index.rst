

.. index::
   pair: RTOS ; FreeRTOS
   ! FreeRTOS


.. _free_rtos:

==============================
FreeRTOS
==============================

.. seealso::

   - http://fr.wikipedia.org/wiki/FreeRTOS
   - https://rt.wiki.kernel.org/index.php/Main_Page


.. figure:: FreeRTOS_Logo.jpg
   :align: center
   

Introduction
============

FreeRTOS est un système d'exploitation temps réel (RTOS) faible empreinte, 
portable, préemptif et Open source pour **microcontrôleur**. 

Il a été porté sur 33 architectures différentes. 

Créé en 2003 par Richard Barry et la FreeRTOS Team, il est aujourd’hui 
le leader du marché des systèmes d'exploitation temps réel.

FreeRTOS est disponible gratuitement sous une licence GPL modifiée et 
utilisable sans paiement de redevances, cette licence n’oblige pas les 
développeurs à publier le code de leurs logiciels applicatifs mais impose 
de garder le noyau de FreeRTOS Open Source. 

Une licence commerciale avec le support ad hoc (OpenRTOS) est également 
proposée par la société High Integrity Systems.

Le nombre de tâches exécutées simultanément et leur priorité n'est limité 
que par le matériel. L'ordonnancement est un système de file d'attente 
basée sur les Sémaphores et les Mutex. 

Il est basé sur le modèle Round-Robin avec gestion des priorités. 

Conçu pour être très compact, il n'est composé que de quelques fichiers 
en langage C et n'implémente aucun pilote matériel.

Les domaines d'applications sont assez larges car les principaux avantages 
de FreeRTOS sont l’exécution temps réel, un code source ouvert et une 
taille très faible. 

Il est donc utilisé principalement pour les systèmes embarqués qui ont 
des contraintes d'espace pour le code mais aussi pour des systèmes de 
traitement vidéo et des applications réseau qui ont des contraintes 
"temps réel".


