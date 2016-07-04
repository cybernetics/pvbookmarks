

.. index::
   pair: sphinx ; index


.. _sphinx_index:

=======================
index (very important)
=======================


Sphinx automatically creates index entries from all object descriptions
(like functions, classes or attributes) like discussed in domains.

However, **there is also explicit markup available, to make the index more
comprehensive and enable index entries in documents where information is not
mainly contained in information units, such as the language reference**.

.. rst:directive:: .. index:: <entries>

   This directive contains one or more index entries.  Each entry consists of a
   type and a value, separated by a colon.

   For example::

      .. index::
         single: execution; context
         module: __main__
         module: sys
         triple: module; search; path

      The execution context
      ---------------------

      ...

   This directive contains five entries, which will be converted to entries in
   the generated index which link to the exact location of the index statement
   (or, in case of offline media, the corresponding page number).

   Since index directives generate cross-reference targets at their location in
   the source, it makes sense to put them *before* the thing they refer to --
   e.g. a heading, as in the example above.










