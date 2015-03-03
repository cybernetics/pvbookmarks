

.. index::
   pair: C♯ collections; Array
   pair: Array; foreach

.. _csharp_array:

================
c♯ arrays
================

.. seealso::

   - :ref:`csharp_collections`
   - http://msdn.microsoft.com/fr-fr/library/9b9dty7d%28v=vs.80%29.aspx
   - http://www.dotnetperls.com/array
   - http://www.dotnetperls.com/buffer
   - :ref:`csharp_arraylist`
   - :ref:`array_blockcopy`


.. contents::
   :depth: 3

Introduction
============


Un tableau est une structure de données qui contient un certain nombre de
variables du même type. Les tableaux sont déclarés avec un type::

    type[] arrayName;


Interface IList
================

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.collections.ilist%28v=vs.100%29.aspx

La classe Array ne fait pas partie de l'espace de noms System.Collections.

Cependant, il s'agit toujours d'une collection, car elle repose sur l'interface
IList.

.. note:: IDictionary et ``IList`` sont des interfaces plus spécialisées qui
   étendent ``ICollection``.



Examples
========

.. toctree::
   :maxdepth: 4

   example_1
   example_2
   example_blockcopy
