
.. index::
   pair: Pypi; crate.io



.. _crate_io:

============================
crate.io
============================

.. seealso::

   - https://crate.io/
   - https://github.com/crateio
   - https://github.com/crateio/crate.io
   - :ref:`python_install_history`

.. contents::
   :depth: 3


Introduction
============

Crate is a PyPI Mirror/Python Package Index that was written to make it easy to
discover packages, evaluate them for usefulness, and then install them.

Additionally it also focuses on presenting an extremely stable interface to PyPI
compatible applications (e.g. pip).

With Crate you should be able to quickly find, evaluate, and install your
packages with no worries about if something is going to be down or not.


Technology Stack
================

Crate.io is built on top of Python using the Django framework.

It uses:

- Celery to process its shared tasks,
- PostgreSQL to store its data,
- and Redis as its caching layer.


Relation to PyPI
================

The software that powers Crate.io defaults to PyPI, but can technically be used
with any index that presents the same XML-RPC API.

Crate.io the website currently only mirrors PyPI. All packages and their
associated data come from PyPI. Crate.io provides a reliable place for those
packages to be stored and accessed and tries to present a cleaner and more
user-friendly interface to that data.


crate.web
=========

.. seealso::

   - https://github.com/crateio/crate.web

Django Application Providing a Python Package Index.


warehouse
=========



Warehouse is a BSD Licensed API driven Python package index.

Warehouse is a re-envisioning of a Python package index.

It is based around the idea of a clean API that exposes a developer friendly API.

It focuses strongly on making it possible for clients to efficiently query the
available meta-data and provide, and where possible enforce, practices and
tooling that enable an end to end secure installation story.

Warehouse is part of the Crate project, a set of applications, tools, and
libraries for creating, distributing, and installing Python packages in a
secure, efficient, and reliable way.


