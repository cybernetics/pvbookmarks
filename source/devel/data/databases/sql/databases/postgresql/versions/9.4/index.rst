

.. index::
   pair: 9.4; PostgreSQL


.. _postgresql_9.4:

====================
PostgreSQL 9.4
====================


.. seealso::

   - http://www.postgresql.org/docs/devel/static/release-9-4.html


.. contents::
   :depth: 3
   
   
Major enhancements in PostgreSQL 9.4 include
=============================================

- Allow materialized views to be refreshed without blocking reads
- Logical decoding allows database changes to be streamed out in a customizable format
- Allow background workers to be dynamically registered, started and terminated
- Add structured (non-text) data type (JSONB) for storing JSON data
- Add SQL-level command ALTER SYSTEM to edit the postgresql.conf configuration file
- Reduce lock levels of some ALTER TABLE commands
