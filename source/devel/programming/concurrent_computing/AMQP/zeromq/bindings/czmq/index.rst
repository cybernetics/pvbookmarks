
.. index::
   czmq library high-level C binding for ØMQ


.. _czmq_library:

===============
C czmq library
===============

.. seealso::

   - http://twitter.com/#!/hintjens
   - http://zguide.zeromq.org/
   - http://czmq.zeromq.org/manual:czmq


Code
====

::

    git clone git://github.com/zeromq/czmq.git


Name
====

::

    czmq - high-level C binding for ØMQ



Synopsis
========

::

    #include <czmq.h>

    cc ['flags'] 'files' -lzmq -lczmq ['libraries']

Description
===========

Scope and goals
---------------

czmq has these goals:

- To wrap the ØMQ core API in semantics that are natural and lead to shorter,
  more readable applications.
- To hide the differences between versions of ØMQ.
- To provide a space for development of more sophisticated API semantics.


