

===================
Créer une vignette
===================	

.. seealso:: 

   - http://c-net.fr/info/?doc=Diffuser_vos_vid%E9os_sur_le_Net_depuis_votre_PC_!_(3)


ffmpeg permet très simplement d’extraire une image d’une vidéo. 

La commande est la suivante::

    ffmpeg -i mavideo.mp4 -vcodec mjpeg -vframes 1 -an -f rawvideo -s 640×360 -ss 0 vignette.jpg


Précisons quelques paramètres : 
« -vcodec mjpeg » : la vignette sera codée en jpg 
« -ss 0″ : on récupère la première image (seconde 0) 
