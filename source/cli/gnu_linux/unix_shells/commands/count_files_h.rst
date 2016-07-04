
.. index::
   pair: cli ; files
   pair: comptage ; fichiers


==================================
Comptage de fichiers
==================================

.. seealso:: :ref:`command_line_interface`

.. contents::
   :depth: 3


Compter le nombre de fichiers include dans un projet
====================================================

.. code-block:: bash

    find . -name "*.h"  | wc -l



Compter le nombre de fichiers C/C++ dans un projet
====================================================

.. code-block:: bash

    find . -name '*.c' -o -name '*.cpp' | wc -l



















