

.. index::
   pair: IndexedDB ; database
   pair: No-SQL ; IndexedDB

.. _indexedDB_database:

===================
IndexedDB database
===================

.. seealso::

   - https://developer.mozilla.org/en/IndexedDB
   - http://www.html5rocks.com/en/tutorials/indexeddb/todo/



.. contents::
   :depth: 3


Introduction
============


IndexedDB is an API for client-side storage of significant amounts of structured
data and for high performance searches on this data using indexes.

While DOM Storage is useful for storing smaller amounts of data, it is less
useful for storing larger amounts of structured data. IndexedDB provides a solution.

IndexedDB provides separate APIs for synchronous and asynchronous access.

The synchronous API is intended to be used inside workers.


Basic Concepts About IndexedDB
==============================


.. seealso:: https://developer.mozilla.org/en/IndexedDB/Basic_Concepts_Behind_IndexedDB

IndexedDB is a way for you to persistently store data inside a user's browser.

Because it lets you create web applications with rich query abilities, these
applications can work both online and offline.

IndexedDB is useful for applications that store a large amount of data
(for example, a catalog of DVDs in a lending library) and applications that
don't need persistent internet connectivity to work (for example, mail clients,
to-do lists, and notepads)

Soma IndexedDB applications
===========================

.. seealso:: http://hacks.mozilla.org/2012/02/announcing-the-december-dev-derby-winners/

- 1st Place: eLibri_ by mar.castelluccio
- 2nd Place: FileSystemDB_ by mar.castelluccio
- 3rd Place: `IndexedDB Editor`_ by twolfson


.. _eLibri:  https://developer.mozilla.org/en-US/demos/detail/elibri
.. _FileSystemDB:   https://developer.mozilla.org/en-US/demos/detail/filesystemdb
.. _`IndexedDB Editor`:  https://developer.mozilla.org/en-US/demos/detail/indexeddb-editor




