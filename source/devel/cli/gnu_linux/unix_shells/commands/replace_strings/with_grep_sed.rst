

.. _replace_strings_with_grep_sed:

=========================================
no recursive replacing with grep and sed
=========================================


.. code-block:: bash

    grep -rl oldstring . | xargs sed -i -e 's/olstring/newstring/'
















