


.. _cr_agopian_pytong_2013:

==========================================
Compte-rendu Mathieu Agopian pytong 2013
==========================================

.. seealso::

   - http://mathieu.agopian.info/blog/retour-sur-pytong-2013.html
   - https://twitter.com/magopian
   - :ref:`cr_remy_pytong_2013`


.. contents::
   :depth: 3

Introduction
=============

Le 22 et 23 juin, à Toulon, s'est tenue la première édition de Pytong, organisée 
par Laurent Paoletti et David Larlet (merci à eux !).

Le format a repris ce dont on a maintenant l'habitude pour les conférences Django 
organisées par django-fr, une première journée de conférences et barcamps, et 
une deuxième journée de détente ensemble pour apprendre à mieux se connaître.

Les présentations
==================

Reporting web et print
------------------------

.. seealso::

   - http://hashbang.fr/
   - http://hashbang.fr/static/medias/pytong_reporting/index.html
   
   
Arthur Vuillard nous a montré comment utiliser pygal pour faire de jolis reporting 
web avec de jolis graphes SVG annotés, et weasyprint pour un export en PDF propre, 
avec gestion des coupures de tableaux, centrage sur la page, etc...

Tu peux WebTest
----------------

.. seealso::

   - http://gawel.github.io/pytong2013_webtest/#/tu-peux-webtest

Gaël Pasgrimaud, mainteneur de l'excellente librairie WebTest (créée par le 
prolifique Ian Bicking), nous a expliqué comment l'utiliser pour tester nos 
applications WSGI. 
Ça peut avantageusement remplacer le Django Test Client, étant donné ses 
fonctionnalités avancées, sa facilité d'utilisation, et le fait que ça dialogue 
directement au niveau WSGI.


Des migrations sans interruption de service
---------------------------------------------

.. seealso::

   - http://polyconseil.github.io/presentations/no_downtime_migrations/
   
Thomas Chaumeny a listé plusieurs techniques et pratiques, ainsi que les pièges 
à éviter pour faire des migrations de schéma de données (principalement en utilisant South), 
et ce sans interruption de service. 

En effet, selon la migration, les changements dans la base de données peuvent 
bloquer une table (verrou en écriture) pendant plusieurs minutes, voire heures. 
Il y a donc certains pièges a éviter, et des méthodes à suivre.

Débuter avec salt
------------------

.. seealso::

   - https://twitter.com/gwadeloop
   - http://saltstack.com/
   
Yann Malet nous a fait une rapide présentation de Salt, un gestionnaire de 
configuration, un framework d'installation et d'exécution à distance. 

Pour ceux qui connaissent Chef ou Puppet, Salt est un remplaçant écrit en Python, 
très performant, car basé sur ZMQ.

Il a ensuite expliqué comment, à LincolnLoop, ils ont utilisé Salt en tant que 
framework d'exécution à distance pour leur nouveau projet de monitoring : Salmon.

Déprimé, au bord du burn-out, et pourtant il faut continuer à coder
--------------------------------------------------------------------

.. seealso::

   - https://speakerdeck.com/mrjmad/deprime-au-bord-du-burn-out-et-pourtant-il-faut-continuer-a-coder

Jean-Michel Armand nous a fait part de son expérience de surmenage, de comment 
il s'en est sorti, et comment il essaie de ne plus se mettre en danger physiquement 
et psychologiquement. 

Un paquet de conseils avisés, à suivre avant qu'il ne soit trop tard.

On dit souvent qu'il faut vivre ses propres expériences pour pouvoir en apprendre, 
et j'ai moi-même vécu une expérience similaire. 

Les conseils donnés dans cette présentation sont précieux, et peuvent se résumer 
à **vous valez mieux que votre code/travail, vivez**.

Mezzanine, le CMS des développeurs pragmatiques
------------------------------------------------

.. seealso::

   - http://miximum.fr/
   - http://mezzanine.jupo.org/


