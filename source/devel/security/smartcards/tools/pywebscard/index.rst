


.. index::
   ! pyscard
   pair: smartcard tools ; WebScard
   pair: python smartcard tools ; WebScard

.. _webscard:

========
WebScard
========

.. seealso::

   - https://bitbucket.org/benallard/webscard/overview
   - :ref:`pcsc`
   - :ref:`pythoncard`



.. contents::
   :depth: 3


Overview
=========

This is a web application acting as a universal smartcard proxy : it provides a
web interface to a smartcard, together with detailled logs about the communication
passing by.

One of the goals is to allow testing of software which necessitate a smartcard
from a computer without a readers.

It is meant to support different implementations of smartcards:

- Software emulations of javacards applets (via pycsc and pythoncard for instance)
- or real smartcards (via pyscard in this case).



