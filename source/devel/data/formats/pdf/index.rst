

.. index::
   pair: data ; PDF
   ! PDF


.. _pdf_format:

==================
PDF Format
==================

.. seealso::

   - http://pdfreaders.org/
   - :ref:`pdf_format_ref`


.. contents::
   :depth: 3

Introduction
============


.. seealso::

   - http://linuxfr.org/news/libre-choix-du-lecteur-pdf
   - http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=29061

Le format PDF ou Portable Document Format a été créé par Adobe en 1993 et
normalisé par l'ISO en 2008 sous la référence ISO 32000-1:2008.

Trois sous-ensembles du format PDF ont également été normalisés par l’ISO :

- `PDF/A-1`_ (PDF for Archive, référencé par la norme ISO 19005-1:2005)
- `PDF/X`_ (PDF for eXchange par ISO 15930-1 à -8)
- `PDF/E-1`_ (PDF for Engineering par ISO 24517-1:2008).

La gratuité du lecteur Acrobat Reader a grandement facilité la diffusion de ce
format et Adobe a pu vendre ses logiciels de création de PDF en situation de
monopole et conserver la stabilité du format jusqu'à la normalisation du format.

Ainsi, beaucoup de gens pensent qu'il n'y a qu'un lecteur, plus grave, certains
indiquent comment le télécharger sur le site d'Adobe et pire encore d'autres
l'imposent, ce qui est contraire à la notion de format ouvert qui promeut
l'interopérabilité et non la simple compatibilité.

Ce qui est anormal, c'est qu'une administration fasse de la publicité
(gratuite de surcroît) pour une entreprise et laisse croire qu'il n'existe
aucune autre solution que Adobe pour lire (et créer) des documents au format PDF.

C'est pourquoi la FSFE a ouvert le site pdfreaders.org et lancé une pétition
pour que les administrations mettent un pointeur sur le site PDFreaders qui
propose des lecteurs pour tous les systèmes d'exploitation.

Le Référentiel Général d'Interopérabilité v1.0 en vigueur pour les administrations
françaises (d'ailleurs diffusé en PDF) précise « Il est RECOMMANDÉ d'utiliser le
format PDF 1.7 (…) pour les échanges de dessins techniques (par exemple des plans)
en mode non révisable (…) pour les échanges de documents bureautiques en mode
non révisable. (…) pour la conservation des documents bureautiques dynamiques. »,
« (…) le format PDF/A, pour l’archivage des documents bureautiques statiques
non révisables. », « (…) d'utiliser le format PDF/X pour l’échange de données
numériques d'impression. »

On peut aussi dire que les centaines de pages des spécifications PDF et les
possibilités laissées en terme d'exécution de binaires externes, de codes
Javascript ou Flash, etc. ont laissé une longue histoire de problèmes de
sécurité sur les différents lecteurs, notamment celui d'Adobe.

Cf. la présentation au congrès CCC 28C3 en 2010, intitulée `OMG WTF PDF`_
(audio/vidéo mp4/mp3/ogg, pdf).

Sans oublier que le PDF prévoit dans ses spécifications la gestion des menottes numériques (DRM), permettant la restriction de l'impression, l'édition, l'annotation, etc.


.. _`PDF/A-1`: http://www.iso.org/iso/catalogue_detail?csnumber=38920
.. _`PDF/X`: http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=29061
.. _`PDF/E-1`:  http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=42274
.. _`OMG WTF PDF`: http://events.ccc.de/congress/2010/Fahrplan/events/4221.en.html

Pdf readers
===========

.. seealso::

   - http://pdfreaders.org/

Le Format de Document Portable (Portable Document Format - PDF) est un format
populaire pour publier textes et documents formatés.

Il en existe de nombreuses versions, certaines peuvent être qualifiées de
Standards Ouverts, d'autres sont normalisées par l'ISO et d'autres enfin sont
grevées par des brevets logiciels.

Vous devriez privilégier et promouvoir les versions basées sur des Standards
Ouverts parce que seuls les Standards Ouverts garantissent l'interopérabilité,
la concurrence et la liberté de choix

.. figure:: pdfreaders-logo.png
   :align: center



Tools
=====

.. toctree::
   :maxdepth: 3

   tools/index




