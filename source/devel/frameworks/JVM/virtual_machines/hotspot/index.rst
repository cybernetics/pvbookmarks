

.. index::
   pair: JVM; Hotspot


.. _hotspot:

=============================
Hotspot Java Virtual Machine
=============================

.. seealso:: http://fr.wikipedia.org/wiki/Machine_virtuelle_Java#HotSpot.2C_la_machine_virtuelle_d.27Oracle


C'est la machine la plus utilisée. Elle a été créée et réalisée par Sun, elle est
aujourd'hui propriété d'Oracle, depuis que ce dernier a racheté Sun.

Elle est gratuite, propriétaire jusqu'à la version 6 (stable) et libre à partir
de la version 7 (non encore officielle).

Le 11 novembre 2006, Sun Microsystems a publié les sources de sa machine virtuelle
HotSpot et de son compilateur javac sous licence GNU GPL.

La première version ne se comportait que comme un interpréteur.

Cette approche était pénalisante, car l'interprète passe plus de temps à
interpréter qu'à exécuter.

Puis est apparue la compilation à la volée, qui traduit le bytecode en langage
machine, et exécute ce langage machine.

Ensuite la machine virtuelle est devenue capable de détecter les portions les
plus fréquemment utilisées pour concentrer les optimisations sur elles.
Elle a été dotée d'un profileur, et d'optimisations standards comme la mise à
plat des boucles. Toutes ces opérations peuvent être faites en plusieurs passes,
soit pour les améliorer progressivement, soit pour les annuler si elles se
révèlent obsolètes.


