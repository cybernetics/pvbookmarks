
.. index::
   pair: Replace strings ; rpl
   ! rpl


.. _replace_strings_rpl:

============================================
recursive replace string in files with rpl
============================================


.. seealso::

   - http://www.commandlinefu.com/commands/matching/replace-string-in-files-recursively/cmVwbGFjZSBzdHJpbmcgaW4gZmlsZXMgcmVjdXJzaXZlbHk=/sort-by-votes


.. contents::
   :depth: 3

Dry run ('s' option)
====================


.. code-block:: bash

    rpl -Rs -x'.rst' '2010-2012' '2010-2013' .
    rpl -Rs olstring  newstring  .



Replace (without 's' option)
=============================

.. code-block:: bash

    rpl -R -x'.rst' '2010-2012' '2010-2013' .
    rpl -R olstring  newstring  .













