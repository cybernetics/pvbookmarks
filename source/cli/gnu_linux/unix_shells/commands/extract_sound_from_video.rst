
.. index::
   cli (extract sound)


.. _extract_sound_from_a_video_with_ffmpeg:

======================================
Extract sound from a vidéo with ffmpeg
======================================

.. seealso:: 

   - :ref:`ffmpeg_video_library` 

Source: Linux Partique numéro 63, p.23

Vous venez de récupérer une vidéo depuis un site de publications du type Youtube
ou DailyMotion, dont vous aimeriez bien récupérer la bande son ?

C'est idéal dans le cas de clip vidéo d'un artiste que vous appréciez par exemple...

Dans ce cas, la commande suivante, utilisant :ref:`ffmpeg <ffmpeg_audio_library>`
vous sera très utile.



::

    ffmpeg -i input.flv -ar 44100 -ab 192k -ac 2 output.mp3
  

L'option ``-i`` 
    permet de définir le fichier vidéo en entrée.
    
L'option ``-ar``
    définit la fréquence d'échantillonnage (par défaut 44100Hz)
    
L'option ``-ac``
    permet de définir le nombre de canaux audio
    
L'option ``_ab``
    désigne le bitrate audio (64k par défaut)
    
    
    
    
    













