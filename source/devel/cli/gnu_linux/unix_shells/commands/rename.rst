
.. index::
   cli (renaming files)
   cli (hg rename)


.. _renaming_files:

==============
Renaming files
==============

rename command
==============

.. seealso:: http://www.commandlinefu.com/commands/tagged/404/rename

Rename files from .c to .cpp
------------------------------

.. code-block:: bash

    rename 's/\.c/\.cpp/' *.c

Rename files from .MOD to .MPG
------------------------------

.. code-block:: bash

    rename 's/\.MOD/\.MPG/' *.MOD
    

With the find command + hg rename
=================================

Rename files from ".txt" to ".rst"
----------------------------------

.. code-block:: bash

    find . -name "*.txt" | awk '{ newFile=gensub("txt$", "rst", 1); system("hg rename " $0 " " newFile) }'




















