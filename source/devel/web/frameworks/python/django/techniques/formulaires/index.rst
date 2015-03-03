
.. index::
   pair: Django; Forms 



.. _django_forms:

====================
Django forms
====================

.. seealso::

   - https://docs.djangoproject.com/en/dev/ref/forms/api/
   - https://docs.djangoproject.com/fr/1.6/ref/forms/api/


.. contents::
   :depth: 3

Introduction
============

.. seealso::

   - https://docs.djangoproject.com/en/dev/topics/forms/
   - https://docs.djangoproject.com/fr/1.6/topics/forms/

This document provides an introduction to Django’s form handling features. 

For a more detailed look at specific areas of the forms API, see:

- The Forms API, 
- Form fields, 
- and Form and field validation.

Ce document présente une introduction aux fonctionnalités de formulaires avec 
Django. 

Pour plus de détails sur des aspects spécifiques de l’API des formulaires, 
consultez 

- The Forms API, 
- Form fields et 
- Form and field validation.

django.forms est la bibliothèque de gestion des formulaires de Django.

Même s’il est possible de traiter les envois de formulaires en utilisant 
simplement la classe HttpRequest de Django, l’utilisation de la bibliothèque 
de formulaires se charge d’un certain nombre de tâches liées aux formulaires. 

Avec cette bibliothèque, vous pouvez :

- Afficher un formulaire HTML contenant des composants de formulaires générés 
  automatiquement.
- Vérifier les données envoyées par un ensemble de règles de validation.
- Réafficher le formulaire en cas d’erreurs de validation.
- Convertir les données de formulaires envoyées dans les types Python appropriés.

Aperçu
-------

La bibliothèque se base sur ces concepts :

Composant

    Une classe correspondant à un composant de formulaire HTML, par exemple 
    <input type="text"> ou <textarea>. L’affichage du composant en HTML est 
    aussi pris en charge.
    
Champ

    Une classe responsable de la validation, par exemple un champ EmailField 
    qui s’assure que ses données correspondent à une adresse électronique valable.
    
    
Formulaire

    Un ensemble de champs qui savent comment valider leur contenu et s’afficher 
    sous forme de code HTML.
    
    
Fichiers annexes des formulaires (classe Media)

    Les ressources CSS et JavaScript requises pour afficher un formulaire.


Tutorials
==========


.. toctree::
   :maxdepth: 3
   
   tutorials/index
   

