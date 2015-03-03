

.. index::
   pair: Python ; Fields

===========================
Python field module
===========================

.. seealso::

   - https://github.com/ionelmc/python-fields


.. contents::
   :depth: 3

Features
=========

* Human-readable ``__repr__``
* Complete set of comparison methods
* Keyword and positional argument support. Works like a normal class - you can override just about anything in the
  subclass (eg: a custom ``__init__``). In contrast, `hynek/characteristic <https://github.com/hynek/characteristic>`_
  forces different call schematics and calls your ``__init__`` with different arguments.


Installation
============

.. code-block: sh

    pip install fields

Usage & examples
================

A class that has 2 attributes, ``a`` and ``b``:

.. code:: pycon

    >>> from fields import Fields
    >>> class Pair(Fields.a.b):
    ...     pass
    ...
    >>> p = Pair(1, 2)
    >>> p.a
    1
    >>> p.b
    2
    >>> Pair(a=1, b=2)
    Pair(a=1, b=2)

A class that has one required attribute ``value`` and two attributes (``left`` and ``right``) with default value
``None``:

.. code:: pycon

    >>> class Node(Fields.value.left[None].right[None]):
    ...     pass
    ...
    >>> Node(1, Node(2), Node(3, Node(4)))
    Node(value=1, left=Node(value=2, left=None, right=None), right=Node(value=3, left=Node(value=4, left=None, right=None), right=None))
    >>> Node(1, right=Node(2))
    Node(value=1, left=None, right=Node(value=2, left=None, right=None))


Want tuples?
------------

An alternative to ``namedtuple``:

.. code:: pycon

    >>> from fields import Tuple
    >>> class Pair(Tuple.a.b):
    ...     pass
    ...
    >>> p = Pair(1, 2)
    >>> p.a
    1
    >>> p.b
    2
    >>> tuple(p)
    (1, 2)
    >>> a, b = p
    >>> a
    1
    >>> b
    2

Documentation
=============

https://python-fields.readthedocs.org/

Development
===========

To run all the tests run ``tox`` in your shell (``pip install tox`` if you don't have it)::

    tox

FAQ
===

Why should I use this?
-----------------------

It's less to type, why have quotes around when the names need to be valid symbols anyway. In fact, this is one of the
shortest forms possible to specify a container with fields.

