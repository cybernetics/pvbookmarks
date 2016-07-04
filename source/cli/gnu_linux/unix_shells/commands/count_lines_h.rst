
.. index::
   pair: comptage ; lignes

===================================================
Comptage de lignes
===================================================

.. seealso:: :ref:`command_line_interface`

.. contents::
   :depth: 3



Compter le nombre de lignes '.h' dans un projet
====================================================

.. code-block:: bash

    find . -name "*.h" -print | xargs wc -l



Compter le nombre de lignes 'C/C++' dans un projet
====================================================

.. code-block:: bash

    find . -name '*.c' -o -name '*.cpp' -print | xargs wc -l


Compter le nombre de lignes python dans un projet
====================================================

.. code-block:: bash

    find . -name '*.py' -print | xargs wc -l
















