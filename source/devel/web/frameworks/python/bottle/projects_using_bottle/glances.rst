
.. index::
   pair: Bottle ; Glances


.. _bottle_glances:

==========================
``Bottle`` glances
==========================


.. seealso::

   - http://linuxfr.org/news/sortie-de-glances-version-2-0#linterface-web


.. contents::
   :depth: 3

L'interface Web (juin 2014)
============================

Avant de me faire jeter des pierres par des barbus énervés, sachez que cette 
nouvelle interface est un réel besoin remonté par les utilisateurs. 

Ils souhaitaient disposer d'une interface Web pour surveiller leurs machines 
depuis n'importe quel poste fixe ou mobile. J'ai donc supprimé le mode 
d'exportation au format HTML (basé sur Jinja) pour le remplacer par un service 
Web intégré (utilisant le framework Bottle).

Une fois Glances lancé avec l'option -w, on dispose ainsi d'une interface Web "responsive"::


    $ glances -w
    Bottle v0.12.5 server starting up (using WSGIRefServer())...
    Listening on http://0.0.0.0:61208/
    Hit Ctrl-C to quit.

