
.. index::
   pair: Petl; Examples


.. _petl_examples:

===============================================================
petl  examples
===============================================================


.. contents::
   :depth: 3



valuecounts
============

::

    petl.valuecounts(table, *fields, **kwargs)

Find distinct values for the given field and count the number and relative 
frequency of occurrences. Returns a table mapping values to counts, with 
most common values first. E.g.::

    >>> from petl import valuecounts, look
    >>> table = [['foo', 'bar'], ['a', True], ['b'], ['b', True], ['c', False]]
    >>> look(valuecounts(table, 'foo'))
    +---------+---------+-------------+
    | 'value' | 'count' | 'frequency' |
    +=========+=========+=============+
    | 'b'     | 2       | 0.5         |
    +---------+---------+-------------+
    | 'a'     | 1       | 0.25        |
    +---------+---------+-------------+
    | 'c'     | 1       | 0.25        |
    +---------+---------+-------------+

    >>> look(valuecounts(table, 'bar'))
    +---------+---------+--------------------+
    | 'value' | 'count' | 'frequency'        |
    +=========+=========+====================+
    | True    | 2       | 0.6666666666666666 |
    +---------+---------+--------------------+
    | False   | 1       | 0.3333333333333333 |
    +---------+---------+--------------------+



Avec sqlite3
============

::

    petl.fromdb(dbo, query, *args, **kwargs)

Provides access to data from any DB-API 2.0 connection via a given query. 
E.g., using sqlite3::

    >>> import sqlite3
    >>> from petl import look, fromdb
    >>> connection = sqlite3.connect('test.db')
    >>> table = fromdb(connection, 'select * from foobar')
    >>> look(table)


Building tables with petl 
=========================

.. toctree::
   :maxdepth: 3
   
   
   tables/index


csv example
============

.. toctree::
   :maxdepth: 3
   
   
   csv/index
   
