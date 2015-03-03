


.. index::
   pair: Images ; FFmpeg
   pair: GIF ; Animé

.. _ffmpeg_image_magick:

=====================
FFmpeg + Imagemagick
=====================



.. contents::
   :depth: 3
   

Créer un Gif animé à partir d’une vidéo en ligne de commandes
============================================================= 

.. seealso::

   - http://lehollandaisvolant.net/index.php?d=2013/12/26/19/33/51-creer-un-gif-anime-a-partir-dune-video-en-ligne-de-commandes

Une astuce pour la nouvelle année — la sixième bientôt entamée pour ce site \o/.
Vous avez une vidéo et vous voulez faire un gif animé d’une scène, sous GNU/Linux ?

Il faut avoir installé avconv (le nouveau nom de ffmpeg) et des outils de 
manipulation d’images Imagemagick, puis il suffit de lancer ces commandes.

Prenez la séquence vidéo que vous voulez, avec après -ss le temps de début et 
après -t la durée de la séquence::

    avconv -i "video.avi" -f avi -vcodec copy -acodec copy -ss 00:13:00 -t 00:00:5 "temp.avi"


On fait un dossier temporaire::

    mkdir frames


On extrait les images de la vidéo, on mettant la largeur à 480 pixels et à 
raison de 10 images pour une seconde de film::


    avconv -i temp.avi -vf scale=480:-1 -r 10 frames/ffout%03d.png


On convertit ces images en un seul gif animé::


    convert -delay 5 -loop 0 frames/ffout*.png output.gif


Supprime les fichiers temporaires::


    rm temp.avi
    rmdir -r frames



Astuce : il est préférable de choisir une fenêtre de temps plus large pour la 
scène lors de la première commande, par exemple avec 10 secondes avant et 10 
secondes après. 

Juste après la troisième commande, vous pouvez aller dans le dossier frames et 
voir grâce aux vignettes les images précises qu’il vous faut.

Notez que cette commande (plus complexe) donne des gif animés de bonne qualité, 
contrairement à certaines autres commandes du genre. 


