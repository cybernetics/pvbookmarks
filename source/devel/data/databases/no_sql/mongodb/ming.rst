

.. index::
   pair: ming ; mongodb

.. _python_ming_mongodb:

=====================
Python ming framework
=====================

.. seealso::

   - http://merciless.sourceforge.net/index.html


MongoDB is a high-performance schemaless database that allows you to store and
retrieve JSON-like documents. MongoDB stores these documents in collections,
which are analogous to SQL tables.

Because MongoDB is schemaless, there are no guarantees given to the database
client of the format of the data that may be returned from a query; you can put
any kind of document into a collection that you want.


While this dynamic behavior is handy in a rapid development environment where
you might delete and re-create the database many times a day, it starts to be
a problem when you need to make guarantees of the type of data in a collection
(because you code depends on it).

The goal of Ming is to allow you to specify the schema for your data in Python
code and then develop in confidence, knowing the format of data you get from a
query.


