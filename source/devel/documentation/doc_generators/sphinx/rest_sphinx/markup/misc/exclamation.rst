

.. index::
   pair: sphinx ; exclamation
   ! exclamation


.. _sphinx_exclamation:


==============================
! exclamation (important)
==============================

You can mark up "main" index entries by prefixing them with an exclamation
mark.  The references to "main" entries are emphasized in the generated
index.  For example, if two pages contain ::

      .. index:: Python

   and one page contains ::

      .. index:: ! Python

   then the backlink to the latter page is emphasized among the three backlinks.

   For index directives containing only "single" entries, there is a shorthand
   notation::

      .. index:: BNF, grammar, syntax, notation

   This creates four index entries.

   .. versionchanged:: 1.1
      Added ``see`` and ``seealso`` types, as well as marking main entries.



