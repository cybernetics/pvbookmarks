

.. index::
   pair: RTOS ; Linux-RT
   ! Linux-RT


.. _linux_rt:

==============================
Linux RT
==============================

.. seealso::

   - http://fr.wikipedia.org/wiki/Linux-rt
   - https://rt.wiki.kernel.org/index.php/Main_Page

.. contents::
   :depth: 3

Introduction
============

Linux-rt (où RT signifie en anglais « Real Time », littéralement « Temps Réel ») 
est une branche du noyau Linux initiée par Ingo Molnar dans le but de 
répondre aux contraintes d'un système temps réel.

L'application du patch officiel PREEMPT-RT sur le noyau Linux standard 
lui confère des fonctionnalités temps réel.

Un tel noyau est par exemple fourni en option par la distribution Ubuntu, 
et est au cœur de la distribution Demudi Linux.


Principe d'action du patch PREEMPT_RT
======================================

Ce patch a pour effet de donner au noyau Linux un comportement temps 
réel dur, tout en limitant le nombre de modifications apportées. 

Une partie des fonctionnalités ajoutées par Ingo Molnar ont depuis été 
introduites directement dans le noyau.

Il agit en rendant préemptible la majeure partie du code du noyau, et en 
particulier les sections critiques, les gestionnaires d'interruptions. 

Il modifie par ailleurs certains mécanismes pour réduire les temps de 
latence induits par le fonctionnement du système.

Ce patch met aussi en place un mécanisme de protection contre le problème 
connu sous le nom d'"inversion de priorité", par l'utilisation de sémaphore 
à héritage de priorité.

Comparaison avec la concurrence
===============================

Par rapport à des extensions concurrentes du noyau Linux tels que Xenomai 
ou RTAI, il ne fait que modifier le fonctionnement du noyau standard sans 
ajouter un second noyau ou une couche de virtualisation temps réel, ce qui 
simplifie et allège le système résultant.

Il n'ajoute aucune interface de programmation spécifique, utilisant 
l'API POSIX standard, et ne requiert par là même aucune modification 
d'une application existante. 

Un programme prévu pour fonctionner sur un noyau Linux conventionnel 
fonctionnera donc naturellement sur linux-rt et en tirera immédiatement 
certains bénéfices (temps de latence réduits) sans aucune re-compilation.



