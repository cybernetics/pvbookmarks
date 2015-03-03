

.. _replace_strings_find_grep_sed:

============================================
recursive replacing with find grep and sed
============================================


.. code-block:: bash

    find . -name "*.rst" -print0 | xargs -0 sed -i 's/1.1.1/1.2.0/g'













