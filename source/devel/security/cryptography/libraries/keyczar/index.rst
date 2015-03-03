
.. index::
   pair: crytography ; keyczar

.. _keyczar_library:

====================
keyczar library
====================


.. seealso::

   - http://code.google.com/p/keyczar/



.. contents::
   :depth: 3


Introduction
============

Keyczar is an open source cryptographic toolkit designed to make it easier and
safer for devlopers to use cryptography in their applications.

Keyczar supports authentication and encryption with both symmetric and asymmetric
keys. Some features of Keyczar include:

- A simple API
- Key rotation and versioning
- Safe default algorithms, modes, and key lengths
- Automated generation of initialization vectors and ciphertext signatures
- Java, Python, and C++ implementations

Why Keyczar ?
=============

Cryptography is easy to get wrong.

Developers can often choose the wrong cipher mode, use obsolete algorithms,
compose primitives in an unsafe manner, or fail to anticipate the need for
key rotation. Keyczar abstracts some of these details by choosing safe defaults,
automatically tagging outputs with key version information, and providing a
simple interface.

Keyczar is designed to be open, extensible, and cross-platform compatible.

It is not intended to replace existing cryptographic libraries like OpenSSL,
PyCrypto, or the Java JCE, and in fact is built on these libraries.




