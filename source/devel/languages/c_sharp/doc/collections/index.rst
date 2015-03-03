

.. index::
   pair: c♯ ; collections
   pair: Interface ; collections


.. _csharp_collections:

================
c♯ collections
================

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.collections.icollection%28v=vs.100%29.aspx
   - http://www.dotnetperls.com/
   - :ref:`csharp_exceptions_bis`



.. contents::
   :depth: 3



.. _interface_csharp_collection:

Interface C♯ ICollection
========================

.. seealso:: http://msdn.microsoft.com/fr-fr/library/system.collections.icollection%28v=vs.100%29.aspx


L'interface ``ICollection`` étend IEnumerable ;



Une implémentation de IDictionary est une collection de paires clé/valeur,
comme la classe Hashtable.

Une implémentation de IList est une collection de valeurs dont les membres sont
accessibles par index, comme la classe ArrayList.

Les collections qui limitent l'accès à leurs éléments, comme les classes Queue
et Stack, implémentent directement l'interface ICollection.

Si ni l'interface IDictionary, ni l'interface IList ne répondent aux exigences
de la collection requise, dérivez la nouvelle classe de collection de
l'interface ICollection afin d'obtenir plus de flexibilité.


IDictionary et ``IList``
-------------------------

IDictionary et ``IList`` sont des interfaces plus spécialisées qui étendent
ICollection.





Implémentation de c♯ ICollection
================================

.. toctree::
   :maxdepth: 4

   array/index
   arraylist/index
   dictionaries/index
   indexer/index
   list/index
   tuple/index



