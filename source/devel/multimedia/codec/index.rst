


.. index::
   ! Codec


.. _codec:

============================================
Codec (COde-DECode)
============================================

.. seealso::

   - http://fr.wikipedia.org/wiki/Audio_Video_Interleave
   - http://www.the-labs.com/Video/odmlff2-avidef.pdf

.. contents::
   :depth: 3


Introduction
============


Un codec est un procédé capable de compresser et/ou de décompresser un signal
numérique.

Ce procédé peut être un circuit imprimé ou un logiciel.

Le mot-valise « codec » vient de «compression-décompression»
(ou « codage-décodage » - COde-DECode en anglais).

D'un côté, les codecs encodent des flux ou des signaux pour la transmission,
le stockage ou le chiffrement de données. D'un autre côté, ils décodent ces
flux ou signaux pour édition ou restitution.

Les différents algorithmes de compression et de décompression peuvent
correspondre à différents besoins en qualité de restitution, de temps de
compression ou de décompression, de limitation en termes de ressource processeur
ou mémoire, de débit du flux après compression ou de taille du fichier résultant.

Ils sont utilisés pour des applications comme la téléphonie, les visioconférences,
la diffusion de médias sur Internet, le stockage sur CD, DVD, la télé numérique
par exemple.



Codecs, normes et conteneurs
=============================

Les notions de codec, norme et conteneur sont souvent confondues par les
néophytes, ou par abus de langage.

- La norme décrit le format des données.
- Le codec est le logiciel ou le matériel qui met en œuvre un procédé capable
  de compresser ou décompresser les données de format normalisé.

Par exemple, MPEG-4 AVC/H.264 est une norme vidéo, et x264 est un codec capable
de produire un flux vidéo respectant cette norme. Il existe d'autres codecs
pour cette norme.

Lorsqu'il n'existe qu'une seule implémentation, les termes codec et norme sont
confondus (exemple : VC-1).

Un format conteneur contient des flux audio et vidéo respectant une quelconque
norme. Ce format permet d'entrelacer les données audio et vidéo, et contient
les informations permettant de les synchroniser au moment de la restitution.

Un conteneur peut contenir plusieurs flux audio et vidéo, mais aussi des
sous-titres, du chapitrage et des menus.

Le choix d'un conteneur peut par contre limiter les normes utilisables à
l'intérieur de celui-ci.

Ainsi un conteneur MPEG-2 ne peut contenir que des flux vidéo MPEGV2 et des
flux audio MPEGA 1, 2 ou 3 ou des flux audio AAC.


Interface OpenMAX
==================

.. toctree::
   :maxdepth: 3

   openmax




