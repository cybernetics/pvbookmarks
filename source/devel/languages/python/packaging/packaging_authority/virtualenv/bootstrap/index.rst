

.. index::
   pair: Python; Bootstrap


.. _virtualenv_bootstrap:

====================
Virtual bootstrap
====================

.. seealso::

   - :ref:`bootstrap`
   - http://stephane-klein.info/blog/2013/06/19/mon-cookbook-:-pip,-virtualenv/
   - http://www.virtualenv.org/en/latest/#bootstrap-example



.. contents::
   :depth: 3


Warning (obsolete)
===================

.. seealso::

   - :ref:`bootstrap`


Introduction
=============

.. seealso::

   - http://stephane-klein.info/blog/2013/06/19/mon-cookbook-:-pip,-virtualenv/

Depuis quelques mois, j'utilise la fonctionnalité « Creating Your Own 
Bootstrap Scripts » de virtualenv.

Cette fonctionnalité permet de générer un fichier python, qui installera 
automatiquement un environnement virtuel comme la commande virtualenv 
mais sans aucune dépendance à installer. 

pip sera bien présent dans bin même si vous ne l'avez pas installé avant.

Utilisation de bootstrap.py
============================

Avant de voir comment générer un fichier bootstrap.py, nous allons voir 
comment l'utiliser::

    $ mkdir ~/my_project/
 	$ cd ~/my_project/
 	$ git clone http://stephane@repos.stephane-klein.info/example1.1 .
 	$ python bootstrap.py
 	$ bin/pip install -r devel-requirements.txt

Voila, rien de plus… on va voir par la suite qu'il est même possible 
d'installer automatiquement les devel-requirements.txt.


Génération d'un bootstrap.py
=============================

La documentation de virtualenv, donne une exemple de génération d'un 
fichier bootstrap.py.

Personnellement, je place un fichier nommé create-bootstrap.py dans le 
dossier où je souhaite créer mon fichier bootstrap.py. 

Ce fichier :file:`create-bootstrap.py` contient le code suivant::

    import virtualenv, textwrap
         
    output = virtualenv.create_bootstrap_script(textwrap.dedent("""
    import os, subprocess
     
    def adjust_options(options, args):
        if len(args) == 0:
            args.append('.')
     
    def after_install(options, home_dir):
        subprocess.call([
            os.path.join('bin', 'pip'),
            'install', '-r', 'devel-requirements.txt'
        ])
    """))
    f = open('bootstrap.py', 'w').write(output)

La ligne args.append('.') indique qu'au lancement de bootstrap.py 
l'environnement python sera installé dans le dossier courant.

Un peu plus bas, je lance l'installation de devel-requirements.txt.

J'ai juste à lancer (une fois) python create-bootstrap.py pour générer 
bootstrap.py::

	$ ls -1
	create-bootstrap.py
	setup.py
	devel-requirements.txt
	requirements.txt
	$ python create-bootstrap.py
	$ ls -1
	bootstrap.py
	create-bootstrap.py
	devel-requirements.txt
	requirements.txt
	setup.py

Maintenant, j'ajoute create-bootstrap.py et bootstrap.py dans mon dépôt.


    $ git add create-bootstrap.py bootstrap.py

Par la suite, il n'y a plus besoin d'utiliser create-bootstrap.py à moins 
de vouloir modifier bootstrap.py pour ajouter/supprimer des actions automatiques.


Pour finir, mon workflow complet
=================================

Prérequis:

- python

Simple comme niveau prérequis, non ? Un peu comme buildout pour ceux qui 
connaissent.

Je prépare un dossier avec mon projet::

	$ mkdir ~/my_project/
	$ cd ~/my_project/
	$ git clone http://my-project.org/ .

En une seule commande, j'installe mon environnement python et mon projet 
en mode développement (éditable).

	$ python bootstrap.py


