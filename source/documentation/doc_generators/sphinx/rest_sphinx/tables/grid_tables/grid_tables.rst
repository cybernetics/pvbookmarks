

.. index::
   pair: Grid ; Tables


.. _rest_grid_tables:

=====================
Rest **grid tables**
=====================

.. seealso::

   - :ref:`petl_tables_grid`
   - http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables
   - http://rest-sphinx-memo.readthedocs.org/en/latest/ReST.html#tables


Two forms of tables are supported.  

For `*grid tables* <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables>`_
you have to "paint" the cell grid yourself.  


They look like this::

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | ...        | ...      |          |
   +------------------------+------------+----------+----------+
   


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+


Examples
---------

::

    +---------------------------------+------------+
    | Condition                       | Decision   |
    +=================================+============+
    | comparison score >= threshold   | Match      | 
    +---------------------------------+------------+
    | comparison score < threshold    | Non-Match  | 
    +---------------------------------+------------+
    
    
Result
    

+---------------------------------+------------+
| Condition                       | Decision   |
+=================================+============+
| comparison score >= threshold   | Match      | 
+---------------------------------+------------+
| comparison score < threshold    | Non-Match  | 
+---------------------------------+------------+

      

