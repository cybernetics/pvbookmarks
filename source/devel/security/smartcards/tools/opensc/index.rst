
.. index::
   pair: Smartcards; Opensc


.. _open_sc:
.. _opensc:

===========
Open SC
===========

.. seealso::

   - https://github.com/OpenSC/OpenSC/wiki
   - https://github.com/OpenSC/OpenSC/wiki/Frequently-Asked-Questions
   - https://github.com/OpenSC/OpenSC/wiki/Supported-hardware-%28smart-cards-and-USB-tokens%29
   - :ref:`ludovic_rousseau`


.. contents::
   :depth: 3


Introduction
============


OpenSC provides a set of libraries and utilities to work with smart cards.
Its main focus is on cards that support cryptographic operations, and facilitate
their use in security applications such as authentication, mail encryption and
digital signatures. OpenSC implements the  PKCS#11_ API so applications
supporting this API (such as Mozilla Firefox and Thunderbird) can use it.

On the card OpenSC implements the  PKCS#15_ standard and aims to be compatible
with every software/card that does so, too.


.. _PKCS#11: http://www.rsa.com/rsalabs/node.asp?id=2133

.. _PKCS#15: http://www.rsa.com/rsalabs/node.asp?id=2141


Mailing lists
=============

.. seealso::

   - http://lists.sourceforge.net/lists/listinfo/opensc-announce


OpenSC migration (january 2013)
===============================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2013/01/opensc-server-migration.html
   - :ref:`ludovic_rousseau`


New services
------------

The source code repository of the OpenSC project and sub-projects is now at
github: https://github.com/OpenSC

Bug tracker
+++++++++++

.. seealso:: https://github.com/OpenSC/OpenSC/issues

Bug are stored in the Trac instance and are not easy to migrate. One option is
to use github `issues feature`_.


.. _`issues feature`:  https://github.com/OpenSC/OpenSC/issues


Continuous integration
++++++++++++++++++++++

.. seealso::

   - https://opensc.fr/jenkins/
   - https://opensc.fr/jenkins/user/Ludovic




Developer information
======================

.. seealso:: https://www.opensc-project.org/opensc/wiki/DeveloperInformation

If you, as a developer, want to write software that can work with cryptographic
smart cards, you need to orientate in the maze of different APIs.


OpenSC source code
-------------------

.. seealso:: https://github.com/OpenSC/OpenSC





