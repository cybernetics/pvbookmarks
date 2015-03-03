
.. index::
   pair: zeromq; glimpse


.. _glimpse_zeromq:

===================
glimpse
===================


.. seealso::

   - http://packages.python.org/glimpse/index.html
   - http://packages.python.org/glimpse/manual/pools/gearman_pool.html


This worker pool uses a `Gearman <http://gearman.org/>`_ job server to
manage the list of tasks (i.e., function invocations), and a small number of
`ZeroMQ <http://www.zeromq.org/>`_ channels for logging and command
communication. To create a new Gearman cluster pool, use the
MakePool function as::

   >>> config_file = "config.ini"
   >>> pool = glimpse.pools.gearman_cluster.MakePool(config_file)
   >>> pool.map(hex, [1, 2, 3])
   ['0x1', '0x2', '0x3']
