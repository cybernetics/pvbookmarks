


=======================
Installation GNU/linux
=======================

.. seealso:: http://www.arakhne.org/linux/frenchtut/installubuntu/index.html


.. contents::
   :depth: 3


Introduction
=============


Et maintenant, tu indiques que tu n'as qu'une partition qui occupe tout le
disque ?

Pour Linux, ton disque c: s'appelle sda1 (1ère partition du 1er disque)

Tu dois donc le réduire avec Gparted pour y mettre les partitions que Ubuntu
a besoin !


Pour installer Ubuntu, tu as besoin au minimum d'une partition ext3 pour le
système -> 8 Go mini, mais prévoir les programmes à installer et une pour le
swap -> mini 256 Mo, mais il vaut mieux indiquer entre 512Mo à 1Go.

Ensuite rien ne t'empêche de créer plusieurs partitions de données.

Un exemple de 4 partitions principales pour ton disque dur de 160 Go :

- Ubuntu : Partition dev/sda1 -> ext 3 - Point de montage / - 10 Go
- Swap : dev/sda2 -> linux-swap - 1 Go
- Données : Partition dev/sda3 -> ext 3 - Point de montage /Home - 100 Go

Si tu veux pouvoir avoir accès à des données sous Linux et Windows tu peux
créer une partition en Fat32:

- Partition dev/sda4 -> Fat32 - Point de montage media/documents

Exemple2
========

::

    Bonjour,
    Je m'apprête à créer une machine avec un dual boot : Windows 7 et Linux
    (Ubuntu probablement). Linux me servira à faire de bureautique, de la musique,
    un peu de vidéo. Windows 7 sera pour les jeux :sarcastic:

    J'envisage de partitionner mon disque en 4 :
    1) Partition Linux système et programmes Linux.
    2) Système Windows 7 et programmes Windows.
    3) Mes documents (à voir pour utiliser cette partition à la fois par Linux et 7).
    4) Swap Linux, 4go.

    Sachant que le DD fait 640 Go, quelle proportions entre les 3 partitions ?? Voilà mon idée :
    1) Linux : 100Go.
    2) Windows 7 : 200Go
    3) Mes documents : 337Go.
    4) Swap 4go.

    Config hardware :
    Asus PQ5-E
    Go DDR2
    Intel E8400
    HD 4870 Sapphire Vapor-x 1Go
    WD Black caviar 640Go.


Estimes-tu vraiment avoir besoin d'une partition de swap ? Les tutos que tu
trouveras et qui justifient d'usage d'une partition de swap égale au double
de la mémoire datent un peu. Un système Linux fonctionne d'autant mieux qu'il
dispose de mémoire, et le rapport efficience/mémoire est linéaire.
Alors au tant en profiter. Mais ajouter du swap a un système déjà largement
doté de mémoire vive est inutile. Sauf pour certains modes de veille.
Là, ça se justifie, donc.

Concernant la partition partagée, et Windows ne connaissant que son nombril,
ce sera à Linux de faire l'effort de lire et d'écrire dans le format de l'autre.

Mais si permettre à Linux d'accéder aux fichiers de Windows n'est pas idiot,
je ne pense pas que faire d'une partition NTFS et d'une arborescence Windows
le point de montage de /HOME soit une excellente idée.

Autre chose. 100 Go pour les programmes Linux ! Mais qu'est ce que tu vas
installer ? Réserve plutôt 10 Go pour ton système libre, et 90 Go pour /HOME.

Après, pour Windows, c'est à toi de voir.

