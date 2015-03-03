

.. index::
   pair: hash functions; passlib
   pair: hash functions; SHA256


.. _passlib_library:

======================
passlib
======================

.. seealso::

   - https://code.google.com/p/passlib/
   - http://packages.python.org/passlib/


.. figure:: logo_passlib.png

   Passlib package



.. contents::
   :depth: 3


Presentation
============


Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 30 password hashing algorithms, as well
as a framework for managing existing password hashes.

It’s designed to be useful for a wide range of tasks, from verifying a hash
found in :file:`/etc/shadow`, to providing full-strength password hashing for
multi-user application.


Source
======

.. seealso:: https://code.google.com/p/passlib/source

Get a local copy of the passlib repository with this command::

    hg clone https://code.google.com/p/passlib/


Example
=======

As a quick sample, the following code hashes and then verifies a password
using the algorithm::

    >>> # import the hash algorithm
    >>> from passlib.hash import sha256_crypt

    >>> # generate new salt, and hash a password
    >>> hash = sha256_crypt.encrypt("toomanysecrets")
    >>> hash
    '$5$rounds=80000$zvpXD3gCkrt7tw.1$QqeTSolNHEfgryc5oMgiq1o8qCEAcmye3FoMSuvgToC'

    >>> # verifying the password
    >>> sha256_crypt.verify("toomanysecrets", hash)
    True
    >>> sha256_crypt.verify("joshua", hash)
    False





