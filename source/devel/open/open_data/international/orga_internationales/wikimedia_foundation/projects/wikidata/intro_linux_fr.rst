
.. index::
   pair: Linuxfr; Wikidata


.. _wikidata_linuxfr_2012:

================================================
Annonce de Wikidata par Linuxfr (13 avril 2012)
================================================

.. seealso::

   - http://linuxfr.org/news/wikidata-wikipedia-comme-une-base-de-donnees
   - :ref:`wikidata_april_2013`

.. contents::
   :depth: 3

Open Data Wikidata : Wikipedia comme une base de données
========================================================


La mode est à l'Opendata. L'État français a ainsi ouvert son portail et 
c'est loin d'être le seul exemple. 

Des téraoctets de données sont ainsi disponibles sur le web. 

Il serait criminel de laisser ces données moisir quand on n'a jamais eu 
autant de puissance de calcul pour les exploiter.

Exploiter ces données peut cependant devenir assez casse-tête dès qu'on 
veut le faire automatiquement (ce qui est parfois indispensable vu le 
volume). 

En prenant un exemple de fichier sur data.gouv.fr, on peut voir que les 
données sont organisées sur le classeur de tableur, de manière pas forcément 
homogènes (les années sont classées dans les onglets, la description de 
l'étude est mélangée dans le même document). 

Elles sont presque plus organisées pour être lues par un humain que pour 
être exploitées.

Un de ces gigantesques dépôts de données plus ou moins organisés est
Wikipédia. Les données sont organisées sous forme de pages, de catégories, 
d'infobox, mais pas forcément exploitables facilement automatiquement. 
Des projets issus du monde du Web Sémantique le font cependant, comme 
par exemple dbpedia dont voici la page concernant la France, qui permettent 
d'organiser ces données sous forme plus facilement exploitable par la machine 
et les programmeurs.

Il n'a pas échappé à certains membres de la communauté wikipedia qu'on 
pouvait faire beaucoup mieux en n'extrayant plus seulement les données 
à partir de wikipedia mais en mettant une base de données au cœur de 
Wikipedia et Mediawiki ...

C'est ainsi qu'est né le projet Wikidata et ça promet d'être une étape 
importante pour l'encyclopédie, mais pas que

Description
===========

Problématique
--------------

Wikipedia, c'est 280 langages et plusieurs millions d'articles. 

Certaines informations sont dupliquées en plusieurs endroits de 
l'encyclopédie, sont redondantes entres les langues et nécessitent 
d'être périodiquement mises à jour, ce qui peut prendre beaucoup de 
temps aux contributeurs pour des tâches fastidieuses.

Wikidata vise entre autre à faciliter ces mises à jours en centralisant 
les informations dans une base de données, dans laquelle les articles 
vont piocher pour pouvoir les afficher et à faciliter l'automatisation 
de leur manipulation.

Un autre objectif de Wikidata est, à la manière d'autre projets de la 
fondation Wikimedia comme Commons, le dépôt de fichiers multimédias libre, 
de servir de dépôt de données ouvertes et librement réutilisables.

Ce dépôt ayant vocation à accueillir des données de natures arbitraires 
et diverses, les technologies du Web sémantique, structurées et ayant 
le potentiel d'accueillir des données de toutes natures, sont toutes 
indiquées.

Le projet
=========

D'après sa feuille de route, le projet comporte trois grandes étapes 
pour son développement et sa mise en œuvre:

Dans un premier temps 
---------------------

création de l'infrastructure pour une base de données d'entité. 

Une Entité, ce sera tout ce qui fait l'objet d'un article dans wikipedia, 
une personne, un pays, une notion mathématique ou un Pokémon par exemple, 
qui seront associées à un identifiant.

Rien que faire cela permet de gérer d'une manière nouvelle les liens 
interlangues : au lieu d'avoir à ajouter des liens vers les articles 
correspondant dans toutes les autres langues, il suffira de lier les 
articles avec leur entité pour retrouver les liens interwikis 
correspondants. 

Le travail est actuellement largement assuré par des bots communautaires 
et le projet compte fournir son aide à la communauté pour les adapter.

Sur le plan de l'organisation, la philosophie du projet Wikidata est la 
même que celle de la fondation Wikimedia : fournir l'infrastructure 
technique et laisser la communauté se charger de l'utilisation des données.

Une fois les bases en place, rentrer un peu plus dans le coeur du sujet 
et rajouter la gestion des infobox. 
Du point de vue du backend, il s'agit d'ajouter la possibilité de lier 
les entités identifiées en phase 1 à un ensemble de propriétés (arbitraires) 
associées à leur valeur - par exemple à l'entité "France", ajouter une 
propriété "densité de population" de valeur "116 hab/km²" - de manière 
similaire aux infobox actuelles. 

Les développeurs vont fournir une API permettant de manipuler les données, 
ainsi qu'une ou plusieurs interfaces utilisateurs.

Du côté des joyeusetés techniques de cette phase, on trouve entre autre 
la conversion automatique des unités (basée sur le système de type de 
Semantic MediaWiki) pour l'internationalisation, la création d'une 
syntaxe pour aller chercher une info dans la base de données quand on 
rédige une page sur Wikipedia, la possibilité d'indiquer les sources des 
différentes informations, la création d'articles stub pour les Entités 
ne disposant pas d'articles dans une langue mais pour lesquelles des 
informations sont présentes sur Wikidata à partir de modèles correspondants 
à la nature de l'entité.

Encore une fois, un des effets sera la facilitation de la maintenance 
de wikipedia pour avoir des informations le plus à jour possible et 
la synchronisation. 

Du point de vue du contributeur, ça implique principalement la 
modification des modèles qui génèrent les infobox. 

Du point de vue des données, est aussi laissé à la communauté le choix 
des priorités des données à afficher quand plusieurs sources non 
concordantes sont disponibles pour une information particulière. 

De ce que j'en comprends, les différentes données seront disponibles dans 
la base et la communauté devra définir les règles de choix automatiques 
(par exemple priorité aux données de l'ONU sur les données de l'Insee, 
ou l'inverse).

Je ne détaillerai pas la liste des perspectives ouvertes (les objectifs 
optionnels de wikidata) mais elles sont bien entendu assez larges, ils 
évoquent la création de jeux de fact checking pour vérifier la validité 
des données de manière ludique, ou encore la suggestion automatique 
de données à ajouter dans un article, ainsi que de sources.

La dernière phase consiste en un développement de la possibilité 
d'utiliser les données dans MediaWiki, la gestion de listes de données. 
C'est-à-dire la possibilité de faire des requêtes pour créer des listes 
de données, faire quelques statistiques basiques, on imagine par exemple une moyenne, ou des possibilités pour afficher ces listes ou générer des graphiques.

Les gens
=========

Le projet est porté par des universitaires allemands (Markus Krötzsch, 
de l'Université d'Oxford et Denny Vrandecic qui travaille maintenant pour 
Wikimedia) qui n'en sont pas à leur coup d'essai puisqu'ils sont déjà à 
l'origine de Semantic Mediawiki, l'extension ajoutant la gestion de la 
sémantique au célèbre moteur wiki et a semblé suffisamment intéressant 
pour être financé par la Gordon and Betty Moore Foundation, créé par 
l'auteur de la fameuse loi, Paul Allen, le cofondateur de Microsoft par 
l'intermédiaire de l'Allen Institute for Artificial Intelligence ou 
encore Google. 

Techcrunch fait d'ailleurs le lien avec de vagues rumeurs de virage 
sémantique de Google sur son moteur de recherche initiées par le 
Wall Street Journal.

L'avancement
============

Le projet est en développement actif. On peut naviguer à partir de la 
page consacrée au développement pour s'en convaincre. 

Il est notamment inscrit au programme du Berlin Hackaton 2012 qui aura 
lieu début juin. 
D'autres ressources sont aussi actuellement modifiées, comme la page 
dédiée au modèle de données qui contient pas mal d'informations 
intéressantes, à consulter pour les amateurs.

Le premier objectif temporel est fixé pour l'été prochain et concerne 
la première phase de gestion des identifiants. 

D'après la FAQ il devrait être terminé en Mars 2013, donc après un an 
de développement.

Impacts
=======

Le projet n'est pas en service ni même achevé pour l'instant, il 
n'échappe pas pour autant aux critiques par exemple sur la neutralité 
de point de vue qui soulève le problème de la non neutralité du choix 
de données. 

L'accueil de l'annonce est cependant globalement assez bon sur les sites 
à orientation technique et la nouvelle a été largement relayée 
(par exemple H-online, Numerama, CNet ou Scientific computing).

Parmi les effets de bords, Wikidata pourrait avoir des conséquences sur 
les politiques internes de la communauté Wikipedia sur les critères 
d'admissibilité dans l'encyclopédie, polémique majeure autour de 
Wikipedia entre les inclusionistes et les suppressionnistes.


Il va en effet devenir assez tentant de créer des entités qui ne sont 
pas décrites par un article dans Wikipedia, avec les importations de 
données de masse par exemple, ou pour y faire référence dans des 
articles, par exemple des personnes qui existent mais ne remplissent 
pas les critères pour avoir un article. 

Il sera intéressant de voir comment la communauté va s'adapter.

En conclusion
==============

Wikidata a plusieurs intérêts majeurs pour le projet d'encyclopédie, la 
facilitation de certaines tâches fastidieuses de Wikipedia, 
l'internationalisation des données facilitée (l'indépendance à la langue). 

C'est un projet utile et prometteur auquel le monde du logiciel libre 
ne peut qu'apporter son soutien et qui pourrait rendre bien des services 
à la communauté en servant de source de données pour des applications 
libres (ou même non-libres).
