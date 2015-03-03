
.. index::
   ! Tests


.. _tests_quality:

=========
Les tests
=========


.. seealso::

   - https://fr.wikipedia.org/wiki/Test_%28informatique%29
   - http://www.cftl.net/cms/files/Dokumente/frGlossaire%20des%20tests%20de%20logiciel%20-%20ISTQB.pdf
   - https://fr.wikipedia.org/wiki/ISO_9126


.. contents::
   :depth: 3


Constats
========

- plus une erreur est détectée tard plus elle est coûteuse à corriger
- le logiciel est un produit où le défaut semble tolérable
- le test souffre souvent en premier des dépassements de délai.
- le test se résume trop souvent à de la simple validation placée en bout
  de chaîne dans le cycle de développement.
- le développement n'est pas piloté par les tests:

  * exigences rédigées sans se soucier de leur testabilité
  * spécifications volatiles et non gérées efficacement (Ingénierie des Exigences)


Comité français du test logiciel
================================

.. toctree::
   :maxdepth: 3
   
   cftl/index


Rôle du test
============

Le test a pour objectif de détecter les anomalies d'un logiciel.

Quelques principes pour les tests
=================================

- 1: le test montre la présence de défauts, pas leur absence
- 2: tester de façon exhaustive n'est pas possible
- 3: le test doit démarrer le plus tôt possible dans le cycle de développement
- 4: un développeur ne doit pas tester ses propres programmes
- 5: la définition des sorties ou résultats attendus doit être réfléchie avant
     l'exécution des tests (plan de tests)
- 6: les jeux de tests doivent être écrits pour des entrées invalides ou
     incohérentes aussi bien que pour des entrées valides.


Les niveaux de tests
====================

Tests unitaires
----------------

Documents de départ:

* plan de tests unitaires
* spécification de test du module
* conception détaillée

Tests d'intégration
--------------------

Documents de départ:

* plan de tests d'intégration
* spécification de test de validation
* conception architecturale

Tests systèmes
---------------

.. seealso::

   - https://fr.wikipedia.org/wiki/Test_de_validation
   

Documents de départ:

* plan de tests de validation_ du système
* spécification du système
* manuel utilisateur et d'exploitation
* exigences fonctionnelles


.. _validation: https://fr.wikipedia.org/wiki/Test_de_validation



tests d'acceptation
--------------------



Types de tests 
================

.. toctree::
   :maxdepth: 4

   types_tests/index



