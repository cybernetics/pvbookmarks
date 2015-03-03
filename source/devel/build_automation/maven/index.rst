


.. index::
   pair: Building tool ; Maven
   ! Maven


.. _maven_building_tool:
.. _maven:


======
maven
======

.. image:: apache-maven-project-2.png.jpg
.. image:: maven-logo-2.gif.jpg

.. seealso::

   - http://maven.apache.org/
   - http://maven.apache.org/what-is-maven.html
   - http://maven.apache.org/download.html
   - http://en.wikipedia.org/wiki/Maven
   - http://fr.wikipedia.org/wiki/Apache_Maven


Prelude
========

A maven (also mavin) is a trusted expert in a particular field, who seeks to
pass knowledge on to others.
The word maven comes from the Hebrew (עברית), via Yiddish, and means one who 
understands, based on an accumulation of knowledge

Apache Maven est un outil logiciel libre pour la gestion et l'automatisation de
production des projets logiciels Java en général et Java EE en particulier.

L'objectif recherché est comparable au système Make sous Unix : produire un
logiciel à partir de ses sources, en optimisant les tâches réalisées à cette
fin et en garantissant le bon ordre de fabrication.

Il est semblable à l'outil Ant, mais fournit des moyens de configuration
plus simples, eux aussi basés sur le format XML.
Maven est géré par l'organisation Apache Software Foundation.
Précédemment Maven était une branche de l'organisation Jakarta Project.


Introduction
============

.. seealso:: http://maven.apache.org/what-is-maven.html

Maven, a Yiddish word meaning accumulator of knowledge, was originally started
as an attempt to simplify the build processes in the Jakarta Turbine project.
There were several projects each with their own Ant build files that were all
slightly different and JARs were checked into CVS. We wanted a standard way to
build the projects, a clear definition of what the project consisted of,
an easy way to publish project information and a way to share JARs across
several projects.

The result is a tool that can now be used for building and managing any
Java-based project. We hope that we have created something that will make
the day-to-day work of Java developers easier and generally help with the
comprehension of any Java-based project.

Maven's Objectives
==================

Maven's primary goal is to allow a developer to comprehend the complete state
of a development effort in the shortest period of time. In order to attain this
goal there are several areas of concern that Maven attempts to deal with:

- Making the build process easy
- Providing a uniform build system
- Providing quality project information
- Providing guidelines for best practices development
- Allowing transparent migration to new features

Maven does encourage best practices, but we realise that some projects may not
fit with these ideals for historical reasons. While Maven is designed to be
flexible, to an extent, in these situations and to the needs of different projects,
it can not cater to every situation without making compromises to the integrity
of its objectives.


Project Object Model (POM)
==========================

Chaque projet ou sous-projet est configuré par un POM qui contient les
informations nécessaires à Maven pour traiter le projet (nom du projet,
numéro de version, dépendances vers d'autres projets, bibliothèques
nécessaires à la compilation, noms des contributeurs etc.).

Ce POM se matérialise par un fichier pom.xml à la racine du projet. Cette
approche permet l'héritage des propriétés du projet parent. Si une propriété
est redéfinie dans le POM du projet, elle recouvre celle qui est définie dans
le projet parent. Ceci introduit le concept de réutilisation de configuration.
Le fichier pom du projet principal est nommé pom parent.


Examples
========

javacl maven project
--------------------

.. seealso:: http://code.google.com/p/javacl/wiki/GettingStarted




