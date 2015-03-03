

.. index::
   pair: sphinx ; guilabel


.. _sphinx_guilabel_s:

==============================
guilabel
==============================


.. seealso:: http://sphinx-doc.org/latest/markup/inline.html?highlight=guilabel#role-guilabel

Labels presented as part of an interactive user interface should be marked
using ``:guilabel:``.

This includes labels from text-based interfaces such as those created using
curses or other text-based libraries.

Any label used in the interface should be marked with this role, including:

- button labels,
- window titles,
- field names,
- menu and
- menu selection names,
- and even values in selection lists.

Changed in version 1.0: An accelerator key for the GUI label can be included
using an ampersand; this will be stripped and displayed underlined in the output
(example: :guilabel:`&Cancel`).

To include a literal ampersand, double it.



Example  1
==========

::

     button :guilabel:`Start`



button :guilabel:`Start`


Example 2  ampersand accelerators
=================================

``guilabel`` also supports ampersand accelerators just like guilabel.


::

     button :guilabel:`&Start`



button :guilabel:`&Start`

