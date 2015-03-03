
.. index::
   pair: Search; Sqlite

.. _sqlite_search_mai_2014:

========================================================
Using SQLite Full-Text Search with Python (may 12 2014)
========================================================


.. seealso::

   - http://charlesleifer.com/blog/using-sqlite-full-text-search-with-python/
   - http://charlesleifer.com/blog/search/?q=peewee+AND+sqlite
   - :ref:`peewee_articles_2014`



In this post I will show how to use SQLite full-text search with Python (and a 
lot of help from peewee ORM). 

We will see how to index content for searching, how to perform searches, and 
how to order search results using two ranking algorithms.

Last week I migrated my site from Postgresql to SQLite. I had been using Redis 
to power my site's search, but since SQLite has an awesome full-text search 
extension, I decided to give it a try. 

I am really pleased with the results, and being able to specify boolean search 
queries is an added plus. 


