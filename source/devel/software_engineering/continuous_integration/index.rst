
.. index::
   pair: Software Engineeering; Continuous Integration
   pair: Continuous ; Integration
   ! Continuous Integration
   ! CI

.. _continuous_integration:

========================
Continuous integration
========================


.. seealso::

   - http://en.wikipedia.org/wiki/Continuous_integration
   - http://fr.wikipedia.org/wiki/Int%C3%A9gration_continue


.. contents::
   :depth: 3

Introduction
=============

L'intégration continue est un ensemble de pratiques utilisées en génie 
logiciel consistant à vérifier à chaque modification de code source que 
le résultat des modifications ne produit pas de régression dans 
l'application développée. 

Bien que le concept existât auparavant[réf. nécessaire], l'intégration 
continue se réfère généralement à la pratique de l'extreme programming.

Pour appliquer cette technique, il faut d'abord que :

- le code source soit partagé (en utilisant des logiciels de gestion de 
  versions tels que CVS, Subversion, git, Mercurial, etc)
- les développeurs intègrent (commit) quotidiennement (au moins) leurs 
  modifications
- des tests d'intégration soient développés pour valider l'application 
  (avec JUnit par exemple)

Ensuite, il faut un outil d'intégration continue tel que CruiseControl 
ou Jenkins (anciennement Hudson) pour le langage Java par exemple.

Les principaux avantages d'une telle technique de développement sont :

- le test immédiat des unités modifiées
- la prévention rapide en cas de code incompatible ou manquant
- les problèmes d'intégration sont détectés et réparés de façon continue, 
  évitant les problèmes de dernière minute une version est toujours 
  disponible pour un test, une démonstration ou une distribution
  
  
Tools
=====

.. toctree::
   :maxdepth: 3
   
   tools/index
   
     

