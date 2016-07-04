
.. index::
   pair: CLI ; delete svn files


.. _cli_delete_files:

=================
Delete svn files
=================

.. contents::
   :depth: 3


With the find command 
=================================

.. code-block:: bash

    find . -depth -name .svn -type d -exec rm -fr {} \;






















