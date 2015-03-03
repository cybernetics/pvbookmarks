

.. _git_intro:

===================
Introduction à git
===================


.. figure:: logo_git_core.png
   :align: center

   Git core


Particularités techniques
=========================

Comme BitKeeper, Git ne repose pas sur un serveur centralisé. 

C'est un outil bas niveau, qui se veut simple et très performant, dont la 
principale tâche est de gérer l'évolution du contenu d'une arborescence.

Git indexe les fichiers d'après leur somme de contrôle calculée avec la 
fonction SHA-1. 

Quand un fichier n'est pas modifié, la somme de contrôle ne change pas et le 
fichier n'est stocké qu'une seule fois. 
En revanche, si le fichier est modifié, les deux versions sont stockées sur le disque.

Git n'était pas, au départ, à proprement parler un logiciel de gestion de versions. 
Linus Torvalds expliquait que, « par bien des aspects, vous pouvez considérer Git 
comme un système de fichiers : il permet un adressage associatif, et possède 
la notion de versionnage, mais surtout, a été conçu en résolvant le problème du 
point de vue d'un spécialiste des systèmes de fichiers. 

Il n'y avait donc aucun intérêt à créer un système de gestion de version 
traditionnel. ». 

Il a aujourd'hui évolué pour intégrer toutes les fonctionnalités d'un gestionnaire 
de versions.

Git est considéré comme performant, au point que certains autres logiciels de 
gestion de version (Darcs, Arch), qui n'utilisent pas de base de données, se 
sont montrés intéressés par le système de stockage des fichiers de Git pour 
leur propre fonctionnement.


Source code
===========

Github
-------

.. seealso::

   - https://github.com/git/git
   - https://github.com/git/git/blob/master/Documentation/SubmittingPatches
   
Git Source Code Mirror - This is a publish-only repository and all pull requests 
are ignored. 

Please follow Documentation/SubmittingPatches procedure for any of your 
improvements.
 
 
Google codee
------------

.. seealso::

   - http://code.google.com/p/git-core/
   
      







