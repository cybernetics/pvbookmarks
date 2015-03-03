
.. index::
   pair: zerorpc; zmq


.. _zerorpc:

===================
zerorpc-python
===================


.. seealso::

   - https://github.com/dotcloud/zerorpc-python
   - :ref:`message_pack_format`



zerorpc is a flexible RPC implementation based on zeromq and messagepack.

Service APIs exposed with zerorpc are called "zeroservices".

zerorpc can be used programmatically or from the command-line. It comes with a
convenient script, "zerorpc", allowing to:

- expose Python modules without modifying a single line of code,
- call those modules remotely through the command line.
