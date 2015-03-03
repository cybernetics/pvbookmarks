

.. index::
   pair: Leveldb ; Database
   pair: Nosql database ; Leveldb

.. _leveldb_database:

=================
Leveldb database
=================

.. seealso::

   - http://code.google.com/p/leveldb/
   - http://peter-hoffmann.com/2011/installation-leveldb-ubuntu-python.html



.. contents::
   :depth: 3

Introduction
=============

LevelDB is a fast key-value storage library written at Google that provides an
ordered mapping from string keys to string values.


Features
========

- Keys and values are arbitrary byte arrays.
- Data is stored sorted by key.
- Callers can provide a custom comparison function to override the sort order.
- The basic operations are Put(key,value), Get(key), Delete(key).
- Multiple changes can be made in one atomic batch.
- Users can create a transient snapshot to get a consistent view of data.
- Forward and backward iteration is supported over the data.
- Data is automatically compressed using the `Snappy compression library`_.
- External activity (file system operations etc.) is relayed through a virtual
  interface so users can customize the operating system interactions.
- `Detailed documentation`_ about how to use the library is included with the source code.


.. _`Detailed documentation`:  http://leveldb.googlecode.com/svn/trunk/doc/index.html
.. _`Snappy compression library`:  http://code.google.com/p/snappy/
