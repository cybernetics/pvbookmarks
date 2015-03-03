

.. index::
   pair: cli ; find strings in files


=================================
find strings in files recursively
=================================

.. code-block:: bash

    find . -name "*.rst" -exec grep -iHA5 -B5 "string" {} \;
    find . -name "*.rst" -exec grep -iH "string" {} \;
    find . -name "*.rst" -exec grep "string" {} \;



















