

.. index::
   pair: CSV; Python-table-fu


.. _csv_python_table_fu:

===============
Python table-fu
===============

.. seealso::

   - https://github.com/eyeseast/python-tablefu
   
 
.. contents::
   :depth: 3 
 
Introduction
=============

   
Python TableFu is a tool for manipulating spreadsheet-like tables in 
Python. 

It began as a Python implementation of ProPublica's [TableFu]
(http://propublica.github.com/table-fu/), though new methods have been 
added. 

TableFu allows filtering, faceting and manipulating of data. 

Going  forward, the project aims to create something akin to an ORM for 
spreadsheets.

Usage
======

::

    >>> from table_fu import TableFu
    >>> table = TableFu.from_file('tests/test.csv')
    >>> table.columns
    ['Author', 'Best Book', 'Number of Pages', 'Style']

    # get all authors
    >>> table.values('Author')
    ['Samuel Beckett', 'James Joyce', 'Nicholson Baker', 'Vladimir Sorokin']

    # total a column
    >>> table.total('Number of Pages')
    1177.0
    
    # filtering a table returns a new instance
    >>> t2 = table.filter(Style='Modernism')
    >>> list(t2)
    [<Row: Samuel Beckett, Malone Muert, 120, Modernism>,
     <Row: James Joyce, Ulysses, 644, Modernism>]
    
    
    # each TableFu instance acts like a list of rows
    >>> table[0]
    <Row: Samuel Beckett, Malone Muert, 120, Modernism>
    
    list(table.rows)
    [<Row: Samuel Beckett, Malone Muert, 120, Modernism>,
     <Row: James Joyce, Ulysses, 644, Modernism>,
     <Row: Nicholson Baker, Mezannine, 150, Minimalism>,
     <Row: Vladimir Sorokin, The Queue, 263, Satire>]
    
    # rows, in turn, act like dictionaries
    >>> row = table[1]
    >>> print row['Author']
    James Joyce
    
    # transpose a table
    >>> t2 = table.transpose()
    >>> list(t2)
    [<Row: Best Book, Malone Muert, Ulysses, Mezannine, The Queue>,
     <Row: Number of Pages, 120, 644, 150, 263>,
     <Row: Style, Modernism, Modernism, Minimalism, Satire>]
    
    >>> t2.columns
    ['Author',
     'Samuel Beckett',
     'James Joyce',
     'Nicholson Baker',
     'Vladimir Sorokin']
    
    # sort rows
    >>> table.sort('Author')
    >>> table.rows
    [<Row: James Joyce, Ulysses, 644, Modernism>,
     <Row: Nicholson Baker, Mezannine, 150, Minimalism>,
     <Row: Samuel Beckett, Malone Muert, 120, Modernism>,
     <Row: Vladimir Sorokin, The Queue, 263, Satire>]
    
    # sorting is stored
    table.options['sorted_by']
    {'Author': {'reverse': False}}
    
    # which is handy because...
    
    # tables can also be faceted (and options are copied to new tables)
    >>> for t in table.facet_by('Style'):
    ...     print t.faceted_on
    ...     t.table
    Minimalism
    [['Nicholson Baker', 'Mezannine', '150', 'Minimalism']]
    Modernism
    [['Samuel Beckett', 'Malone Muert', '120', 'Modernism'],
     ['James Joyce', 'Ulysses', '644', 'Modernism']]
    Satire
    [['Vladimir Sorokin', 'The Queue', '263', 'Satire']]

Here's an [advanced example](https://gist.github.com/765321) that uses 
faceting and filtering to produce aggregates from [this spreadsheet]
(https://spreadsheets.google.com/ccc?key=0AprNP7zjIYS1dG5wbVJpWTVacWpUaUh5VHUxMk1wTEE&hl=en&authkey=CJfB5MYP) 
(extracted from the New York Times Congress API).

   
