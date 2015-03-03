

.. index::
   pair: Python; SHA3

.. _python_sha3:

======================
python sha3
======================

.. seealso::

   - https://github.com/bjornedstrom/python-sha3
   - :ref:`sha3_keccak`
   - :ref:`hashlib_module`


.. contents::
   :depth: 3


Presentation
============


This module implements SHA-3 (also known as Keccak) with a hashlib-like interface.

The module is written as a Python C extension on top of the reference
implementation.

This yields better performance than the pure Python implementation that is
available on the Keccak website.

Sample usage
============

::

    import sha3
    s = sha3.SHA3512() # also 224, 256, 384, 512
                       # also exposed as the function sha3.sha3_512(...)
    s.update('foo')
    print s.hexdigest()

Importing the sha3 module will also add the new modules to hashlib.::

    >>> import hashlib
    >>> import sha3
    >>> hashlib.sha3_512('foo')
    <sha3.SHA3512 object at 0x7fcd0fcb7590>


