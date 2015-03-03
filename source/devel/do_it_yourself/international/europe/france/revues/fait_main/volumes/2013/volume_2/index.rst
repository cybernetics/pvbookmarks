.. index::
   pair: FaitMain; Raspberry
   pair: Météo; Yoctopuce
   pair: Météo; Grenouille
   pair: Géo; Localisation;

.. _volume_2_fait_main_2013:

================================================
Volume 2 "Fait main" 2013
================================================


.. seealso::

   - http://faitmain.org/volume-2/edito.html
   - https://github.com/faitmain/faitmain.org/blob/master/src/volume-2/edito.rst
   - https://github.com/faitmain/faitmain.org/tree/master/src/volume-2
   - http://faitmain.org/volume-2/faitmain-volume-2.pdf
   
   
.. contents::
   :depth: 3
   
Edito
======

.. seealso::

   - http://faitmain.org/volume-2/edito.html
   - https://github.com/faitmain/faitmain.org/blob/master/src/volume-2/edito.rst

Bienvenue dans le deuxième numéro du magazine Fait Main. Trois mois se sont
écoulés depuis le précédent numéro et il s'est passé énormément de choses
dans le projet depuis.

Comme vous pouvez le constater, le look a changé, grâce au travail de
`Raphaël Bastide <http://raphaelbastide.com/>`_, qui a rejoint l'équipe des
contributeurs pour retravailler l'identité visuelle. Un style épuré,
conçu pour faciliter la lecture au maximum. Ce volume 2 est l'occasion
de commencer une transition graphique qui s'afinera à travers les
numéros et les supports. Vous pourrez en savoir plus sur le travail graphique
autour de Fait Main dans le numéro 3, ne le manquez pas !

Au niveau PDF, rien n'a changé par manque de temps. C'est toujours un
PDF spartiate qui est obtenu avec une moulinette. Les images sont
mal taillées mais le magazine reste lisible.
J'espère que le numéro 3 verra des évolutions sur ce front.

Niveau style et orthographe, il nous manque encore clairement un
gros boulot de fond - mais depuis la création de la
`liste de diffusion </mailing.html>`_ nous avons de plus en plus
de relecteurs qui s'attèlent à cette tâche.

Côté nouveauté, nous avons ajouté une page
`partenariat </partenariat.html>`_ qui propose à des constructeurs
ou revendeurs de matériel de s'associer à l'élaboration d'un
article de bidouille en envoyant du matériel.

Il y a aussi un `calendrier </calendrier.html>`_ qui liste les
évènements DIY de l'hexagone (ou autour).

Mais trêve de bavardages, parlons plutôt du contenu...

Contenu du volume 2
--------------------

David nous revient avec un article sur le `coût écologique
de vos données </volume-2/cout-ecologique-donnees.html>`_ qui
souhaite faire prendre conscience de l'impact de vos photos
oubliées au fond de votre disque dur.

On peut enchaîner sur `Comment réparer soi-même les Internets
</volume-2/ffdn.html>`_ par Damien Nicolas et compagnie, qui
présente les enjeux autours des fournisseurs d'accès internet
et une présentation de la Fédération FDN.

Fabien Batteix, qui tient un blog très intéressant sur la
bidouille électronique, s'est fendu d'un `article
sur le light painting </volume-2/light-painting.html>`_
qui explique le fonctionnement de sa *baguette magique*.

`Comment ouvrir une puce </volume-2/ouvrir-puce.html>`_
est la traduction d'un article en anglais sur lequel je suis tombé il
y a quelque temps sur le web, que j'ai trouvé assez impressionnant.
Zeptobar décortique des puces avec de l'acide chaud. Rien que ça.

Christophe Seyve nous explique comment fabriquer une `table
basse pliante et escamotable </volume-2/table_basse.html>`_
avec du matériel de récupération.

Jonathan Schemoul revient avec un article sur
`les batteries </volume-2/batterie.html>`_ dans les projets
électroniques. C'est un sujet qui m'a beaucoup intêressé car
j'ai du faire face à ce problème pour mon projet de
`station météo USB </volume-2/station-meteo.html>`_ avec
les puces Yoctopuce.

Fritz van Deventer, rencontré au FOSDEM, présente son travail
autour de `la surveillance des digues en
Hollande </volume-2/surveillance-digues.html>`_.

Vous avez tous entendu parler des Open Bidouille Camp.
Les lecteurs ont posé des `questions à Sabine Blanc </volume-2/sabine-blanc.html>`_,
qui est l'une des organisatrices.

On enchaîne sur un dossier sur les technologies sans fils
basées sur le protocole Zigbee. Un véritable `tour d'horizon d'X-Bee
& Arduino </volume-2/xbee-arduino.html>`_ par Jérôme Abel.

Amina El Kamel nous explique rapidement comment fonctionne
la `sérigraphie
sur textile <http://next.faitmain.org/volume-2/serigraphie.html>`_.

