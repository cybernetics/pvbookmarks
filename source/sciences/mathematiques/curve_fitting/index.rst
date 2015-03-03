

.. index::
   pair: Curve; Fit
   pair: Scipy; FittingData

.. _curve_fit:

==============
Curve fitting
==============


.. seealso::

   - http://www.miscel.dk/MiscEl/miscelCurveFit.html


.. contents::
   :depth: 3

Engauge Digitizer
=================

.. seealso::

   - http://digitizer.sourceforge.net/

Why Would You Need This Tool ?
-------------------------------

Here are some real-life examples:

- You are an engineer with some graphs in decades-old documents, but you really
  need the numbers represented in those graphs so you can do analyses that will
  determine if a space vehicle is safe to fly.
- You are a graduate student gathering historical data from charts for your thesis.
- You are a webmaster with visitor statistics charts and you want to do statistical analyses.
- You ride a bike or boat and want to know how much distance you covered in your
  last trip, but you do not have an odometer or GPS unit. However, you do have a map.

Nice Features
-------------

- Automatic curve tracing of line plots
- Automatic point matching of point plots
- Automatic axes matching
- Automatic grid line removal for improved curve tracing
- Handles cartesian, polar, linear and logarithmic graphs
- Support for drag-and-drop and copy-and-paste makes data transfer fast and easy
- Image processing tools highlight data by removing grid lines and backgrounds
- Status bar suggestions guide beginners
- Context sensitive popup help windows reveal explain feature of the user interface
- Tutorials with pictures explain strategies for common operations
- Browser-based user manual is extensive yet easy to navigate
- Preview windows give immediate feedback while modifying settings
- Dates and times are imported with the Date/Time Converter
- Import support for common image file formats such as BMP, GIF, JPEG, PNG and XPM
- Export support for common software packages such as Microsoft Excel, OpenOffice CALC,
  gnuplot, gnumeric, MATLAB and Mathematica
- Engauge is available for a wide variety of platforms (Linux, Mac OSX, Windows)
- Engauge Digitizer is completely open source and free courtesy of Sourceforge,
  Trolltech and FFTW


Problem
-------

nerick a écrit::

    j'ai la courbe suivante : [...]


    J'aimerais trouver une formule permettant d'approximer la courbe
    orange, mais je n'ai jamais fait ça...



Oh, un un problème de fit empirique, j'aime bien ce genre de problèmes.
;-) Voici ma démarche :

La première chose à faire est d'extraire de la courbe les données
numériques. Tu peux utiliser pour cela un logiciel tel que Engauge
Digitizer [1] ou g3data [2]. On obtient alors un tableau de points
(x, y) dans un fichier TSV.

Ensuite, je trace ça avec Gnuplot [3], et je trace par dessus des
fonctions qui ont la même allure (racine carrée, logarithme..) dont
j'ajuste les paramètres pour essayer de me rapprocher des données
expérimentales. C'est une sorte de « fit à la main », et c'est la partie
un peu artistique de la méthode. Si un fit a l'air de marcher, je peux
l'affiner automatiquement avec la fonction "fit" de gnuplot.

Quand j'ai une fonction qui a une bonne tête, je transforme les données
pour faire une droite. Par exemple, si le fit est

    y = a*log(x)+b

alors je trace y en fonction de log(x), qui devrait être une droite. Les
données numériques devraient donner aussi quelque chose de
raisonnablement bien aligné. Je trace aussi l'erreur de fit. Si cette
erreur est une fonction assez douce, alors c'est gagné, il suffit de
fiter un polynôme dessus, ça devrait marcher avec un degré pas trop
élevé. Si par contre l'erreur semble avoir une singularité à l'une des
extrémités de la courbe... alors il faut essayer une autre fonction.
Éventuellement on peut regarder l'erreur relative au lieu de l'erreur
absolue, auquel cas on obtiendra une correction multiplicative au lieu
d'une correction additive.


Hervé de Dianous a écrit::

    Bref, tu as les coordonnées de points et tu veux connaître l'équation
    qui contiendrait ces points ... Ca existe depuis la fin du XVIII-ième
    siècle grâce à notre compatriote Mr Lagrange [...]


Oui, mais il est aussi connu que ça marche très mal dès que tu as plus
de 4 ou 5 points [1]. Plutôt qu'une interpolation, il vaut mieux dans un
cas comme ça faire un ajustement (un « fit »), avec un polynôme de degré
largement inférieur au nombre de points de données. Et c'est encore
mieux si tu peux, en amont, transformer les données pour qu'elles
ressemblent davantage à un polynôme.

Si tu tiens à l'interpolation de Lagrange, alors il faut bien choisir
les abscisses auxquelles tu échantillonnes la courbe. Les abscisses de
Tchebychev [2] marchent bien en général.

Edgar.

- [1] http://fr.wikipedia.org/wiki/Phénomène_de_Runge
- [2] http://fr.wikipedia.org/wiki/Polynôme_de_Tchebychev

g3data
======

.. seealso::

   - http://www.frantz.fi/software/g3data.php


scipy
=====

C est un tres vaste sujet. Comme Remi indique les tableurs ont
des fonctions integrees pour ca.

Mais si tu cherches un outil du point de vue programmeur, tu peux utiliser
python et scipy: http://www.scipy.org/Cookbook/FittingData




