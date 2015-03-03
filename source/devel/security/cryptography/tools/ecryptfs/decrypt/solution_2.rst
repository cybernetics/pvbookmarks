
.. index::
   pair: Decrypt; File System
   pair: Crypt; File System

.. _decrypt_ecryptfs:

===============================================
Décrypter un  répertoire home à partir d'Ubuntu
===============================================


.. seealso::

   - http://ecryptfs.org/


.. contents::
   :depth: 3


Introduction
============

Ubuntu permet de crypter le répertoire home des utilisateurs, ce qui est
un gain considérable pour la sécurité même si cela ne règle pas tous les
problèmes.

Néanmoins, il peut arriver que dans certains cas on ait besoin de
décrypter ce volume en dehors de l'installation initiale.

C'est le cas notamment de la restauration d'un système, ou le clonage 
sur différents postes.


Tutoriel
========

.. seealso::

   - http://blog.evolya.fr/index.php?post/2012/Recuperer-les-donnee-encryptees-dans-le-repertoire-home-sous-Ubuntu
   

Voici donc un petit tutoriel pour expliquer comment décrypter un 
répertoire home à partir d'Ubuntu. 


En anglais ce serait *recovering encrypted home directory under Ubuntu*.

Lancer ubuntu
--------------

Pour commencer, lancer Ubuntu (avec un Live CD par exemple) et monter la
partition où se trouve le répertoire home.


Ouvrez une terminal (Alt+F2, et entrer "gnome-terminal") puis placez
vous dans le répertoire home en question.

Par exemple, ça pourrait ressembler à quelque chose comme::


    cd /media/5a0141f7-8841-c89f7-1b69-604896b27e75/home/


Aller au répertoire crypté
--------------------------

Ensuite, naviguer jusqu'au répertoire crypté correspondant à l'utilisateur.
Ce n'est pas forcément le nom entier de l'utilisateur, mais son login::

    cd .ecryptfs/username

Note: c'est ecryptfs, et pas encryptfs.


Récupérer la mount passphrase
------------------------------

L'étape suivante consiste à récupérer la "mount passphrase", qui n'est
pas pareil que celui utilisé pour se connecter.

Pour cela, entrez la commande suivante::

    ecryptfs-unwrap-passphrase .ecryptfs/wrapped-passphrase

La commande demande ensuite le mot de passe de l'utilisateur, c'est à
dire celui qui est utilisé pour ouvrir la session.

Récupérer le mount password
---------------------------

Quand c'est fait, la commande renvoie le "mount password" qu'il vous
faudra noter quelque part pour l'avoir par la suite.

Maintenant, créer un répertoire qui pointera vers les données décryptées::

    sudo mkdir /media/decrypted

Exécutez ensuite la commande suivante et entrez la "mount passphrase"
que vous avez obtenu un peu plus haut::

    sudo ecryptfs-add-passphrase --fnek

Cette commande devrait afficher deux lignes comme celles-ci::

    Inserted auth tok with sig [24dff660d7a4895f] into the user session keyring
    Inserted auth tok with sig [97364430f5234b94] into the user session keyring

Notez la seconde clé (ici 97364430f5234b94) qui corresponds au "auth token".

Maintenant vous pouvez monter le répertoire crypté grâce à la commande
suivante::

    sudo mount -t ecryptfs
    /media/5a0141f7-8841-c89f7-1b69-604896b27e75/home/.ecryptfs/username/.Private
    /media/decrypted
    Passphrase:  # Entrez la "mount passphrase"
    Selection: aes
    Selection: 16
    Enable plaintext passthrough: n
    Enable filename encryption: y
    Filename Encryption Key (FNEK) Signature: # entrez le "auth token"

Vous allez probablement obtenir un warning car la clé n'avais jamais été
utilisée avant (vous pouvez répondre "yes") et pour vous demander si
vous voulez conserver celle clé en cache (vous pouvez répondre "no",
sauf si vous comptez remonter la partition cryptée une autre fois).

Accès au répertoire décrypté
-----------------------------

Et voilà. Si tout se passe bien, vous pouvez accéder au répertoire décrypté
à partir de /media/decrypted/.

Le problème le plus fréquent concerne le fichier /home/username/.Private
qui est en fait un lien symbolique, et qui peut pointer vers le mauvais
répertoire si vous avez d'autres utilisateurs sur la partition.

Dans ce cas, il faut utiliser le lien directe comme /home/.ecryptfs/username.


