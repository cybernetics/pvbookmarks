

.. index::
   pair: USB CCID ; libpcsclite
   pair: PC/SC ; API


.. _libpcsclite:

===========
libpcsclite
===========

.. seealso::

   - :ref:`ludovic_rousseau`


.. contents::
   :depth: 3


Introduction
============


Middleware to access a smart card using SCard API (PC/SC).

Source code available from http://svn.debian.org/wsvn/pcsclite/trunk/PCSC/

- http://ludovicrousseau.blogspot.com/
- http://pcsclite.alioth.debian.org/

- `Project page <https://alioth.debian.org/projects/pcsclite/>`_
- `Download <https://alioth.debian.org/project/showfiles.php?group_id=30105>`_
- Subversion repository:

      * `viewsvn <http://svn.debian.org/viewsvn/pcsclite/trunk/PCSC/>`_
      * `wsvn <http://svn.debian.org/wsvn/pcsclite/trunk/PCSC/>`_
      * svn co svn://svn.debian.org/pcsclite/trunk/PCSC


`Ludovic Rousseau's blog about PC/SC and smart cards <http://ludovicrousseau.blogspot.com/>`_


Documentation
=============

* `PC/SC Lite API (WinSCard) <http://pcsclite.alioth.debian.org/api/group__API.html>`_
* `IFD Handler API v3.0 <http://pcsclite.alioth.debian.org/api/group__IFDHandler.html>`_
* `PC/SC internals documented with Doxygen <http://pcsclite.alioth.debian.org/api/index.html>`_


PC/SC API spy
==============

.. toctree::
   :maxdepth: 4

   api_spy/index

pcsclite installation
=====================

.. toctree::
   :maxdepth: 4

   install/index


pcsclite news
=====================

.. toctree::
   :maxdepth: 4

   news/news
   
   

Versions
========

.. toctree::
   :maxdepth: 4

   versions/index


Debug
=====

.. toctree::
   :maxdepth: 4

   debug/index


.. index::
   pair: DBUS ; PC/SC


.. _pcsc_DBUS:

pcscs and DBUS
==============

.. literalinclude:: pcsc-watcher.py











