

.. index::
   pair: data ; MessagePack
   pair: zerorpc ; zeromq
   ! MessagePack


.. _message_pack_format:

=========================================
MessagePack format
=========================================

.. seealso::

   - http://msgpack.org/



.. contents::
   :depth: 3


Introduction
============

It's like JSON. but fast and small.

MessagePack is an efficient binary serialization format.

It lets you exchange data among multiple languages like JSON but it's faster and
smaller. For example, small integers (like flags or error code) are encoded into
a single byte, and typical short strings only require an extra byte in addition
to the strings themselves.

If you ever wished to use JSON for convenience (storing an image with metadata)
but could not for technical reasons (encoding, size, speed...), MessagePack is a
perfect replacement.


Related projects
================

zerorpc-python
--------------

.. seealso:: https://github.com/dotcloud/zerorpc-python


zerorpc is a flexible RPC implementation based on zeromq and messagepack.

Service APIs exposed with zerorpc are called "zeroservices".

zerorpc can be used programmatically or from the command-line. It comes with a
convenient script, "zerorpc", allowing to:

- expose Python modules without modifying a single line of code,
- call those modules remotely through the command line.
