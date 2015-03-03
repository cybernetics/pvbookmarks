
==========================================
Transformer un fichier MOV en fichier ogg
==========================================

.. seealso::

   - http://korben.info//ffmpeg-pour-les-nuls.html


.. contents::
   :depth: 3

Introduction
=============

Le temps nécessaire à l'encodage

Les preset gérant le temps nécessaire à l'encodage :

- ultrafast : le plus rapide, mais donne la moins bonne qualité d'image.
- superfast
- veryfast
- faster
- fast
- medium
- slow
- slower
- veryslow : La meilleure qualité au prix de la vitesse
- placebo : le plus lent, mais pas la meilleure qualité (optimisé pour les benchmarks)

Les preset gérant le temps nécessaire à un encodage sans aucune perte de
qualité d'image :

- lossless_max
- lossless_ultrafast
- lossless_fast
- lossless_medium
- lossless_slow
- lossless_slower

Par exemple, la ligne suivante permet de spécifier que le fichier de sortie
doit pouvoir être lu sur à peu près n'importe quel appareil (cela donnera une
moins bonne qualité d'image ou un fichier de sortie plus gros) et un encodage
très lent (pour essayer de maximiser la qualité d'image) :

bitrate  -b
============

- 380k
- 522k

::

    ffmpeg -i MOV0A0.MOD -vcodec libx264 -vpre ultrafast  video_test.ogg
    ffmpeg -i MOV0A0.MOD -s 720x480 -b 522k  v4.ogg
    ffmpeg -i MOV0A0.MOD -s 720x480 -b 522k -aspect 16:9 v5.ogg


Supprime le son
===============

La taille passe de 1.1 Mo à 380ko également.

::

    ffmpeg -i MOV0A0.MOD -s 720x480 -b 522k -an  v7.ogg

::

    ffmpeg -i MOV0A0.MOD -s 720x480 -b 522k -ab 56k  v8.ogg


Codage du son avec vorbis
=========================

::

    date; ffmpeg -i MOV0A0.MOD -s 720x480 -b 522k -strict experimental -acodec vorbis -aq 20 v10.ogg; date


Script pour traiter un répertoire
=================================

::

    #!/bin/bash

    for f in *.MOD ; do
        ffmpeg -i ${f} -s 720x480 -b 522k -strict experimental -acodec vorbis -aq 20 ${f%%.*}.ogg;
    done

Liste des fichiers d'un répertoire
==================================

::

    #!/bin/bash

    for f in *.MOD ; do
        echo ${f%%.*};
    done

