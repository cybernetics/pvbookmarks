

.. index::
   pair: hash functions; hashlib
   pair: message; digests
   pair: secure ; hash

.. _hashlib_module:

======================
hashlib python module
======================

.. seealso::

   - http://docs.python.org/library/hashlib.html#module-hashlib
   - :ref:`python_sha3`



.. contents::
   :depth: 3


Presentation
============


This module implements a common interface to many different ``secure hash`` and
``message digest`` algorithms.

Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384, and
SHA512 (defined in FIPS 180-2) as well as RSA’s MD5 algorithm (defined in Internet RFC 1321).

The terms secure hash and message digest are interchangeable.

Older algorithms were called ``message digests``.
The modern term is ``secure hash``.


Example
=======

For example, to obtain the digest of the string ``'Nobody inspects the spammish repetition'``::

   >>> import hashlib
   >>> m = hashlib.md5()
   >>> m.update("Nobody inspects")
   >>> m.update(" the spammish repetition")
   >>> m.digest()
   '\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'
   >>> m.digest_size
   16
   >>> m.block_size
   64


More condensed:

   >>> hashlib.sha256("Nobody inspects the spammish repetition").hexdigest()
   'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'



A generic :func:`new` constructor that takes the string name of the desired
algorithm as its first parameter also exists to allow access to the above listed
hashes as well as any other algorithms that your OpenSSL library may offer.  The
named constructors are much faster than :func:`new` and should be preferred.

Using :func:`new` with an algorithm provided by OpenSSL:

   >>> h = hashlib.new('ripemd160')
   >>> h.update("Nobody inspects the spammish repetition")
   >>> h.hexdigest()
   'cc4a5ce1b3df48aec5d22d1f16b894a0b894eccc'


Python SHA3
===========

- ref:`python_sha3`