Thibault Jouannic nous a parlé de Mezzanine, un CMS simple, performant et facilement 
extensible, qui permet de répondre à des demandes simples sans avoir à installer 
un Drupal ou Wordpress.

Use ZMQ and Tornado for fun and profit
---------------------------------------

.. seealso::

   - http://feldboris.alwaysdata.net/blog/
   - https://speakerdeck.com/lothiraldan/use-omq-and-tornado-for-fun-and-profits

Boris Feld nous a donné des recettes pour utiliser ZMQ avec Tornado pour faire 
le lien avec HTTP.

Use ZMQ and Tornado for fun and profit, les slides.


Écriture d'un livre sur Django
-------------------------------

.. seealso::

   - https://twitter.com/boblefrag
   - http://fr.slideshare.net/YohannGabory/pytong-2013

Yohann Gabory nous a parlé de son expérience d'écriture d'un livre sur Django : 
Django avancé. 

Il en a profité pour nous expliquer comment écrire une bonne documentation 
utilisateur, pour lui donner envie d'utiliser notre projet/librairie/application...

Python dans le navigateur, et pourquoi pas
-------------------------------------------

.. seealso::

   - http://j-mad.com/
   - http://brython.info/
   
   
Jean-Michel Armand nous a fait une démonstration de Brython, vu que toute sa 
présentation était faite avec. 

Brython a pour ambition de remplacer JavaScript dans le navigateur par le 
langage Python.

Python(Script) par Python pour le navigateur
---------------------------------------------

.. seealso::

   - https://plus.google.com/116302792447642827163/posts
   - https://pythonscript.readthedocs.org/

Amirouche Boubekki nous a parlé de son projet PythonScript, une autre alternative 
à Brython pour avoir du Python dans le navigateur.

JavaScript pour les développeurs Python
----------------------------------------

.. seealso::

   - https://twitter.com/n1k0

Nicolas Perriault a pris à revers les deux précédentes présentations courtes : 
il explique qu'il est inutile et futile de vouloir remplacer le langage qui a 
été prévu exprès pour manipuler le DOM et être asynchrone (à base de callbacks), 
exprès pour être exécuté dans les navigateurs.

Le pragmatisme du développeur Python voudrait justement qu'il utilise les bons 
outils pour les bonnes utilisations, et donc JavaScript pour du code dans le 
navigateur.

Développer une app Django
--------------------------

.. seealso::

   - https://twitter.com/ouhouhsami
   - https://github.com/ouhouhsami/django-select2light
   - http://django-floppyforms.readthedocs.org/en/latest/
   - http://tastypieapi.org/
   - https://raw.github.com/ouhouhsami/pytong2013-LT-django-app-development-/master/slides.txt
   
Samuel Goldszmidt s'est servi de l'exemple de son application Django-Select2Light 
pour montrer comment créer une application Django, en utilisant FloppyForms et 
TastyPie.


Utiliser un système de packaging privé
---------------------------------------

.. seealso::

   - http://buildout.org/
   - http://mathieu.agopian.info/blog/le-miroir-pypi-du-pauvre.html

Brice Gelineau nous a expliqué comment il utilisait un système de packaging 
privé pour son déploiement. 

C'est encore une autre alternative à l'utilisation de Buildout ou encore le 
mirroir PyPI privé dont j'ai eu l'occasion de parler lors d'une précédente 
conférence.

À quoi ressemblerait mon python ?
----------------------------------

.. seealso::

   - https://twitter.com/duboisnicolas
   - http://git.nicolasdubois.com/talks/2013-pytong/

Nicolas Dubois s'est demandé comment améliorer encore la lisibilité de nos 
programmes Python. 

Il s'avère qu'avec quelques judicieuses modification, et l'utilisation de 
caractères Unicode par exemple, nous pourrions avoir du code source encore plus 
concis et expressif.

Il y a peu de chances que nous ayons un interpréteur Python comprenant cette 
syntaxe un jour, mais je trouve très intéressant de se poser ce genre de questions, 
et nous avons commencé a écrire « BMC » (Beautify My Code) avec Nicolas, petite 
librairie (service ?) qui permet d'opérer des changements/remplacements sur un 
fichier source et d'afficher le résultat. À suivre donc.


