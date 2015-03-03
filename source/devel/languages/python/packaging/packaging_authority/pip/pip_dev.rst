

.. index::
   pair: pip; Edition


=================
pip development
=================

.. contents::
   :depth: 3
   

Installation en mode « édition » ?
===================================

.. seealso::

   - http://stephane-klein.info/blog/2013/06/19/mon-cookbook-:-pip,-virtualenv/



Voici deux méthodes pour installer un package python à partir du fichier setup.py::

    $ python setup.py install

ou::

    $ pip install .

Ces deux commandes installent le package dans le dossier site-packages 
de votre environnement python.


.. warning:: Si vous modifiez le code source de votre package, vos modifications ne 
   seront pas "visibles" lors de l'exécution du package dans votre environnement, 
   car une copie des fichiers sources a été faite lors de l'installation.

Par conséquent, à chaque modification, vous allez devoir installer de 
nouveau votre package.

.. note:: Ceci est très pénible si vous êtes en train de développer 
   votre application.


C'est là que l'installation en mode editable entre en jeu.

Lors de l'installation en mode édition, le code source n'est pas copié 
vers le dossier site-packages mais un lien symbolique est utilisé.

Vos modifications seront tout le temps pris en compte, sans passer par 
l'étape d'installation.

Voici deux commandes pour effectuer une installation en mode « édition »::

    $ python setup.py develop

ou::

    $ pip install -e .

Par le passé, python setup.py develop ne permettait pas la désinstalation 
du package. 
Maintenant ce n'est plus le cas, par conséquent ces deux commandes semblent 
être synonymes.


