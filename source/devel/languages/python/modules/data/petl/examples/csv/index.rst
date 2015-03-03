
.. index::
   pair: Data; CSV


.. _data_csv:

==================
csv petl Examples
==================

.. contents::
   :depth: 3
   
   

E.g., given the following data in a file at 'example.csv' in the current working directory::

    foo,bar,baz
    a,1,3.4
    b,2,7.4
    c,6,2.2
    d,9,8.1

...the interactive session below illustrates some simple uses of this module::

    >>> from petl import *
    >>> table1 = fromcsv('example.csv')
    >>> look(table1)
    +-------+-------+-------+
    | 'foo' | 'bar' | 'baz' |
    +=======+=======+=======+
    | 'a'   | '1'   | '3.4' |
    +-------+-------+-------+
    | 'b'   | '2'   | '7.4' |
    +-------+-------+-------+
    | 'c'   | '6'   | '2.2' |
    +-------+-------+-------+
    | 'd'   | '9'   | '8.1' |
    +-------+-------+-------+

    >>> table2 = convert(table1, 'foo', 'upper')
    >>> table3 = convert(table2, 'bar', int)
    >>> table4 = convert(table3, 'baz', float)
    >>> table5 = extend(table4, 'quux', expr('{bar} * {baz}'))
    >>> table6 = cut(table5, 'foo', 'quux')
    >>> table7 = selectgt(table6, 'quux', 10)
    >>> table8 = sort(table7, 'quux')
    >>> look(table8)
    +-------+--------------------+
    | 'foo' | 'quux'             |
    +=======+====================+
    | 'C'   | 13.200000000000001 |
    +-------+--------------------+
    | 'B'   | 14.8               |
    +-------+--------------------+
    | 'D'   | 72.89999999999999  |
    +-------+--------------------+

        >>> tocsv(table8, 'output.csv')

