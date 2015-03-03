


.. index::
   ! Openmax


.. _openmax:

============================================
Openmax
============================================

.. seealso::

   - http://www.khronos.org/openmax/
   - http://fr.wikipedia.org/wiki/OpenMAX

.. contents::
   :depth: 3


Introduction
============

OpenMAX est une Interface de programmation ouverte et libre de droit qui fournit 
un accès aux codecs multimédias.

L'interface est spécifiée et normée par le Khronos Group. Elle fait partie de 
la plateforme OpenKODE.

Elle est divisée en plusieurs couches :

- OpenMAX AL (Application Layer, c'est-à-dire, couche d'application) est une 
  interface permettant aux application de s'abstraire de la gestion des 
  middlewares multimédia qui exécuteront les tâches dévolues (lecture, 
  enregistrement, etc...).
- OpenMAX IL (Integration Layer, c'est-à-dire, couche d'intégration) est une 
  interface permettant aux applications ou frameworks de communiquer avec les 
  différents codecs (logiciels ou matériels) audio, video, et d'imagerie de 
  façon transparente et standard.
- OpenMAX DL (Development Layer, c'est-à-dire, couche de développement) est 
  une interface contenant un ensemble de fonctions d'encodage et décodage 
  pouvant être implémentées et optimisées par les concepteurs des processeurs 
  matériels.


GST OpenMAX
===========

.. seealso:: 

   - http://www.freedesktop.org/wiki/GstOpenMAX
   - http://cgit.freedesktop.org/gstreamer/gst-openmax/
  
gst-openmax is a GStreamer plug-in that allows communication with OpenMAX IL 
components.

OpenMAX IL is an industry standard that provides an abstraction layer for 
computer graphics, video, and sound routines.

This project is a collaboration between Nokia, NXP, Collabora, 
STMicroelectronics, Texas Instruments, and the open source community.
  
   

  


