

.. index::
   pair: Arangodb ; Database
   pair: No-SQL ; Arangodb

.. _arangodb:

=====================
Arangodb database
=====================

.. seealso::

   - https://www.arangodb.org/
   - http://arangodb-python-driver.readthedocs.org/en/latest/glossary.html


.. figure:: arangodb_logo2.png
   :align: center

The multi-purpose NoSQL DB
==========================


An open-source database with a flexible data model for documents, graphs, and 
key-values. 

Build high performance applications using a convenient sql-like query language 
or JavaScript extensions.


Interesting facts
------------------

ArangoDB needs in many scenarios less space than :ref:`MongoDB <mongodb>` as it saves the 
structure of a document and the document itself separately – and reuses the 
structure definition for the next document with the same structure.


Key features
=============

* Schema-free schemata let you combine the space efficiency of MySQL with the
  performance power of NoSQL
* Use ArangoDB as an application server and fuse your application and database
  together for maximal throughput
* JavaScript for all: no language zoo, you can use one language from your
  browser to your back-end
* ArangoDB is multi-threaded - exploit the power of all your cores
* Flexible data modeling: model your data as combination of key-value pairs,
  documents or graphs - perfect for social relations
* Free index choice: use the correct index for your problem, be it a skip list
  or a fulltext search
* Configurable durability: let the application decide if it needs more
  durability or more performance
* No-nonsense storage: ArangoDB uses all of the power of modern storage
  hardware, like SSD and large caches
* Powerful query language (AQL) to retrieve data
* Transactions: run queries on multiple documents or collections with optional 
  transactional consistency and isolation
* Replication: set up the database in a master-slave configuration
* It is open source (Apache Licence 2.0)


Source code
===========

.. seealso:: https://github.com/triAGENS/ArangoDB



ArangoDB Driver for Python
===========================

.. seealso:: http://arangodb-python-driver.readthedocs.org/en/latest/


Driver for Python is not entirely completed. 

It supports Connections to ArangoDB with custom options, Collections, Documents, 
Indexes Cursors and partially Edges.


