
.. index::
   pair: Site Web; Fait main

.. _fait_main_site_web:

================================================
Site web Fait main 
================================================

.. seealso:: 

   - https://github.com/faitmain/faitmain.org/blob/master/src/apropos.rst


Le site web est un site statique généré avec le moteur `kompost <https://github.com/faitmain/kompost>`_,
un script `Python <http://www.python.org/>`_ créé pour l'occasion, et des
templates `Mako <http://www.makotemplates.org/>`__.

Le contenu est au format `reStructuredText <https://fr.wikipedia.org/wiki/ReStructuredText>`_.
Ce format permet de générer les pages html mais aussi le PDF (spartiate), et dans le futur
un ePub, voir un magazine papier au format un peu plus léché.

Le site utilise `Bootstrap <http://twitter.github.com/bootstrap/>`_ pour un rendu correct
sur tous les périphériques. Les icônes sont de chez `Glyphicons <http://glyphicons.com>`_.

Le design est un derivé du thème *Amelia* du projet Bootswatch de
`Thomas Park <http://thomaspark.me>`_. Les polices de caractères viennent
de `Google Fonts <http://www.google.com/webfonts>`_

Chaque lien sortant est transformé en short link avec https://github.com/faitmain/short.faitmain.org.
Cette redirection permet de corriger d'éventuels liens cassés de manière
centralisée.

.. warning::

   Fait Main ajoute à tous les liens vers Amazon.fr un tag de référencement, qui rapporte
   au magazine un petit pourcentage des ventes réalisées si vous achetez sur cette boutique
   quelque chose. A terme, l'idée serait de voir si ce référencement permet de couvrir les
   frais d'hébergement du site.

   Conscients que c'est une option *opt-out* - nous envisageons aussi un modèle de dons,
   et les liens sont pour l'instant expérimentaux.


Le moteur de recherche est un `web service <https://github.com/faitmain/search.faitmain.org>`_
écrit avec `Cornice <http://cornice.readthedocs.org>`_,
basé sur `Xapian <http://xapian.org/>`_, appelé en Javascript depuis l'écran
de recherche. La base Xapian est mise à jour à chaque modification de contenu.


Le PDF
::::::

Le PDF est généré grâce à `rst2pdf <http://rst2pdf.ralsina.com.ar>`_, qui lui 
même utilise `ReportLab <http://www.reportlab.com/software/opensource/rl-toolkit/>`_.

La mise en page est spartiate mais suffisante pour une lecture sur écran.

Informations légales
::::::::::::::::::::

Magazine publié en France. Numéro ISSN en cours d'obtention.

Contact & addresse:

    Tarek Ziadé - tarek@faitmain.org
    6 rue de l'Eglise
    21540 Turcey
    France


- **Editeur** - Tarek Ziadé
- **Directeur de la publication** - Tarek Ziadé


Donnée personnelles stockées: chaque accès au site est stocké dans un 
fichier de log à des fins de statistiques - mais **les addresses IP ne 
sont pas collectées** et le serveur ne contact aucun service tiers.


