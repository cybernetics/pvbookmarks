

.. index::
   pair: Csvkit;  Sql
   ! Csvsql


.. _csvsql_2014:

================================================================================
csvsql, you can truly execute SQL queries on one or more CSV files 25 mai 2014
================================================================================

.. seealso::

   - https://github.com/onyxfish/csvkit/pull/276



Courriel
=========

::

    De:	 Jeroen Janssens <notifications@github.com>
    à:	 onyxfish/csvkit <csvkit@noreply.github.com>
    Date:	 25 mai 2014 06:26
    Objet:	 [csvkit] Execute SQL queries directly on one or more CSV files (#276)
    liste de diffusion:	 csvkit.onyxfish.github.com Filtrer les messages de cette liste de diffusion


In #259, with the new tool sql2csv, it was already suggested that you could 
execute SQL queries directly on CSV files using a hacky bash script. 

Now, with these small changes to csvsql, you can truly execute SQL queries on 
one or more CSV files.

This functionality is similar to TextQL and Q. However, thanks to the solid 
codebase of csvkit, csvsql offers both multiple tables and proper escaping of
output. 
 
The following example, which joins two data sets that can be found in the 
examples directory, illustrates the changes:

::

    < iris.csv python ../csvkit/utilities/csvsql.py --query 'select m.usda_id, avg(i.sepal_length) as mean_sepal_length from stdin as i join irismeta as m on (i.species = m.species) group by m.species' irismeta.csv | csvlook
    
    

::
    
    |----------+--------------------|
    |  usda_id | mean_sepal_length  |
    |----------+--------------------|
    |  IRSE    | 5.006              |
    |  IRVE2   | 5.936              |
    |  IRVI    | 6.588              |
    |----------+--------------------|

Note that you can now mix standard input and filenames. 

It is no longer necessary to specify --table when standard input is provided. 
Tables based on standard input are named "stdin" by default. 

Table names can still be overridden by specifying a (comma delimited) string to ``--tables``. 

When ``--query`` is specified and ``--db`` is not, **sqlite:///:memory:** is used 
as the connection string and ``--insert`` is set to True. 

Multiple SQL queries can be specified by using ";" as a delimiter. Only the output 
of the last query is outputted as CSV. 

This allows you to execute SQL queries in memory.

No functionality has been removed. 

Appropriate tests have been added. I'll write the corresponding documentation 
once these changes have been accepted.


Commit Summary
===============

- Mix filenames and stdin, execute SQL queries, output final result as CSV
- Change method of detecting available stdin
- Add two new example datasets
- Add tests for executing SQL query in memory and for mixing stdin and filenames
- Remove comma from value

File Changes
============

- M csvkit/utilities/csvsql.py (126)
- A examples/iris.csv (151)
- A examples/irismeta.csv (4)
- M tests/test_utilities/test_csvsql.py (41)


