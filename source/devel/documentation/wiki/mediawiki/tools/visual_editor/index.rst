


.. index::
   pair: Visual Editor ; Wikimedia

.. _visual_editor:

=======================
Visual Editor
=======================

.. seealso::

   - https://www.mediawiki.org/wiki/VisualEditor


.. contents::
   :depth: 3


Introduction
============

The VisualEditor project aims to create a reliable rich-text editor for MediaWiki.

It is being developed so it can be used as a MediaWiki extension, using the
Parsoid project to supply HTML+RDFa.

It is currently deployed to a test namespace of this wiki; more information
about this test deployment can be found on Wikimedia's blog, the FAQs, and
VisualEditor:Welcome or VisualEditor:Test. Please note that the test deployment
only works with the Vector skin.


Annonces
========

Linux-fr
--------

.. seealso::

   - http://linuxfr.org/news/lancement-de-l-editeur-visuel-de-mediawiki



Sûrement motivée par la nouvelle interface de linuxfr.org et afin d'attirer un
nombre plus grand de contributeurs au projet Wikipedia, la fondation Wikimedia
a développé le logiciel open-source VisualEditor.

Il s'agit de proposer une interface WYSIWYG (ce que vous voyez est ce que vous
obtenez) au moteur Wiki de la fondation afin de ne pas obliger les contributeurs
potentiels à apprendre la syntaxe wikitexte.

La première version utilisable avait été présentée en juin dernier, il s'agissait
plus d'un démonstrateur aux fonctionnalités très limitées que d'une version alpha.

Ce 12 décembre, l'équipe a annoncé sur le blog wikimedia le lancement de la version
alpha du projet.

Cette version n'est disponible que depuis la version anglaise de Wikipedia et,
ce, pour les utilisateurs enregistrés qui auront activés l'option dans leurs
préférences (option désactivée par défaut). Il s'agit d'une version de test,
le but étant donc de faire des retours à l'équipe.

Une fois l'option activée, pour chaque article, il est possible d'éditer en
passant par un onglet un second éditeur étiqueté « VisualEditor » à côté de
l'onglet « Modifier ».

En cliquant sur cet onglet, après une petite pause vous entrerez dans le VisualEditor.

De là, vous pouvez jouer, éditer et enregistrer des articles réels et avoir une
idée de ce que sera l'article lorsque vous avez terminé.

À ce stade précoce du développement, il est recommandé de réaliser des
vérifications après avoir sauvegardé pour s'assurer que rien n'a été cassé.

Toutes les modifications faites par VisualEditor seront affichées dans les onglets
Histoire des articles avec un tag VisualEditor à côté d'eux, afin qu'il soit
possible de suivre ce qui se passe.

Cette version reste limitée en fonctionnalités tel qu'indiqué dans la page
VisualEditor et l'équipe rencontre des difficultés avec le langage wikitexte
qui n'a cessé d'évoluer depuis le lancement de Wikipedia.

Ceci a nécessité le développement de Parsoid afin de convertir les anciens
fichiers dans un format qui convient à VisualEditor pour être ensuite reconverti
en wikitexte.
Les tests réalisés ont été concluant dans 80% des cas et 18% des cas ont été
légèrement différents. Les développeurs disent qu'ils ont l'intention d'améliorer
significativement ces pourcentages, et la vitesse de Parsoid, au cours des
prochains mois.

Selon le calendrier actuel, VisualEditor est prévu pour être l'éditeur par
défaut de presque tous les projets Wikimedia à partir de juillet 2013.