Daybed, une couche de validation pour CouchDB
----------------------------------------------

.. seealso::

   - http://blog.antoine.cezar.fr/
   - http://daybed.readthedocs.org/en/latest/
   - https://github.com/AntoineCezar/pytong-2013-daybed-slides

Antoine Cezar nous a présenté le projet Daybed dont il est un des contributeurs. 

Cette surcouche à CouchDB, qui ajoute la validation de données, permet d'avoir 
un remplaçant à GoogleForms.

Les barcamps
------------

Les Web Components
+++++++++++++++++++

.. seealso::

   - https://larlet.fr/david/
   - https://github.com/mozilla/xtags-org/tree/master/public
   - http://www.polymer-project.org/

Il y a eu un premier barcamp proposé par David Larlet qui a fait l'unanimité 
(oui, c'est bizarre d'avoir un seul et unique barcamp, ça s'oppose un peu à la 
loi des deux pieds) : une présentation des Web Components.

Les Web Components ont à l'heure actuelle deux implémentations : celle de Mozilla 
avec xtags, et celle de Google avec polymer. 

Ce sont des composants qui peuvent être entièrement packagés et distribuables : html, 
css et JavaScript en un seul morceau.

Ça me laisse une sorte d'impression de déjà vu, comment si on revenait aux années 
sombres des « clients lourds » avec GUI, composants et widgets, etc... je vois 
néanmoins l'intérêt que ces Web Components apportent alors qu'on déporte de plus 
en plus de logique et de calcul sur le client, et qu'on cherche à avoir des 
applications web de plus en plus proches, justement, des applications natives.

Comprendre "this" en JavaScript
+++++++++++++++++++++++++++++++

.. seealso::

   - http://benalman.com/news/2010/11/immediately-invoked-function-expression/
   - http://ejohn.org/apps/learn/

Suite à sa présentation courte sur « JavaScript pour les développeurs Python », 
Nicolas Perriault a indiqué les différentes utilisations et manières de spécifier 
this en JavaScript, ainsi que les IIFE et use strict.

J'avais déjà eu la chance de me pencher sur l'utilisation de this grâce à un lien 
que Nicolas m'avait fourni : Learning advanced JavaScript.

Maitriser git
++++++++++++++


Proposé par Thibault Jouannic, je n'ai pu y participer ayant assisté au barcamp 
ci-dessus, mais j'en ai eu de bons retours.


La journée détente
===================

Au programme :

- plage + baignade : pour les plus courageux, l'eau n'étant pas très chaude, et le vent était assez violent et frais
- slackline : première fois pour moi, génial ! J'ai hâte de pouvoir en refaire
- repas : bon, convivial, à l'ombre des mûriers platane, vue sur la mer, que demander de plus
- jeux de société : Dixit, Pandémie
- pétanque
- marshmallow challenge animé par Stéphane Langlois.Sympa de voir la rétrospective, 
  sur comment les enfants ont parfois de meilleurs résultats que les jeunes 
  ingénieurs ou commerciaux !

Conclusion
===========

.. seealso::

   - http://tech.novapost.fr/pytong-2013-a-toulon-le-resume.html
   
   
C'est toujours un vrai plaisir de pouvoir rencontrer ses pairs, apprendre d'eux, 
faire des connaissance, échanger des astuces et techniques. 

Je pense que c'est un investissement indispensable à tout développeur passionné 
et curieux qui souhaite évoluer et rester au courant des avancées dans son domaine.

Vous pouvez par ailleurs consulter le compte rendu de Rémy.

Enfin, en petit bonus, je vous met le lien vers la présentation courte que 
j'avais préparée « au cas où », mais que je n'ai pas eu l'occasion de montrer: 
`Sécuriser ses données`_


.. _`Sécuriser ses données`:  http://mathieu.agopian.info/presentations/2013_06_pytong/




