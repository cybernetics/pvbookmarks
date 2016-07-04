

.. index::
   pair: sphinx ; conf.py (exlude_patterns)


.. _exclude_patterns:

===================
exclude_patterns
===================

.. seealso:: http://sphinx-doc.org/latest/config.html?highlight=conf#confval-exclude_patterns

::

	if conf_product==’mini’:
		exclude_patterns = ['interface/*.rst',’dialogs/*.rst’]
	elif conf_product==’main’:
		exclude_patterns = ['mini-indexes.rst]