Enfin, un article qui présente `quelques livres </volume-2/quelques-livres.html>`_.
Pour ce dernier j'espère que le numéro 3 pourra inclure des revues
de livres par plus de contributeurs.

Le numéro 3 est prévu pour le 1er Août 2013.

En attendant, bonne Lecture et joyeuse bidouille!  
  
   
Station météo avec le raspberry (le projet Grenouille)
=======================================================

.. seealso::

   - https://github.com/faitmain/faitmain.org/blob/master/src/volume-2/station-meteo.rst
   - https://raw.github.com/faitmain/faitmain.org/master/src/volume-2/station-meteo.rst
   - :ref:`raspberry_pi_station_meteo_2013`
   - https://fr.wikipedia.org/wiki/Formule_du_nivellement_barom%C3%A9trique

   
Après la sortie du premier numéro de FaitMain, j'ai été
contacté par `Yoctopuce <http://yoctopuce.com>`__ qui
m'a proposé de tester son matériel dans un article.

Ca tombait plutôt bien puisque dans la (volumineuse) pile
des projets en attente de réalisation il y a la conception
d'une station météo.

Publier les courbes de température, pression atmosphérique
et humidité de mon jardin en Bourgogne, ne va intéresser que
ma mère qui vient de temps en temps jardiner chez moi.
Mais d'un point de vue réalisation technique c'est un projet
intéressant à conçevoir, surtout du coté logiciel.

Cet article ne va pas trop s'attarder sur le coté hardware
et va surtout vous expliquer comment on peut traiter et visualiser
un stream continu de données.

Grenouille
-----------

.. seealso::

   - http://www.elasticsearch.org/
   - https://pyelasticsearch.readthedocs.org/
   - https://fr.wikipedia.org/wiki/G%C3%A9olocalisation#G.C3.A9olocalisation_par_adresse_IP_.28sur_internet.29
   - http://www.maxmind.com/
   - https://github.com/tarekziade/grenouille
   - https://github.com/faitmain/faitmain.org/blob/master/volume-2/batterie.html

Ce n'est pas un nom très original mais je n'ai pas trouvé mieux. 
Le projet Grenouille utilise la sonde Yocto-Meteo pour remplir une 
base de données qui sert ensuite à afficher les informations dans 
des séries temporelles.

Limites & Evolutions
+++++++++++++++++++++

.. seealso::

   - https://raw.github.com/faitmain/faitmain.org/master/src/volume-2/station-meteo.rst
   
Le principal problème d'une station météo basé sur un Raspberry-PI et la
Yocto-Meteo est la consommation d'énergie. L'USB est un port très gourmand en
énergie et en branchant mon système complet sur une batterie lithium 3.7v en
6000 mAh et un panneau solaire censé charger la batterie la journée pour qu'elle
tienne le coup toute la nuit - je n'ai tenu que quelques heures...

Les puces Yoctopuce peuvent être coupées en deux afin de déporter les sondes
du port USB de quelques dizaines, voir centaines de mètre, mais ça n'enlève pas
la dépendance à une source d'énergie fixe.

Une évolution possible pour limiter la consommation serait de déporter la
base ElasticSearch sur un ordinateur dans la maison ou sur internet, et
de suspendre les ports USB pour ne les utiliser que toutes les 15 minutes
pour la récupération des valeurs.

Jonathan a écrit un article très intéressant à ce sujet dans ce numéro:
`Passer un projet sur batterie </volume-2/batterie.html>`_

Pour ma station météo, je reste quand même sur l'objectif de créér un
système autonome en énergie, qui puisse être interrogé sans fil -
donc la prochaine version de la station sera peut être réalisée avec
du matériel plus low-level. Donc peut être un Arduino, une puce radio
433mhz et une base déportée...

Dans tout les cas, pour une application indoor ou proche de la maison,
cette board est très simple à mettre en oeuvre et parfaite pour mettre
rapidement en place un projet sans avoir à jouer du fer à souder.


Yoctopuce
---------

.. seealso::

   - http://www.yoctopuce.com
   - https://pypi.python.org/pypi/yoctopuce
   
   
This is Yoctopuce Python API. All required source files are in the 
Yoctopuce folder. You will find some small examples for every available 
Yoctopuce product in examples folder. 

The complete documentation is in the Documentation folder. 
The HTML documentation is interactive, similar to JavaDoc

There is a small difference between this library and the the one you can 
download directly from Yoctopuce, with this one includes are done the 
following way::

    from yoctopuce.yocto_api import *

instead of::

    from yocto_api import *

This API uses precompiled C LIB files, sources are located C++ API, 
available from Yoctopuce's web site.

More information about Yoctopuce devices can be found on Yoctopuce's web 
site : http://www.yoctopuce.com

Any question, bug report or suggestion can be sent to Yoctopuce support.

   
   
      


