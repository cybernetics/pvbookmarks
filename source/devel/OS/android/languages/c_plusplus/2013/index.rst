

.. index::
   pair: Android; C++


.. _android_cplusplus_2013:

=========================
Android C++ 2013
=========================

.. contents::
   :depth: 3


Il y a un article sur GNU/Linux magazine N°156 de janvier 2013 intitulé
"Programmer Android avec Qt4".

Quelques extraits
=================

Dans un article précédent, nous avons considéré la programmation d'une
application pour systèmes Android en pur C++, ce qui s'était révélé,
disons, insatisfaisant. Aujourd'hui, nous allons voir comment obtenir
quelque chose de bien plus gratifiant en nous appuyant ni plus ni moins
sur la bibliothèque C++ Qt4 - et sans écrire une ligne de Java ni invoquer
explicitement le JNI.


... cette prouesse est le résultat de l'énorme travail initié par 
BogDan Vatra (http://www.behindkde.org/bogdan-vatra-0)  qui a abouti à 
la communauté du projet Necessitas (http://necessitas.kde.org).
En plus du "simple" portage de Qt4 sur Android, Necessitas fournit une
infrastructure complète pour le développement Qt ciblant Android depuis 
le compilateur jusqu'à l'environnement de développement Qt-Creator
légèrement adapté, en passant par un SDK/NDK légèrement modifié....


... le plus critique est le choix du (ou des) SDK Android à installer,
les fameux "niveaux d'API"...

... l'objectif premier de Necessitas est de permettre à un développeur
C++/Qt de travailler presque "normalement", c'est à dire comme s'il était
sur un système bureau....

... en plus de cette structure, du code Java va être automatiquement
généré pour établir le pont entre l'API Android et les fonctions invoquées 
par les bibliothèques Qt, au moyen du JNI. Finalement, votre application
va être stockée dans un fichier de bibliothèque partagée (lib*.so), la 
fonction main() étant invoquée par un emballage ("wrapper") qui est un 
programme Android "sauce officielle", produit par Necessitas.
 









