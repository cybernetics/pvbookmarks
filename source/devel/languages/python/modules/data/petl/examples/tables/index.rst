

.. index::
   pair: Tables; Petl


.. _petl_tables:

==================
Tables petl look
==================

.. contents::
   :depth: 3

petl.look
==========


::

    petl.look(table, *sliceargs, **kwargs)

Format a portion of the table as text for inspection in an interactive 
session. E.g.::


    >>> from petl import look
    >>> table = [['foo', 'bar'], ['a', 1], ['b', 2]]
    >>> look(table)
    +-------+-------+
    | 'foo' | 'bar' |
    +=======+=======+
    | 'a'   | 1     |
    +-------+-------+
    | 'b'   | 2     |
    +-------+-------+



Any irregularities in the length of header and/or data rows will appear 
as blank cells, e.g.::


    >>> table = [['foo', 'bar'], ['a'], ['b', 2, True]]
    >>> look(table)
    +-------+-------+------+
    | 'foo' | 'bar' |      |
    +=======+=======+======+
    | 'a'   |       |      |
    +-------+-------+------+
    | 'b'   | 2     | True |
    +-------+-------+------+

Changed in version 0.3.

Positional arguments can be used to slice the data rows. The sliceargs 
are passed to itertools.islice().

Changed in version 0.8.

The properties n and p can be used to look at the next and previous 
rows respectively. I.e., try >>> look(table) then >>> _.n then >>> _.p.

Changed in version 0.13.

Three alternative presentation styles are available: ‘grid’, ‘simple’ 
and ‘minimal’, where ‘grid’ is the default. A different style can be 
specified using the style keyword argument, e.g.


Petl look(table, style='simple')
=================================

.. seealso::

   - :ref:`rest_simple_tables`


::

    >>> table = [['foo', 'bar'], ['a', 1], ['b', 2]]
    >>> look(table, style='simple')
    =====  =====
    'foo'  'bar'
    =====  =====
    'a'        1
    'b'        2
    =====  =====


.. _petl_tables_minimal:

Petl look(table, style='minimal')
==================================

::

    >>> look(table, style='minimal')
    'foo'  'bar'
    'a'        1
    'b'        2



The default style can also be changed, e.g.::

    >>> look.default_style = 'simple'
    >>> look(table)
    =====  =====
    'foo'  'bar'
    =====  =====
    'a'        1
    'b'        2
    =====  =====



.. _petl_tables_grid:

Petl look.default_style = 'grid'
=================================

.. seealso::

   - :ref:`rest_grid_tables`


::


    >>> look.default_style = 'grid'
    >>> look(table)
    +-------+-------+
    | 'foo' | 'bar' |
    +=======+=======+
    | 'a'   |     1 |
    +-------+-------+
    | 'b'   |     2 |
    +-------+-------+    

    See also lookall() and see().



   
